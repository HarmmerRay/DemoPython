# def round_division(a, b):
#     r = 0
#     while True:
#         if a > b:
#             r = a % b
#             if r == 0:
#                 return b
#             a = r
#         elif a < b:
#             r = b % a
#             if r == 0:
#                 return a
#             b = r


def gcd(a, b):
    r = 0
    while True:
        if a > b:
            r = a % b
            if r == 0:
                return b
            a = r
        elif a < b:
            r = b % a
            if r == 0:
                return a
            b = r


if __name__ == '__main__':
    print(gcd(22, 520))
