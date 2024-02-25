# while
index = 0
students_age = [21, 25, 21, 23, 22, 20]
while index < len(students_age):
    print(students_age[index])
    index += 1
# for
print("###########################")
for i in range(0, len(students_age)):
    print(students_age[i])
print("###########################")
for element in students_age:
    print(element)

# 练习题
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
index = 0
while index < len(list1):
    if list1[index] % 2 == 0:
        even_list.append(list1[index])
    index += 1

print(f"{list1}构成的偶数列表为{even_list}")