class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print("Student类创建了一个类对象")

    def __str__(self):
        return f"姓名:{self.name},性别:{self.gender},年龄:{self.age}"

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age


stu = Student("赵资源", "男", 18)
stu1 = Student("赵正", "男", 18)
print(stu.__lt__(stu1))
print(stu <= stu1)
print(stu >= stu1)
print(stu == stu1)