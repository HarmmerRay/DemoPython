my_str = "hello"
print(my_str[2])
print(my_str[-1])
# 找到字符串的起始下标
print(my_str.index("ll"))
# 字符串转换
new_str = my_str.replace("ll", "kk")
print(new_str)
# 字符串分割
my_str = "hello world! my name is YangZhao"
str_list = my_str.split(" ")
for element in str_list:
    print(element)
for i in range(0, len(str_list)):
    print(str_list[i])
index = 0
while index < len(str_list):
    print(str_list[index])
    index += 1
# 字符串规整操作 去掉前后的空格 或者 指定字符串
my_str = "  hello world! my name is YangZhao.  "
new_str = my_str.strip()
print(new_str)
my_str = "123456hello world! my name is YangZhao.654321"
# my_str = "123456hello world! my name is YangZhao.123456"
new_str = my_str.strip("123456")
print(new_str)
# 统计字符串中某字符串出现的次数
print(my_str.count("hello"))
# 统计字符串的长度
print(len(my_str))

# 练习题
tmp_str = "itheima itcast boxuegu"
print(tmp_str.count("it"))
new_tmp_str = tmp_str.replace(" ","|")
print(new_tmp_str)
list_tmp_str = new_tmp_str.split("|")
for element in list_tmp_str:
    print(element)
