def judge_prime(num):
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
        i += 1
    return True


def output_prime(start: int, end: int) -> []:
    result = []
    for i in range(start, end + 1):
        if judge_prime(i):
            result.append(i)
    return result


if __name__ == '__main__':
    # val = int(input("输入正整数，系统判断是否为素数\n"))
    # print(judge_prime(val))
    print(output_prime(1, 99))

