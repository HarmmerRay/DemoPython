import random

i = 1
j = 0
while i <= 100:
    j = j + i
    i += 1

print("从1累加到100的和:%d" % j)
print(f"从1累加到100的和:{j}")

num = random.randint(1, 10)
i = 0
print("欢迎来到猜数字游戏，你一共有5次机会")
while i < 5:
    tmp = int(input("请输入你猜的数字:"))
    if tmp == num:
        print("恭喜你猜中啦！")
        break
    elif tmp > num:
        print("你猜的数字大了!还有机会：")
    else:
        print("你猜的数字小了!还有机会：")
    i += 1

print("**************************************************")

num1 = random.randint(1, 100)
flag = True
count = 0
print("欢迎来到猜数字游戏（[1,100]的整数），你有无限次的机会，看看谁用的次数最少吧！")
while flag:
    tmp = int(input("请输入你猜的数字:"))
    if tmp == num:
        print("恭喜你猜中啦！")
        flag = False
    elif tmp > num:
        print("你猜的数字大了!还有机会：")
    else:
        print("你猜的数字小了!还有机会：")
    count += 1
print(f"你一共猜了{count}次")
