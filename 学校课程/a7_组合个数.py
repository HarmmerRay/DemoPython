def count(m: int, n: int) -> float:
    a = 1
    b = 1
    c = 1
    t = m - n
    while m > 0:
        a *= m
        m -= 1
    while n > 0:
        b *= n
        n -= 1

    while t > 0:
        c *= t
        t -= 1
    return a / (b * c)


if __name__ == '__main__':
    print(count(10, 5))
