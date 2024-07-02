def modify_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for index, line in enumerate(lines):
            # 移除每个逗号后的空格
            processed_line = line.replace(", ", ",").strip()  # 使用 strip() 移除尾部的换行符
            if index != 0:  # 如果不是第一行
                processed_line += ",0"  # 在行尾添加 ,0
            processed_line += "\n"  # 重新添加换行符
            file.write(processed_line)

# 调用函数
input_filename = 'data-15-gsv.txt'
output_filename = 'data-15-gsv_outside.txt'
modify_file(input_filename, output_filename)