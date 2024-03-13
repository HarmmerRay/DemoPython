def hanoi(n):
    if n == 1:
        return 1
    else:
        return hanoi(n - 1) * 2 + 1


if __name__ == '__main__':
    print(hanoi(3))
