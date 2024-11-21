def swap_case(s):
    """
    将字符串中的小写字母转换为大写字母，大写字母转换为小写字母。

    参数:
    s (str): 输入字符串

    返回:
    str: 处理后的字符串
    """
    result = []
    for char in s:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)


def main():
    # 主程序
    try:
        # 输入一句话
        input_string = input("请输入一句话: ")

        # 调用函数进行字母大小写互换
        output_string = swap_case(input_string)

        # 输出结果
        print("转换后的结果:", output_string)
    except Exception as e:
        print("发生错误:", e)


if __name__ == "__main__":
    main()
