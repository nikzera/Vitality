import pandas as pd

# 读取CSV文件
csv_file = "ARN-20240625.txt"
data = pd.read_csv(csv_file)

# 创建ARFF文件的头部信息
arff_header = """@relation satellite_data

@attribute ts numeric
@attribute satellite_count numeric
@attribute average_snr numeric
@attribute average_snr_change numeric
@attribute snr_zero_count numeric
@attribute snr_zero_change numeric
@attribute average_speed numeric
@attribute average_satellites numeric
@attribute inside_outside numeric

@data
"""

# 将数据转换为ARFF格式
arff_data = data.to_csv(header=False, index=False)

# 将头部信息和数据合并
arff_content = arff_header + arff_data

# 写入ARFF文件
arff_file = "output.arff"
with open(arff_file, "w") as f:
    f.write(arff_content)

print(f"ARFF文件已保存为 {arff_file}")