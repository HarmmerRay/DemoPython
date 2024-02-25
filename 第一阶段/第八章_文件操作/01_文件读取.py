import sys

with open("file.txt", "r", encoding="utf-8") as file:
    for element in file:
        sys.stdout.write(element)

# file = open("file.txt", "r", encoding="utf-8")
# print(type(file))
# 读取文件所有的内容
# var = file.read()
# print(var)
# var = file.read(10)
# print(var)
# var_list = file.readlines()
# for element in var_list:
#     sys.stdout.write(element)
# var = file.readline()
# print(type(var))
# sys.stdout.write(var)
# while var != "" and var != "\n":
#     var = file.readline()
#     print(type(var))
#     sys.stdout.write(var)
# file.close()

# 文件读取练习题
# with open("file.txt", "r", encoding="utf-8") as file:
#     var = file.read()
#     var_list = var.split(" ")
#     count = 0
#     for element in var_list:
#         if element == "是":
#             count += 1
#     print(f"‘是’出现的次数为:{count}")
#     print(f"‘是’出现的次数为:{var.count('是')}")
