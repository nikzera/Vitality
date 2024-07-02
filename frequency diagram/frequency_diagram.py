import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
filename = "ARN-20240611-gsv_including_null.txt"
data = pd.read_csv(filename)

# 定义一个函数来转换时间戳
def convert_to_seconds(ts):
    hours = ts // 10000
    minutes = (ts % 10000) // 100
    seconds = ts % 100
    return hours * 3600 + minutes * 60 + seconds

# 应用转换函数
data['ts_seconds'] = data['ts'].apply(convert_to_seconds)

# 筛选每隔五秒的数据点
filtered_data = data[data['ts_seconds'] % 5 == 0]

# 获取所有的卫星id
satellite_ids = filtered_data['id'].unique()

# 绘图
plt.figure(figsize=(20, 12))  # 设置更大的图片尺寸

# 为每个卫星ID画图
for sat_id in satellite_ids:
    sat_data = filtered_data[filtered_data['id'] == sat_id]
    plt.plot(sat_data['ts_seconds'], sat_data['snr'], label=f'Satellite {sat_id}')

# 确保 y 轴标出 0 点
plt.ylim(bottom=0)

# 添加图例
plt.legend()

# 添加标题和标签
plt.title('Satellite SNR over Time (All Satellites, Every 5 Seconds)')
plt.xlabel('Time (seconds)')
plt.ylabel('SNR')

# 展示图表
plt.show()