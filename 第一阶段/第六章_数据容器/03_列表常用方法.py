name_list = [["Tom", "Lily"], "John", "Smith"]
print(name_list)
# 查询某个元素的下标
index = name_list.index("John")
print(index)
# 修改某个下标处的元素
name_list[1] = "Hammer"
print(name_list)
# 插入元素到列表中
name_list.insert(1, "John")
print(name_list)
# 追加元素到列表
name_list.append("Ben")
print(name_list)
# 追加一批元素到列表
name_list.extend(["Ray", "Brian"])
print(name_list)
# 删除元素
del name_list[0]
print(name_list)
element = name_list.pop(0)
print(f"{name_list}，取出的元素为{element}")
# 删除某元素在列表中的第一个匹配项
name_list.remove("Ben")
print(name_list)
# 清空列表
# name_list.clear()
# print(name_list)
# 统计某元素在列表中出现的次数
count = name_list.count("Brian")
print(f"Brian出现的次数:{count}")
# 统计列表中的元素数量
len = len(name_list)
print(len)
