import random


def game():
    global money
    money -= 5
    # print(f"当前余额{money}")
    machine = random.randint(1, 3)
    gamer = random.randint(1, 3)
    # 1:剪刀 2:石头 3:布
    if gamer == 1:
        if machine == 1:
            print("Draw！")
            print(f"当前余额{money}")
        else:
            if machine == 2:
                print("Machine Win!")
                money -= 5
                print(f"当前余额{money}")
            else:
                if machine == 3:
                    print("Gamer Win!")
                    money += 10
                    print(f"当前余额{money}")
    else:
        if gamer == 2:
            if machine == 2:
                print("Draw！")
                print(f"当前余额{money}")
            else:
                if machine == 3:
                    print("Machine Win!")
                    money -= 5
                    print(f"当前余额{money}")
                else:
                    if machine == 1:
                        print("Gamer Win!")
                        money += 10
                        print(f"当前余额{money}")
        else:
            if gamer == 3:
                if machine == 3:
                    print("Draw！")
                    print(f"当前余额{money}")
                else:
                    if machine == 1:
                        print("Machine Win!")
                        money -= 5
                        print(f"当前余额{money}")
                    else:
                        if machine == 2:
                            print("Gamer Win!")
                            money += 10
                            print(f"当前余额{money}")


if __name__ == '__main__':
    print("欢迎来到石头剪刀布人机对决!\n您最开始有50个金币,每开始一局游戏，花费5金币。")
    money = 50
    times = 0
    while money > 0:
        times += 1
        print(f"第{times}局")
        game()

