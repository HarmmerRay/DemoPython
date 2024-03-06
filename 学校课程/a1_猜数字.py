import random


def guess_num():
    global guess
    num = int(input("数字是[0,50]之间的整数，请输入你猜的数字，并回车确认！"))
    if num == guess:
        print("棒！你猜对了")
        return True
    elif num > guess:
        print("比这个数小")
        return False
    else:
        print("比这个数大")
        return False


if __name__ == "__main__":
    print("欢迎来到猜数字游戏！")
    guess = random.randint(0, 50)
    times = 0
    while times < 3:
        if guess_num():
            break
        else:
            times += 1
    if times >= 3:
        print(f"这局游戏你输了！正确的数是{guess}")
