# # 装饰器一般写法闭包
# def sleep():
#     import random
#     import time
#     print("睡眠中>>>>>>>>>>>>>>")
#     time.sleep(random.randint(1, 5))
#
#
# def outer():
#     def inner():
#         print("我睡觉了")
#         sleep()
#         print("我起床了")
#
#     return inner
#
#
# sl = outer()
# sl()

# 语法糖写法

def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner


@outer
def sleep():
    import random
    import time
    print("睡眠中>>>>>>>>>>>>>>")
    time.sleep(random.randint(1, 5))


sleep()
