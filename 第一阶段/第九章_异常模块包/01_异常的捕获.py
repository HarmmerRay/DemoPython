# 捕获宽泛的异常
try:
    file = open("abc.txt", "r", encoding="utf-8")
    1/0
    print(name)
except: #同 except Exception as e:
    print("出现异常了")
    file = open("abc.txt", "w", encoding="utf-8")

# # 捕获指定的异常
# try:
#     file = open("abc.txt", "r", encoding="utf-8")
# except FileNotFoundError as e:
#     print("出现异常了，因为文件不能再，R模式不能用，改为W模式")
#     file = open("abc.txt", "w", encoding="utf-8")

# 捕获多个异常
try:
    1/0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量名错误，除0异常")
else:
    print("没有异常，好开心！")
finally:
    print("finally多用于 关闭资源，比如file.close() 网络的断开连接等等")