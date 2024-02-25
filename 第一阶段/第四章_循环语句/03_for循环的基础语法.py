import sys

var = "hello"
for x in var:
    print(x)

var1 = "itheima is a brand of itcast"
count = 0
for x in var1:
    if x == 'a':
        count += 1
    sys.stdout.write(x)
print()
print(f"var1中共有{count}个字母'a'")
