
with open('balance', 'r') as f:
    balance = float(f.read())

username = None

def login():
    name = input("请输入你的账号:")
    password = input("请输入你的密码:")
    if name == 'admin' and password == 'admin':
        global username
        username = name
        print("登录成功")
        return True
    print("登录失败")
    return False


def main_menu():
    print("$$$$$$$$$主菜单$$$$$$$$$$$")
    print(f"{username}您好，欢迎使用锤子ATM系统，请选择操作:")
    print("查询余额 [输入1]")
    print("存款 [输入2]")
    print("取钱 [输入3]")
    print("退出系统 [输入4]")
    flag = int(input())
    if flag == 1:
        check_balance()
        return True
    elif flag == 2:
        money = float(input("存款------请输入您要存款金额:"))
        deposit(money)
        return True
    elif flag == 3:
        money = float(input("取款------请输入您要取款金额:"))
        withdraw(money)
        return True
    elif flag == 4:
        return None
    print("请选择有效的操作序号")
    main_menu()
    return True


def check_balance():
    print(f"尊敬的{username}用户，您的余额为{balance}")


def deposit(money):
    global balance
    balance += money
    with open("balance", "w") as f:
        f.write(str(balance))
    print(f"尊敬的{username}用户，您成功存入{money}元，现在账户中剩余{balance}元")


def withdraw(money):
    global balance
    balance -= money
    with open("balance", "w") as f:
        f.write(str(balance))
    print(f"尊敬的{username}用户，您成功取出{money}元，现在账户中剩余{balance}元")


print("欢迎来到锤子ATM系统")
flag = login()
while not flag:
    flag = login()
flag = main_menu()
while flag:
    flag = main_menu()
print("欢迎下次使用锤子ATM系统，祝您生活愉快")
