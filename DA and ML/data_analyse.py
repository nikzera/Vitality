import pandas as pd

# 读取数据文件，确认分隔符是否为逗号
try:
    df = pd.read_csv("ARN-20240625-gsv-labeled.txt", sep=",")  # gsv数据名称
except FileNotFoundError:
    print("数据文件未找到，请确认文件名和路径是否正确。")
    exit()

# 打印列名以确认是否正确读取
print("列名:", df.columns.tolist())

# 确认列名是否正确
required_columns = ['ts', 'id', 'snr', 'inside_outside']
for col in required_columns:
    if col not in df.columns:
        print(f"列 '{col}' 不存在，请检查数据文件的格式。")
        exit()

# 按时间戳排序
df = df.sort_values(by='ts').reset_index(drop=True)

# 计算每个时间戳中 snr 为0的卫星数量
df['snr_zero'] = df['snr'] == 0
snr_zero_counts = df.groupby('ts')['snr_zero'].sum().reset_index()
snr_zero_counts.rename(columns={'snr_zero': 'snr_zero_count'}, inplace=True)

# 计算每个时间戳相比上一个时间戳 snr 为0的变化
snr_zero_counts['snr_zero_change'] = snr_zero_counts['snr_zero_count'].diff().fillna(0).astype(int)

# 分组统计（包括 snr 为 0 的卫星）
grouped = df.groupby('ts').agg(
    satellite_count=('id', 'count'),
    average_snr=('snr', 'mean'),
    inside_outside=('inside_outside', 'first')
).reset_index()

# 将 average_snr 转换为整数
grouped['average_snr'] = grouped['average_snr'].round().astype(int)

# 计算每个时间戳相比上一个时间戳的平均 snr 改变
grouped['average_snr_change'] = grouped['average_snr'].diff().fillna(0).astype(int)

# 合并 snr_zero_counts 数据
grouped = pd.merge(grouped, snr_zero_counts, on='ts', how='left')

# 将结果写入另一个 txt 文件
output_file = "output.txt"
with open(output_file, 'w') as f:
    f.write("ts,satellite_count,average_snr,average_snr_change,snr_zero_count,snr_zero_change,inside_outside\n")
    for _, row in grouped.iterrows():
        f.write(
            f"{row['ts']},{row['satellite_count']},{row['average_snr']},{row['average_snr_change']},{row['snr_zero_count']},{row['snr_zero_change']},{row['inside_outside']}\n")

print(f"结果已写入 {output_file}")