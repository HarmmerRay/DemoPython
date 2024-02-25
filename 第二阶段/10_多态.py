class Animal:
    voice = "###"

    def speak(self):
        print(f"{self.voice}")


class Dog(Animal):
    voice = "旺旺旺"


class Cat(Animal):
    voice = "喵喵喵"


def make_voice(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
dog.speak()
cat.speak()
