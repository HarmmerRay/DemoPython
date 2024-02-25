def read_file(file_name):
    try:
        f = open(file_name, 'r')
        print(f.read())
    except FileNotFoundError as e:
        print("文件找不到")
    finally:
        f.close()


def append_file(file_name, content):
    f = open(file_name, 'a', encoding='utf-8')
    f.write(content)
