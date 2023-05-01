import math
import random
import sys

# years = input("Number of years: ")
# weeks = int(years) * 52
# print("Weeks in " + str(years)+" years are " + str(weeks)+".")
# print(f"Weeks in {years} years are {weeks}.")

# name = input("Enter your name: ")
# print("Hello " + name + ".\nWellcome to the LearningPython")

# print("Welcome to the group name generator.")
# color = input("What is your favorite color: ")
# animal = input("What is your favorite animal: ")
# print(f"Your group name could be {color} {animal}s")

# hours = input("Enter hours: ")
# rate = input("Enter rate: ")
# pay = round(float(hours)*float(rate),2)
# print(f"Pay: {pay}")

# celsius = input("Enter temperature in celsius: ")
# fahrenheit = int(celsius * 9//5 + 32)
# print(f"{celsius} Celsius is {fahrenheit} Fahrenheit")

# print("Welcome to the Trip Cost Calculator!")
# days = float(input("How many days will you stay? "))
# hotelCost = float(input("How much does hotel cost per night? $"))
# flightCost = float(input("How much does flight cost? $"))
# car = float(input("If you need rental car please enter the price otherwise enter zero. $"))
# expenses = float(input("Enter the possible expenses. $"))

# total = round((days*hotelCost)+flightCost+(days*car)+expenses,2)
# print(f"Total cost: {total}")

# number = int(input("Enter number: "))
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# height = float(input("Enter your height in meters: "))
# weight = float(input("Enter your weight in kg: "))
#
# bmi = round(weight/(height**2.2))
#
# if bmi < 18.5:
#     print(f"{bmi} is Underweight")
# elif bmi < 25:
#     print(f"{bmi} is Normal")
# elif bmi < 30:
#     print(f"{bmi} is Overweight")
# else:
#     print(f"{bmi} is Obese")

# price = 0
# burger = input("What kind of burger do you want?\n Mini == M, Normal == N, Large == L. : ")
# mushroom = input("Do you need add mushrooms? (Y/N) ")
# cheese = input("Do you need add extra cheese? (Y/N) ")
#
# if burger == "M":
#     price = 5
# elif burger == "N":
#     price = 8
# else:
#     price = 10
#
# if mushroom == "Y":
#     if burger == "L":
#         price += 2
#     else:
#         price += 1
#
# if cheese == "Y":
#     price += 1
#
# print(f"Your final bill is: ${price}")

# hours = int(input("Enter hours: "))
# rate = int(input("Enter rate: "))
#
# if hours < 40:
#     pay = round(hours * rate, 2)
# else:
#     overtime = hours - 40
#     pay = round(40 * rate + overtime * rate * 1.5, 2)
#
# print(f"Pay: {pay}")

# year = int(input("Enter year: "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

# name1 = input("Enter your name: ")
# name2 = input("Enter your lover name: ")
#
# combined_name = name1 + name2
# lower_cased_name = combined_name.lower()
#
# t = lower_cased_name.count("t")
# r = lower_cased_name.count("r")
# u = lower_cased_name.count("u")
# e = lower_cased_name.count("e")
#
# true = t + r + u + e
#
# l = lower_cased_name.count("l")
# o = lower_cased_name.count("o")
# v = lower_cased_name.count("v")
# e = lower_cased_name.count("e")
#
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
# print(love_score)
#
# if love_score < 10 or love_score > 85:
#     print(f"Your score is {love_score}, you go together like coke and mentos")
# elif love_score >= 40 and love_score <= 70:
#     print(f"Your score is {love_score}, you alright go together")
# else:
#     print(f"Your score is {love_score}")

# hours = input("Enter hours: ")
# rate = input("Enter rate: ")
#
# try:
#     hours = float(hours)
#     rate = float(rate)
# except ValueError:
#     print("Error, enter integer")
#     quit()
#
#
# if hours < 40:
#     pay = round(hours * rate, 2)
# else:
#     overtime = hours - 40
#     pay = round(40 * rate + overtime * rate * 1.5, 2)
# print(f'Pay: {pay}')

# score = input("Enter score: ")
#
# try:
#     score = float(score)
# except ValueError:
#     print("Bad score.")
#     quit()
#
# if 0.9 <= score <= 1.0:
#     print("A")
# elif 0.8 <= score <= 0.9:
#     print("B")
# elif 0.7 <= score <= 0.8:
#     print("C")
# elif 0.6 <= score <= 0.7:
#     print("D")
# elif score < 0.6:
#     print("F")
# else:
#     print("Bad score.")

# #Try 2
# if score >= 0.0 and score <= 1.0:
#     if score >= 0.9:
#         print("A")
#     elif score >= 0.8:
#         print("B")
#     elif score >= 0.7:
#         print("C")
#     elif score >= 0.6:
#         print("D")
#     else:
#         print("F")
# else:
#     print("Bad score")

