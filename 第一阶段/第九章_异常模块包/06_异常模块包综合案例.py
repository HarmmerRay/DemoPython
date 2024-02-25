from my_utils import *

my_str = "Hello World!\n"
print(str_util.str_reverse(my_str))
print(str_util.str_sub(my_str, 1, 4))

file_util.append_file("abc.txt", my_str)
file_util.read_file("abc.txt")
