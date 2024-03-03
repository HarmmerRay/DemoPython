import os


def test_os():
    print(os.listdir("E:/test"))
    # print(os.path.isdir(""))
    # print(os.path.exists(""))


file_list = []


def get_files_recursion_from_dir(path):
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + '/' + f
            if os.path.isdir(new_path):
                get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}，不存在")
        return []

    return file_list


if __name__ == '__main__':
    print(get_files_recursion_from_dir("E:/test"))
