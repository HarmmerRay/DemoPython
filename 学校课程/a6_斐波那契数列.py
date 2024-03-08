import sys


def fibonacci(i):
    c = 0
    a = 1
    b = 1
    if i == 1 % i == 2:
        return 1
    # ranint() 左闭右闭
    for m in range(2, i):
        c = a + b
        a = b
        b = c
        # sys.stdout.write(f"{c}\t")
    return c


if __name__ == '__main__':
    print(fibonacci(20))
    # fibonacci(5)