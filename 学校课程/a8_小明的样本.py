import random


def sample(n):
    result_set: set = set()

    while n > 0:
        result_set.add(random.randint(1000, 2000))
        n -= 1

    return sorted(list(result_set))


if __name__ == '__main__':
    print(sample(8))
