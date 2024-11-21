def decimal_to_binary(n):
    """
    将十进制整数转换为二进制形式的字符串。

    参数:
    n (int): 十进制整数

    返回:
    str: 二进制形式的字符串
    """
    if n < 0:
        raise ValueError("输入必须是非负整数")

    if n == 0:
        return '0'

    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2

    return binary


def main():
    # 主程序
    try:
        # 输入一个整数
        num = int(input("请输入一个非负整数: "))

        # 调用函数将十进制整数转换为二进制字符串
        binary_string = decimal_to_binary(num)

        # 输出结果
        print(f"{num} 的二进制形式是: {binary_string}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
