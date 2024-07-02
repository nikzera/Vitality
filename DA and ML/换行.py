import csv

# 输入和输出文件名
input_filename = 'ARN-20240625.txt'
output_filename = 'ARN-20240625_reordered.txt'

with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 读取标题行
    header = next(reader)

    # 计算 inside_outside 列的索引
    inside_outside_index = header.index('inside_outside')

    # 移动 inside_outside 列到最右边
    new_header = header[:inside_outside_index] + header[inside_outside_index + 1:] + ['inside_outside']

    # 写入新的标题行
    writer.writerow(new_header)

    # 处理数据行
    for row in reader:
        # 获取 inside_outside 列的值
        inside_outside_value = row[inside_outside_index]

        # 重新排列该行数据，把 inside_outside 列移动到最右边
        new_row = row[:inside_outside_index] + row[inside_outside_index + 1:] + [inside_outside_value]

        # 写入重新排列后的数据行
        writer.writerow(new_row)

print(f"Data has been reordered and saved to {output_filename}")