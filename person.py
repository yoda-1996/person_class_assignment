class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and my gender is {self.gender}.")


person_instance = Person("Owen", 26, "male")

person_instance.introduce()
