num = 100

def say_a():
    print(num)

def say_b():
    global num
    num = 500
    print(num)

say_a()
say_b()
print(num)