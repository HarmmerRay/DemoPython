def gcd(a, b):
    """
    使用欧几里得算法计算两个数的最大公因数。

    参数:
    a (int): 第一个整数
    b (int): 第二个整数

    返回:
    int: 最大公因数
    """
    while b != 0:
        a, b = b, a % b
    return a


def main():
    # 主程序
    try:
        # 输入两个整数
        num1 = int(input("请输入第一个整数: "))
        num2 = int(input("请输入第二个整数: "))

        # 调用函数计算最大公因数
        result = gcd(num1, num2)

        # 输出结果
        print(f"{num1} 和 {num2} 的最大公因数是: {result}")
    except ValueError:
        print("输入错误，请确保输入的是整数。")


if __name__ == "__main__":
    main()
