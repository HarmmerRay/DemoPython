my_set = {1, 2, 2, 1}
print(my_set)
# my_set = set()

my_set.add("Ray")
print(my_set)

my_set.remove(1)
print(my_set)
# 随机取出一个元素
print(my_set.pop())

my_set.clear()
print(my_set)
print(type(my_set))

set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
print(f"并集:{set3}")
print(f"交集:{set4}")
print(f"差集:{set5}")

print(len(my_set))

for element in my_set:
    print(element)

# 练习题
my_list = ['Ray', 'Ray', 'Hammer', 'Hammer', 'go', 'go']
print(my_list)
for element in my_list:
    my_set.add(element)

print(my_set)
