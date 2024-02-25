tuple1 = ("John", 1, "Smith", "Halt")
tuple2 = ()
tuple()
# 定义单个元组
tuple3 = ("John",)
# 嵌套元组
tuple4 = ((1, 2, 3), (4, 5, 6))
# 下标索引
print(tuple4[1][1])
# index()方法通过元素找下标
print(tuple1.index(1))
# count()统计某个元素的个数
print(tuple1.count(1))
# len()统计元组长度
print(len(tuple1))
# while
index1 = 0
while index1 < len(tuple1):
    print(tuple1[index1])
    index1 += 1
# for
for i in range(0, len(tuple1)):
    print(tuple1[i])
for element in tuple1:
    print(element)
# 元组内容不可修改，元组里面嵌套的list可以修改
new_tuple = ("John", ["Raymond", "Smith", "Halt"])
print(new_tuple)
# new_tuple[0] = "Hammer"
new_tuple[1][0] = "Hammer"
print(new_tuple)
# 练习题
pra_tuple = ("周杰伦", 11, ["football", "music"])
print(f"年龄index{pra_tuple.index(11)}")
print(f"姓名{pra_tuple[0]}")
# pra_tuple[2].remove("football")
# del pra_tuple[2][0]
# pra_tuple[2].pop(0)
print(pra_tuple)

pra_tuple[2].append("coding")
print(pra_tuple[2])

