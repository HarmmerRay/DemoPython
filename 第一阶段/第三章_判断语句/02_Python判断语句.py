print("欢迎来到黑马程序院\n成人收费，儿童免费\n请输入你的年龄")

age = input()
age = int(age)
print("你的年龄为%d" % age)
# if
if age >= 18:
    print("您已经成年需要收费20元")
    # else
else:
    print("还未成年，免费游玩叭小朋友")
# if elif
height = int(input("请输入你的身高(CM):"))
vip_level = int(input("请输入你的vip等级(1-5):"))
if height > 200:
    print("身高大于200CM,免费游玩")
elif vip_level > 3:
    print("VIP3以上，不包含3，免费游玩")
else:
    if vip_level == 1:
        print("九折游玩,原价100，现价90")
    elif vip_level == 2:
        print("八折游玩,原价100，现价80")
