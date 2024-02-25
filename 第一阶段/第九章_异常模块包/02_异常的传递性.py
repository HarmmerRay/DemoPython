def func1():
    print("func1_BEGIN")
    1 / 0  # 除零异常
    print("func1_END")


def func2():
    print("func2_BEGIN")
    func1()
    print("func2_END")


if __name__ == '__main__':
    # try:
    #     func2()
    # except ZeroDivisionError:
    #     print("发现除零异常")
    func2()