# r = int(input("Please, enter radius: "))
#
# area = round(pow(r, 2) * math.pi, 2)
# print(f"The area of circle is: {area}")


# number = int(input("Enter a number: "))
# result = math.factorial(number)
# print(f'The factorial of {number} is: {result}')

# result = random.random()
# result = result * 10
# print(result)

# number = random.random()
#
# print(number)
# if number > 0.5:
#     print("heads")
# else:
#     print("tails")

# def my_first_function():
#     print("This is first function.")
#     print("Bye now.")
#
#
# my_first_function()


# def greet(name):
#     print(f'Hello {name}')
#
#
# my_name = input("What's your name? ")
# greet(my_name)

# def area_of_square(a):
#     area = a * a
#     print(f"Area of square is: {area}")
#
#
# a = int(input("Put the number: "))
# area_of_square(a)

# 1 fluid ounce is equal to 29.57353 milliliters.

# def volume_converter(ounce):
#     milliliters = ounce * 29.57353
#     print(f'{ounce} ounce is {milliliters} milliliters.')
#
#
# volume_converter(5)


# 1 can of paint can cover 4 square meters

# def number_of_cans(height, width, coverage):
#     area = height * width
#     cans = math.ceil(area/coverage)
#     print(cans)
#
#
# height = int(input("Enter wall height: "))
# width = int(input("Enter wall width: "))
# number_of_cans(height, width, 4)


# def concatenate(word1, word2):
#     return f'{word1}{word2}'
#
#
# output = concatenate("face", "book")
# print(output)


# def password_controller(password):
#     if len(password) < 8:
#         return f'Password should be longer than 8 letters'
#     return f"Good password"


# word = str(input("Enter your password: "))
# output = password_controller(word)
# print(output)

#
# def calculator(num1, num2, option):
#     if option == "*":
#         mult = num1 * num2
#         print(f'{num1} {option} {num2} = {mult}')
#     elif option == "-":
#         minus = num1 - num2
#         print(f'{num1} {option} {num2} = {minus}')
#     elif option == "+":
#         plus = num1 + num2
#         print(f'{num1} {option} {num2} = {plus}')
#     elif option == "/":
#         div = num1 / num2
#         print(f'{num1} {option} {num2} = {div}')
#     else:
#         print("You had to enter either of those: +, -, *, /")
#
#
# num1 = int(input("What is the first number? "))
# num2 = int(input("What is the second number? "))
# option = str(input("Pick operation from this list (+,-,*,/): "))
# calculator(num1, num2, option)

# def temperature(temp):
#     if temp < 18:
#         return 'Cold'
#     elif 18 <= temp <= 28:
#         return 'Warm'
#     else:
#         return 'Hot'
#
#
# temp = int(input("Enter current temperature: "))
# print(temperature(temp))


# def max_of_two(a, b):
#     if a > b:
#         return a
#     return b
#
#
# def max_of_three(a, b, c):
#     max_two = max_of_two(a, b)
#     max_of_three = max_of_two(max_two, c)
#     return max_of_three
#
#
# print(max_of_three(1, 2, 3))

# vegetables = ["Brocolli", "Tomato", "Cucumber"]
#
# for vegetable in vegetables:
#     print(vegetable + " pie")


# student_scores = [80, 60, 50, 65, 75, 55]
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print( highest_score)


# custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']
# for item in custom_list:
#     if isinstance(item, int):
#         print(item)


# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# current_value = 0
# for number in range(1, 101, 2):
#     current_value += number
# print(current_value)
#

# username = ""
# while username != "test":
#     username = input("Enter username: ")

# list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
#
#
# def numbers_divisible_byFive(list):
#     print("hi")
#
#
# numbers_divisible_byFive(list1)


# def numbers_divisible_by_five(list_of_numbers):
#     for number in list_of_numbers:
#         if number % 5 == 0:
#             print(number)
#         if number > 130:
#             print("STOP")
#             break
#
#
# list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
# numbers_divisible_by_five(list1)


# def factorial(p_num):
#     fact = 1
#     if p_num < 0:
#         print("Factorial does not exist for negative numbers.")
#     elif p_num == 0:
#         print("Not for 0.")
#     else:
#         for num in range(1, p_num + 1):
#             fact = fact * num
#         return print(f'The factorial of {p_num} is {fact}')
#
#
# print(factorial(0))

