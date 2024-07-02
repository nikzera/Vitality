# 打开文件并读取内容
with open('ARN-20240611-gsv-labeled.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 替换内容
content = content.replace('enter', 'inside')
content = content.replace('leave', 'outside')

# 将修改后的内容写回文件
with open('ARN-20240611-gsv-labeled.txt', 'w', encoding='utf-8') as file:
    file.write(content)

print("替换完成！")