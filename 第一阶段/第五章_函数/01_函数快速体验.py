str1 = "hello"
str2 = "itheima"


def my_len(str):
    count = 0
    for i in str:
        count += 1
    print(f"{str}长度：{count}")
    

my_len(str1)
my_len(str2)
