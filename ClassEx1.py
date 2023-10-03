class Person():
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def greeting(self):
        print("name: ",self.name)
        print("age: ", self.age)

Jack= Person("Jack",22)
print(Jack.greeting())
