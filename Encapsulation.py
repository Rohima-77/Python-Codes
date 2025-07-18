There are three types of encapsulation:
1.private
2.protected
3.public

# Private encapsulation:

class BankAccount:
    def __init__(self, name, balance):
        self.__name = name       # Private attribute (__ দিয়ে)
        self.__balance = balance # Private attribute
    
    # Private method
    def __show_balance(self):
        print(f"Current balance: {self.__balance}")

account = BankAccount("Rahim", 5000)
print(account.__name)  # Error: AttributeError (বাইরে থেকে এক্সেস করা যাবে না)
account.__show_balance() # Error: AttributeError


# protected Encapsulation:

class Person:
    def __init__(self, name, age):
        self._name = name    # Protected attribute (_ দিয়ে)
        self._age = age      # Protected attribute

class Student(Person):
    def show_details(self):
        print(f"Name: {self._name}, Age: {self._age}")  # চাইল্ড ক্লাসে এক্সেস করা যায়

s = Student("Karim", 20)
s.show_details()  # Output: Name: Karim, Age: 20
print(s._name)    # কাজ করবে, কিন্তু convention অনুযায়ী এড়িয়ে যাওয়া উচিত


# public Encapsulation:
class Car:
    def __init__(self, model, color):
        self.model = model  # Public attribute
        self.color = color  # Public attribute
    
    def display(self):      # Public method
        print(f"{self.model} - {self.color}")

my_car = Car("Toyota", "Red")
my_car.display()  # Output: Toyota - Red
print(my_car.color)  # Output: Red
