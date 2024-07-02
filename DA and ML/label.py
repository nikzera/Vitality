import pandas as pd

# 读取事件文件并解析时间戳和状态
events_file = "ARN-20240625-events.txt"
events = []

with open(events_file, "r") as f:
    for line in f:
        if line.startswith("//") or line.strip() == "":
            continue
        parts = line.strip().split()
        if len(parts) == 2:
            current_status = parts[0]
        elif len(parts) == 3:
            timestamp, status = parts[0], parts[2][1:-1]
            events.append((int(timestamp), status))

# 读取gsv文件数据
gsv_file = "ARN-20240625-gsv.txt"
gsv_data = pd.read_csv(gsv_file)

# 将时间戳转换为整数
gsv_data['ts'] = gsv_data['ts'].astype(int)

# 添加新列用于标注状态和enter/leave情况
gsv_data['status'] = 'unknown'
gsv_data['enter_leave'] = -1

# 添加根据事件标注的状态值
def get_enter_leave_value(status):
    if status == 'enter':
        return 1
    elif status == 'leave':
        return 0
    return -1

# 根据事件标注状态
for i in range(len(events) - 1):
    start_time, status = events[i]
    end_time = events[i + 1][0]
    gsv_data.loc[(gsv_data['ts'] >= start_time) & (gsv_data['ts'] < end_time), 'status'] = status
    gsv_data.loc[(gsv_data['ts'] >= start_time) & (gsv_data['ts'] < end_time), 'enter_leave'] = get_enter_leave_value(status)

# 处理最后一个事件的状态
if events:
    last_time, last_status = events[-1]
    gsv_data.loc[gsv_data['ts'] >= last_time, 'status'] = last_status
    gsv_data.loc[gsv_data['ts'] >= last_time, 'enter_leave'] = get_enter_leave_value(last_status)

# 保存标注后的数据到新文件
output_file = "ARN-20240625-gsv-labeled.txt"
gsv_data.to_csv(output_file, sep=',', index=False)

print(f"标注后的数据已保存到 {output_file}")