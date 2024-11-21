def calculate_stats(numbers):
    """
    计算列表的最大值、最小值和平均值。

    参数:
    numbers (list of int): 整数列表

    返回:
    tuple: 包含最大值、最小值和平均值的元组
    """
    if not numbers:
        raise ValueError("列表不能为空")

    max_value = max(numbers)
    min_value = min(numbers)
    avg_value = sum(numbers) / len(numbers)

    return max_value, min_value, avg_value


def main():
    # 主程序
    try:
        # 输入列表
        input_string = input("请输入一组整数，用空格分隔: ")
        numbers = list(map(int, input_string.strip().split()))

        # 调用函数计算统计值
        max_value, min_value, avg_value = calculate_stats(numbers)

        # 显示结果
        print(f"最大值: {max_value}")
        print(f"最小值: {min_value}")
        print(f"平均值: {avg_value:.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
