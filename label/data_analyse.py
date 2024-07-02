import pandas as pd

# 读取数据文件，确认分隔符是否为逗号
try:
    df = pd.read_csv("ARN-20240611-gsv-labeled.txt", sep=",") #gsv数据名称
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

# 分组统计
grouped = df.groupby('ts').agg(
    satellite_count=('id', 'count'),
    average_snr=('snr', 'mean'),
    inside_outside=('inside_outside', 'first')
).reset_index()

# 将average_snr转换为整数
grouped['average_snr'] = grouped['average_snr'].round().astype(int)

# 计算每个时间戳增加或减少的卫星数量
grouped['satellite_change'] = grouped['satellite_count'].diff().fillna(0).astype(int)

# 将结果写入另一个txt文件
output_file = "output.txt"
with open(output_file, 'w') as f:
    f.write("ts,satellite_count,average_snr,satellite_change,inside_outside\n")
    for _, row in grouped.iterrows():
        f.write(f"{row['ts']},{row['satellite_count']},{row['average_snr']},{row['satellite_change']},{row['inside_outside']}\n")

print(f"结果已写入 {output_file}")