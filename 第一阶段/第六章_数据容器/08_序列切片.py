# list
my_list = [1, 2, 3, 4, 5, 6, 7]
result = my_list[0:4:2]
for element in result:
    print(element)
# tuple
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = my_tuple[::-2]
print(result)
# str
my_str = "hello Python!"
result = my_str[::2]
print(result)
# 练习题
tmp_str = "万过薪月，员序程马黑"
# result = tmp_str[::-1][0:5:]
result = tmp_str.split("，")[1][::-1]
print(result)
