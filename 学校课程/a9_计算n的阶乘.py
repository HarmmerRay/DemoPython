def factorial(n):
    if n == 1:
        return 1
    else:
        n *= factorial(n - 1)
    return n


if __name__ == "__main__":
    print(factorial(9))
