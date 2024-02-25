# 位置参数
def use_info(name, age, gender):
    print(f"您的名字是{name},age={age},gender={gender}")


use_info("zy", 18, "男")
# 关键字参数
use_info(name="zy", age=18, gender="男")
use_info("zy", age=18, gender="男")


# 缺省参数
def use_info(name, age, gender="男"):
    print(f"您的名字是{name},age={age},gender={gender}")


use_info("zy", 18)


# 不定长参数

# 位置参数
def use_info(*args):
    print(args)


use_info("zy", 18)


# 关键字参数
def use_info(**kwargs):
    print(kwargs)


use_info(name="zy", age=18)
