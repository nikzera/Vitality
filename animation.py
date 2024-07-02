import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 文件路径
file_path = 'data-29-gsv.txt'

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

# 准备动画
fig, ax = plt.subplots(figsize=(14, 10))


def update(frame):
    ts, coordinates = frame
    ax.clear()
    if len(coordinates["x"]) > 0:
        sizes = [snr * 10 for snr in coordinates["snr"]]
        scatter = ax.scatter(coordinates["x"], coordinates["y"], s=sizes, label=f'TS: {ts}')
        ax.set_title(f'Scatter Plot for TS {ts} with SNR-based Sizes')
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.legend()
        ax.grid(True)
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)

        for i, txt in enumerate(coordinates["snr"]):
            ax.text(coordinates["x"][i], coordinates["y"][i], f'{txt}', fontsize=8, ha='right')
    else:
        print(f"No valid data points found for TS {ts}")


ani = FuncAnimation(fig, update, frames=data.items(), repeat=False)

# 保存动画
ani.save('scatter_animation.mp4', writer='ffmpeg', fps=1)

plt.show()