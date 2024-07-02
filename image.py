import matplotlib.pyplot as plt
import imageio

# 文件路径
file_path = 'data-all-gsv.txt'

# 使用字典存储每个ts的x、y坐标和snr值
data = {}

# 读取文件并根据ts分组存储x、y的值和snr
with open(file_path, 'r') as file:
    next(file)  # 跳过标题行
    for line in file:
        parts = line.strip().split(',')
        try:
            if len(parts) > 6:
                ts = parts[0]
                x = int(parts[5])
                y = int(parts[6])
                snr = int(parts[4])
                if ts not in data:
                    data[ts] = {"x": [], "y": [], "snr": []}
                data[ts]["x"].append(x)
                data[ts]["y"].append(y)
                data[ts]["snr"].append(snr)
        except ValueError:
            print(f"Skipping invalid line: {line.strip()}")

# 初始化文件名列表
filenames = []

# 为每个ts绘制散点图，点的大小和颜色根据snr来确定
for ts, coordinates in data.items():
    if len(coordinates["x"]) > 0:  # 检查是否有有效的数据点
        plt.figure(figsize=(14, 10))
        colors = []
        sizes = []
        for snr in coordinates["snr"]:
            sizes.append(snr * 10)  # 点的大小
            if snr < 10:
                colors.append('red')  # SNR小于10
            elif 10 <= snr <= 20:
                colors.append('yellow')  # SNR在10到20之间
            else:
                colors.append('green')  # SNR大于20

        scatter = plt.scatter(coordinates["x"], coordinates["y"], s=sizes, c=colors, label=f'TS: {ts}')
        plt.title(f'Scatter Plot for TS {ts} with SNR-based Sizes and Colors')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.legend()
        plt.grid(True)
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)

        # 在每个点旁边添加snr值
        for i, txt in enumerate(coordinates["snr"]):
            plt.text(coordinates["x"][i], coordinates["y"][i], f'{txt}', fontsize=8, ha='right')

        # 生成并保存图像文件名
        filename = f"scatter_plot_ts_{ts}.png"
        plt.savefig(filename)  # 指定文件名和格式
        plt.close()  # 关闭图形，以便释放内存

        # 将文件名添加到列表中
        filenames.append(filename)
    else:
        print(f"No valid data points found for TS {ts}")

# 创建一个写入器，设置输出GIF的路径和帧之间的时间间隔
with imageio.get_writer('my_animation.gif', mode = 'I', duration=10) as writer:  # 将duration调整为更合适的值
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

print("GIF animation has been created.")