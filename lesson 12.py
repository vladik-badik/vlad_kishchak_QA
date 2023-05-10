class Human:

    def __init__(self,name, age):
        print("in human cusruction")
        self.name = name
        self.age =age

    def introduce(self):
        print(f" i'm {self.name} of {self.age} years")

class Employee(Human):
    pass

human = Human('John',34)
employee =  Employee("anna",30)
employee.introduce()
human.introduce()