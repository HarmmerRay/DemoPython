def input_list_row(prompt="请输入列表元素，用空格分隔: "):
    # 行输入，用户在一行内输入所有元素
    return list(map(int, input(prompt).strip().split()))


def input_list_column(n=None, prompt="请输入列表元素，按回车确认每个元素: "):
    # 列输入，用户每次输入一个元素
    lst = []
    i = 0
    while n is None or i < n:
        try:
            element = int(input(prompt))
            lst.append(element)
            i += 1
        except ValueError:
            print("输入错误，请确保输入的是整数。")
            continue
        if n is not None and i >= n:
            break
    return lst


def output_list_row(lst):
    # 行输出，输出所有元素在同一行
    print(" ".join(map(str, lst)))


def output_list_column(lst):
    # 列输出，每个元素各占一行
    for element in lst:
        print(element)


def main():
    # 主程序，用于测试上述函数
    print("行输入示例：")
    row_list = input_list_row()
    print("\n行输出示例：")
    output_list_row(row_list)

    print("\n列输入示例：")
    column_list = input_list_column(n=3)  # 这里假设我们想让用户输入3个元素
    print("\n列输出示例：")
    output_list_column(column_list)


if __name__ == "__main__":
    main()
