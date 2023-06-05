from turtle import Turtle, Screen


# my_turtle = Turtle()
# print(my_turtle)
# my_turtle.shape("turtle")
#
# my_screen = Screen()
# print(my_screen.canvwidth)
# my_screen.exitonclick()
#


# class StarCookie:
#     def __init__(self, color, weight):
#         self.color = color
#         self.weight = weight
#
#
# star_cookie = StarCookie("red", 10)
# print(star_cookie.color)
# print(star_cookie.weight)

#
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} is deposited in {self.name}'s bank account.")
#             print(f"Balance is ${self.balance}")
#         else:
#             print(f"Balance is ${self.balance}")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} is withdrawn from {self.name}'s bank account ")
#
#     def show_balance(self):
#         print(f"Current balance {self.balance}")
#
#
# user = BankAccount(name="Becca", balance=0)
# user.deposit(10000)
# user.withdraw(100)
# user.show_balance()


# class Customer:
#     def __init__(self, name, balance, number):
#         self.name = name
#         self.__balance = balance
#         self._number = number
#
#     def display_details(self):
#         print(f"{self.name}'s contact details: {self._number}")
#
#     def display_balance(self):
#         print(f"{self.name}'s  balance is: {self.__balance}")
#
#
# customer = Customer("John", 3335, 3239423942)
# print(customer._number)
# customer.display_details()
# customer.display_balance()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, new_salary):
#         self.__salary = new_salary
#
#     salary = property(get_salary, set_salary)
#
#
# employee1 = Employee("Becca", 899)
# employee2 = Employee("Peter", 1299)
# print(employee1.name)
# print(employee1.salary)
# employee1.salary = 1290
# print(employee1.salary)

#
# class Person:
#     def __init__(self, name, phone_number, address, salary):
#         self.name = name
#         self.phone_number = phone_number
#         self.address = address
#         self.email = ""
#         self.salary = salary
#
#     def update_contact(self, phone_number, address):
#         self.phone_number = phone_number
#         self.address = address
#         print(f"Phone number has been updated to {self.phone_number} and {self.address}")
#
#     def get_pay(self):
#         return self.salary
#
#
# class Employee(Person):
#     def __init__(self, name, employee_number):
#         super().__init__(name=name, phone_number="0", address="0", salary="0")
#         self.employee_number = employee_number
#
#     def promote(self):
#         print(f"{self.name} has been promoted!")
#
#     def retire(self):
#         print(f"{self.name} has been retired!")
#
#
# class Currier(Person):
#     def __init__(self, name, salary):
#         super().__init__(name=name, phone_number="0", address="0", salary=salary)
#         self.sales_bonus = 0
#
#     def deliver_packages(self, package):
#         print(f"{self.name} delivered {package}")
#
#     def calculate_bonus(self, items):
#         self.sales_bonus = 2 * items
#
#     def get_pay(self):
#         return self.salary + self.sales_bonus
#
#
# new_employee = Employee("Becca", "111")
# new_employee.promote()
# new_employee.update_contact("943232", "There")
#
# new_currier = Currier("Andrew", 1000)
# new_currier.deliver_packages(10)
# new_currier.calculate_bonus(200)
# print(new_currier.get_pay())



class Shape:
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side*2


new_square = Square(4)
print(new_square.calculate_area())