# def calculate_average():
#     count = 0
#     total = 0
#     while True:
#         user_input = input("Enter a number or 'done' to exit: ")
#         if user_input == "done":
#             break
#         try:
#             number = float(user_input)
#         except ValueError:
#             print("Invalid input, please enter a number or 'done'.")
#             continue
#         count += 1
#         total += number
#     if count == 0:
#         print("No numbers were entered.")
#     else:
#         average = total / count
#         print("Total:", total)
#         print("Count:", count)
#         print("Average:", average)
#
#
# calculate_average()


# def check_for_float(p_input):
#     try:
#         val = float(p_input)
#         return val
#     except (ValueError, TypeError):
#         print("Error, please enter numeric input")
#         return False


# def roll_dice():
#     dice1 = random.randrange(1, 6)
#     dice2 = random.randrange(1, 6)
#     print(f"Dice 1: {dice1}")
#     print(f"Dice 2: {dice2}")
#
#
# roll_dice()
# answer = input("Roll the dice again Y/N ")
# while answer == "Y":
#     roll_dice()
#     answer = input("Roll the dice again Y/N ")

# def FizzBuzz(a, b):
#     for i in range(1, 101):
#         if i % a == 0 and i % b == 0:
#             print("FizzBuzz")
#         elif i % a == 0:
#             print("Fizz")
#         elif i % b == 0:
#             print("Buzz")
#         else:
#             print(i)
#
#
# a = int(input("Enter first dividable number: "))
# b = int(input("Enter second dividable number: "))
# FizzBuzz(a, b)


# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums = "1234567890"
# symbols = "-+=!@#$%^&*"
#
# letters_count = int(input("How many letters do you want in your password? "))
# nums_count = int(input("How many numbers do you want in your password? "))
# symbols_count = int(input("How many symbols do you want in your password? "))
#
# password = ""
#
# for char in range(1, letters_count + 1):
#     password += random.choice(letters)
#
# for num in range(1, nums_count + 1):
#     password += random.choice(nums)
#
# for symbol in range(1, symbols_count + 1):
#     password += random.choice(symbols)
#
# print(f"Your password is: {password}")
#
# # more advances
# password_list = list(password)
# random.shuffle(password_list)
# password = ""
# for p in password_list:
#     password += p
#
# print(f"Your advanced password is: {password}")

# number = input("Enter the number: ")
#
# sum_digit = 0
# for num in number:
#     sum_digit += int(num)
#
# print(sum_digit)

# def count_letter(word, letter):
#     counter = 0
#     for char in word:
#         if char == letter:
#             counter += 1
#     return counter
#
#
# print(count_letter("Something simple", "i"))

# count_letter("Learning LearningPython", "n")

# custom_string = 'I love LearningPython.'
#
# print(custom_string.replace(".", "!"))

# def generate_dictionary(n):
#     my_dict = dict()
#     for num in range(1, n+1):
#         my_dict[num] = num * num
#     return my_dict
#
#
# output = generate_dictionary(5)
# print(output)


# student_scores = {
#   "John": 90,
#   "Edy": 68,
#   "Marry": 88,
#   "Ewan": 79,
#   "Park": 62,
# }
#
#
# def convert_grade(p_dict):
#     student_grades = {}
#     for key in p_dict:
#         score = p_dict[key]
#         if score >= 85:
#             student_grades[key] = "Outstanding"
#         elif score >= 65:
#             student_grades[key] = "Good"
#         elif score >= 50:
#             student_grades[key] = "Acceptable"
#         else:
#             student_grades[key] = "Failed"
#     return student_grades
#
#
# print(convert_grade(student_scores))


# my_dict = {
#     "name": "Edy",
#     "age":30,
#     "salary": 5000,
#     "city": "London"
# }
#
# my_dict["address"] = my_dict.pop("city")
# print(my_dict)


# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self._balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"{amount} is deposited in {self.name}'s bank account.")
#             print(f"Balance is ${self.balance}")
#         else:
#             print(f"Balance is ${self.balance}")
#
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self._balance -= amount
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

#
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


# class Person:
#     def __init__(self):
#         self.phone_number = 9594
#
#     def update_contact(self, new_number):
#         self.phone_number = new_number
#         print(f"Phone number has been updated to {self.phone_number}")
#
#
# class Customer(Person):
#     def __init__(self):
#         super().__init__()
#
#     def purchase(self, item):
#         print(f"{item} has been purchased.")
#
#
# new_person = Person()
# print(new_person.phone_number)
# new_person.update_contact(389298439823489)
# new_person = Customer()
# new_person.purchase("Coffee")


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
#         super().__init__(name=name, phone_number="0", address="0", salary = "0")
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

# for n in range(3):
#     if n <= 0:
#         adjective = "not enough"
#     elif n == 1:
#         adjective = "just enough"
#     else:
#        adjective = "more than enough"
#     print(f"You have {adjective} items ({n})")

# s = "some string"
# if s != "":                 # Comparing two strings
#     print('s != ""')

