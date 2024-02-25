# 函数作为传参
def compute(x, y):
    return x + y


def test_func(compute):
    result = compute(2, 3)
    print(result)


test_func(compute)
# lambda匿名函数
test_func(lambda x, y: x + y)
