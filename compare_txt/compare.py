import difflib

def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()

        # 使用difflib进行比较
        diff = difflib.unified_diff(file1_lines, file2_lines, fromfile='file1', tofile='file2', lineterm='')

        print("以下是两个文件的不同之处（统一差异格式）:")
        for line in diff:
            print(line)

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

# 使用示例
file1_path = 'not_include_0.txt'
file2_path = 'include_0.txt'
compare_files(file1_path, file2_path)