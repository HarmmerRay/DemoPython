# 任何的道理都要经过实打实的行动实践才能真正对自己有效
# 备份账单
# 1.创建账单
# 周杰伦,2024.2.3,1000,消费,正式
import datetime

#
# file = open("file.txt", "w", encoding="utf-8")
# record = ["周杰伦", "2024-2-3 15:33:38.567596", 1000, "消费", "正式"]
# print(datetime.datetime.now())
# index = 0
# while index < 12:
#     record[1] = str(datetime.datetime.now())
#     file.write(str(record) + "\n")
#     index += 1
# file.flush()
# file.close()

# 2.备份账单
with open("file.txt", "r", encoding="utf-8") as file:
    my_str = file.read()
    print(f"读取到的数据:\n{my_str}")
    my_str_list = my_str.split("\n")
    test_str_list = list()
    for element in my_str_list:
        element_list = element.split(",")
        print(element_list[len(element_list) - 1])
        if element_list[len(element_list) - 1] == " '测试']":
            test_str_list.append(element)
    my_str_list = set(my_str_list).difference(set(test_str_list))

with open("file_backup.txt", "w", encoding="utf-8") as file:
    print(f"需要备份的数据:")
    for element in my_str_list:
        print(element)
        file.write(str(element) + "\n")
    file.flush()
