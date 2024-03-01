# account_num = 0
# def atm(num, deposit=True):
#     global account_num
#     if deposit:
#         account_num += num
#         print(f"存款:+{num},账户余额:{account_num}")
#     else:
#         account_num -= num
#         print(f"存款:+{num},账户余额:{account_num}")
#
#
# atm(300)
# atm(300)
# atm(300, False)


# 以上方法全局变量有风险 可以被别人篡改  代码在变量定义上不够优雅 干净 整洁
# 以下 就是 闭包 解决上述两个问题
def account_create(account_num=0):
    def atm(num, deposit=True):
        nonlocal account_num
        if deposit:
            account_num += num
            print(f"存款:+{num},账户余额:{account_num}")
        else:
            account_num -= num
            print(f"取款:-{num},账户余额:{account_num}")

    return atm


atm = account_create()
atm(300)
atm(300)
atm(300, False)


# def outer(logo):
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#
#     return inner
#
#
# fn1 = outer("迈思低代码")
# fn1("欢迎大家")
# fn1("低代码平台就来")

def outer(num1):
    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner


fn1 = outer(10)
fn1(10)
fn1(10)
fn1(10)
