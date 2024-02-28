class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print("Student类创建了一个类对象")


stu = Student("赵资源", "男", 18)
print(stu.age)
