import random

num = random.randint(1, 10)
tmp = int(input("请输入一个数字: "))
if tmp == num:
    print("恭喜您第一次猜对了")
else:
    if tmp < num:
        print("猜小了，请再猜一次：")
    else:
        print("猜大了，请再猜一次：")
    tmp = int(input())
    if tmp == num:
        print("恭喜您第二次猜对了")
    else:
        if tmp < num:
            print("猜小了，请再猜一次：")
        else:
            print("猜大了，请再猜一次：")
        tmp = int(input())
        if tmp == num:
            print("恭喜你最后一次猜对了")
        else:
            print("您的三次机会已经用尽，输掉了游戏")


