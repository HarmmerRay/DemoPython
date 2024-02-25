my_list = [["a", 33], ["b", 44], ["c", 55]]

# def my_sort(element):
#     return element[1]
#
# my_list.sort(key=my_sort, reverse=True)

my_list.sort(key=lambda element: element[1], reverse=True)
for item in my_list:
    print(item)
