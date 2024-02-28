class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def sayHello(self):
        print(f"Hello,我是{self.name}")

stu_1 = Student()

stu_1.name = '周杰伦'
stu_1.gender = '男'
stu_1.nationality = '中国'
stu_1.native_place = '山东省'
stu_1.age = 18
stu_1.sayHello()

print(stu_1.nationality)
