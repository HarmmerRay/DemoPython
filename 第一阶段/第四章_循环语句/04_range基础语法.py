import sys
for x in range(5):
    sys.stdout.write(str(x))
print()
for x in range(2, 5):
    sys.stdout.write(str(x))
print()
for x in range(2, 7, 2):
    sys.stdout.write(str(x))
i = 0
for x in range(1,100):
    if(x % 2 == 0):
        i += 1
print("[1,100]中一共有%d个偶数" % i)

