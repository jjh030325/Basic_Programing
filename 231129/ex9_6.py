class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_dog = Dog("Mango", 3)

print("my_dog의 이름은 {}이고, 나이는 {}살입니다.".format(my_dog.name, my_dog.age))