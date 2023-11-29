class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "이름은 {}이고, 나이는 {}살입니다.".format(self.name, self.age)

my_dog = Dog("Mango", 3)

print(my_dog)