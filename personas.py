
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print('Hello, my name is {} and I am {} years old'.format(self.name, self.age))


if __name__ == '__main__':
    Person = Person('David', 22)
    Person.say_hello()