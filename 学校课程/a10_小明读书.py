def rest_pages(n: int):
    rest_6 = 3
    for i in range(1, (6 - n) + 1):
        rest_6 = (rest_6 + 2) * 2
    return rest_6


def rest_pages_recursion(n: int):
    if n == 6:
        return 3
    else:
        return (rest_pages_recursion(n + 1) + 2) * 2


if __name__ == '__main__':
    print(rest_pages(5))
    print(rest_pages_recursion(5))
