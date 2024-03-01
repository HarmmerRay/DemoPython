# 单例模式
class StrTools:
    pass


strTools = StrTools()


# 工厂模式
class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class Factory:
    def get_person(self, person_type):
        if person_type == 'worker':
            return Worker()
        elif person_type == 'teacher':
            return Teacher()
        elif person_type == 'student':
            return Student


factory = Factory()
worker = factory.get_person('worker')
teacher = factory.get_person('teacher')
student = factory.get_person('student')
print(id(worker), id(teacher), id(student))
