import math
import random
import sys
import time

# import sys
# from replit import clear

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
#
# available_parts = {
#     "1": "computer",
#     "2": "monitor",
#     "3": "keyboard",
#     "4": "mouse",
#     "5": "hdmi cable",
#     "6": "dvd drive",
# }
#
# price_quantity = {
#     "computer": {"price": 500, "quantity": 10},
#     "monitor": {"price": 200, "quantity": 8},
#     "keyboard": {"price": 500, "quantity": 5},
#     "mouse": {"price": 10, "quantity": 0},
#     "hdmi cable": {"price": 20, "quantity": 7},
#     "dvd drive": {"price": 50, "quantity": 5},
# }
#
# current_choice = None
# total_price = 0
# while current_choice != "0":
#     if current_choice in available_parts:
#         chosen_part = available_parts[current_choice]
#         if price_quantity[chosen_part]["quantity"] > 0:
#             print(f"Adding {chosen_part}")
#             price_quantity[chosen_part]["quantity"] -= 1
#             total_price += price_quantity[chosen_part]["price"]
#         else:
#             print(f"{chosen_part} is out of stock!")
#
#     else:
#         print("Please add options from the list")
#         for key, value in available_parts.items():
#             print(f"{key}: {value}")
#         print("0: to finish")
#
#     current_choice = input("> ")
#
#
# print(f"Total price: {total_price}")
#
# import pyfiglet
#
# print(pyfiglet.figlet_format("BLIND AUCTION"))

# logo = """
# ██████╗ ██╗     ██╗███╗   ██╗██████╗      █████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗
# ██╔══██╗██║     ██║████╗  ██║██╔══██╗    ██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║
# ██████╔╝██║     ██║██╔██╗ ██║██║  ██║    ███████║██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║
# ██╔══██╗██║     ██║██║╚██╗██║██║  ██║    ██╔══██║██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║
# ██████╔╝███████╗██║██║ ╚████║██████╔╝    ██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║
# ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
# """
#
#
# def find_higest_amount(p_bid_record):
#     highest_bid = 0
#     highest_bidder = ""
#     for key, value in p_bid_record.items():
#         if value > highest_bid:
#             highest_bid = value
#             highest_bidder = key
#     print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
#
#
# print(logo)
# bids = {}
# bidding_finished = False
# while not bidding_finished:
#     name = input("What is your name?: ")
#     amount = int(input("What is your bid amount?: $"))
#     bids[name] = amount
#     another = input("Are there any other bidder?(Y/N)")
#     if another == "N":
#         bidding_finished = True
#         find_higest_amount(bids)
#     elif another == "Y":
#         clear()

# my_tuple = (10, 40, 80, 90)
#
# result = my_tuple[0]+my_tuple[1]+my_tuple[2]+my_tuple[3]
# a, b, c, d = my_tuple
#
# print(result)
# print(f"{a+b+c+d}")

# def even_index_items(my_tuple):
#     result_list = []
#     for index, value in enumerate(my_tuple):
#         if index % 2 == 0:
#             result_list.append(value)
#     result_tuple = tuple(result_list)
#     return result_tuple
#
#
# my_tuple = ("a", "b", "c", "d", "e", "f", "g")
# print(even_index_items(my_tuple))


# my_tuple = (1, 2, 3, 4, 5, 6, 7)
#
#
# def search_tuple(p_tuple, p_item):
#     for index, value in enumerate(p_tuple):
#         if value == p_item:
#             return index
#     return "Item does not exist"
#
#
# print(search_tuple(my_tuple, 5))


# def most_frequent(p_tuple):
#     max_count = 0
#     item = p_tuple[0]
#     for value in p_tuple:
#         current_item_count = p_tuple.count(value)
#         if current_item_count > max_count:
#             max_count = current_item_count
#             item = value
#     return item, max_count
#
#
# my_tuple = ("a", "b", "c", "d", "e", "a", "c", "e", "b", "e", "c", "a", "f", "e", "r")
# print(most_frequent(my_tuple))


# clubs = (("FC Barcelona", "Spain", 1899,
#             [
#                 (3, "Pique"),
#                 (5, "Busquets"),
#                 (7, "Dembele"),
#             ]
#          ),
#          ("Real Madrid CF", "Spain", 1902,
#             [
#                 (7, "Hazard"),
#                 (9, "Benzema"),
#                 (10, "Modric"),
#             ]
#          ),
#          ("Manchester United FC", "England", 1878,
#             [
#                 (6, "Pogba"),
#                 (7, "Ronaldo"),
#                 (14, "Lingard"),
#             ]
#          ),
#          ("Arsenal FC", "England", 1886,
#             [
#                 (7, "Lacazette"),
#                 (14, "Aubameyang"),
#                 (16, "Holding"),
#             ]
#          ),
#          )
#
#
# Lacazette = clubs[3][3][0][1]
# print(Lacazette)
# year = clubs[2][2]
# print(year)
# number = clubs[3][3][0][0]
# print(number)
# benzema = clubs[1][3][1]
# print(benzema)


# def order_words(p_text):
#     words = p_text.split()
#     nested_list = list()
#     for word in words:
#         nested_list.append((len(word), word))
#         print(nested_list)
#
#
# order_words("Python is my favorite programming language")

#
# music = [
#             ("Green Day",
#                         [
#                             (1, "Somewhere Now"),
#                             (2,	"Bang Bang"),
#                             (3, "Revolution Radio"),
#                             (4, "Say Goodbye"),
#                             (5,	"Outlaws"),
#                         ]
#             ),
#             ("Metallica",
#                         [
#                             (1, "Battery"),
#                             (2,	"Master of Puppets"),
#                             (3,	"The Thing That Should Not Be"),
#                             (4,	"Welcome Home (Sanitarium)"),
#                         ]
#             ),
#             ("U2",
#                         [
#                             (1,	"The Miracle"),
#                             (2,	"Every Breaking Wave"),
#                             (3,	"California"),
#                             (4,	"Song for Someone"),
#                             (5,	"Iris (Hold Me Close)"),
#                         ]
#             ),
#         ]
#
#
# def print_playlist():
#     for artist_index, t_song in enumerate(music, 1):
#         artist, songs = t_song
#         for song_num, song in songs:
#             print(f"{artist_index}:{song_num} {artist} - {song}")
#
#
# while True:
#     print_playlist()
#     current_play = input("\nSelect a song to play using number:(1:1) ")
#     print(f"\n{music[int(current_play[0]) - 1][0]} - {music[int(current_play[0]) - 1][1][int(current_play[2]) -
#     1][1]} playing now....")
#     change = input("\nPress C to change song or any letter to quit APP: ")
#     if change == "C":
#         continue
#     break

# def adding_set(list):
#     lists = set()
#     for item in list:
#         lists.add(item)
#     return lists
#
#
# my_list = [3, 4, 5, 1, 1, 3, 4, 9, 8]
# print(adding_set(my_list))


# my_list = ["apple", "apple", "orange", "grape", "grape", "orange", "apple"]
#
# my_set = set(my_list)
# my_list = list(my_set)
# print(my_list)

#
# set1 = {10,20,30,40,50}
# set2 = {60,20,50,70}
#
# both_sets = set1.union(set2)
# print(both_sets)


# def convert_ls(list):
#     lists = set()
#     for item in list:
#         lists = lists.union(item)
#     return lists
#
#
# list_of_sets = [
#     {10,20,30,40,50},
#     {"apple", "orange","limon","pear"},
#     {"London", "Berlin", "Paris"},
#     {"Python", "Java", "Swift"},
#     {10, "ten", "20", 20}
# ]
# print(convert_ls(list_of_sets))

# def divisible_by_3and4(number):
#     d3 = set(range(0, number, 3))
#     d4 = set(range(0, number, 4))
#     result = d3.intersection(d4)
#     return print(result)
#
#
# divisible_by_3and4(100)
#
# while True:
#     print("Enter 5 different numbers from 1 to 69, with spaces between \neach number. (For example: 5 17 23 42 50)")
#     response = input("> ")
#
#     numbers = response.split()
#     # Check that the player entered 5 things
#     if len(numbers) != 5:
#         print("Please enter 5 numbers, separated by spaces.")
#         continue
#     # Convert the strings into integers
#     try:
#         for i in range(5):
#             numbers[i] = int(numbers[i])
#     except ValueError:
#         print("Please enter numbers, like 1,10 or 35")
#         continue
#     # Check that the numbers are between 1 and 69
#     between_1_69 = True
#     for item in numbers:
#         if not (1 <= item <= 69):
#             print("The numbers must be between 1 and 69")
#             between_1_69 = False
#             break
#     if not between_1_69:
#         continue
#     # Check that the numbers are unique
#     if len(set(numbers)) != 5:
#         print("You must enter 5 different numbers")
#         continue
#     break
#
# # Step 2 - Ask the player to select the powerball between 1 to 26
# while True:
#     print("Enter the powerball number from 1 to 26.")
#     response = input('> ')
#     try:
#         powerball = int(response)
#     except ValueError:
#         print("Please enter a number, like 1, 10 or 35")
#         continue
#
#     if not (1 <= powerball <= 26):
#         print("The powerball number must be between 1 and 26")
#         continue
#     break
#
# # Step 3 - Enter the number of times you want to play
# while True:
#     print("How many times do you want to play (Max: 1000000)? ")
#     reponse = input('> ')
#     #  Convert the strings into integers
#     try:
#         numPlays = int(reponse)
#     except ValueError:
#         print("Please enter a number, like 1, 10 or 35")
#         continue
#     #  Check that the number is between 1 and 1000000
#     if not (1 <= numPlays <= 1000000):
#         print("You can play between 1 and 1000000 times.")
#         continue
#     break
#
# # Step 4 - Run the simulation
# price = '$' + str(2 * numPlays)
# print(f"It costs {price} to play {numPlays} times, but dont \nworry. I'm sure you will win it all back.")
# input("Press Enter to start...")
# possibleNumbers = list(range(1, 70))
# for i in range(numPlays):
#     # Come up with lottery numbers
#     random.shuffle(possibleNumbers)
#     winningNumbers = possibleNumbers[0:5]
#     winningPowerball = random.randint(1, 26)
#     # Display winning numbers
#     print("The winning numbers are: ", end="")
#     allWinningNumbers = ""
#     for num in winningNumbers:
#         allWinningNumbers += str(num) + ' '
#     allWinningNumbers += "and " + str(winningPowerball)
#     print(allWinningNumbers, end="")
#     #  Check for winner
#     if (set(numbers) == set(winningNumbers) and powerball == winningPowerball):
#         print()
#         print("You have won the powerball Lottery! Congratulations.")
#         break
#     else:
#         print(" You Lost.")
# print(f"You have wasted {price}")
# print("Thanks for playing")


# import bext
#
# tile_types = (0, 1, 2, 3, 4, 5)
# colors = {0: "red", 1: "green", 2: "blue", 3: "yellow", 4: "cyan", 5: "purple"}
#
# board_width = 20
# board_height = 12
# moves_per_game = 20
# block = chr(9608)
#
#
# def get_new_board():
#     board = {}
#     for x in range(board_width):
#         for y in range(board_height):
#             board[(x, y)] = random.choice(tile_types)
#
#     for i in range(board_width * board_height):
#         x = random.randint(0, board_width - 2)
#         y = random.randint(0, board_height - 1)
#         board[(x+1, y)] = board[(x, y)]
#
#     return board
#
#
# def display_board(board):
#     for y in range(board_height):
#         for x in range(board_width):
#             bext.fg(colors[board[(x, y)]])
#             print(block, end="")
#             if (x + 1) % board_width == 0:
#                 print(end="")
#         print()
#
#
# def ask_for_player_move():
#     """Let the player select a color to paint upper left tile"""
#     while True:
#         bext.fg('white')
#         print("Choose one of ", end="")
#         bext.fg('red')
#         print("(R)ed ", end="")
#         bext.fg('green')
#         print("(G)reen ", end="")
#         bext.fg('blue')
#         print("(B)lue ", end="")
#         bext.fg('yellow')
#         print("(Y)ellow ", end="")
#         bext.fg('cyan')
#         print("(C)yan ", end="")
#         bext.fg('purple')
#         print("(P)purple ", end="")
#         bext.fg('white')
#         print("or QUIT:")
#         response = input("> ").upper()
#         if response == "QUIT":
#             print("Thanks for playing!")
#             sys.exit()
#         result = {'R':0, 'G': 1, 'B':2, 'Y':3, 'C':4, 'P':5}
#         return result[response]
#
#
# def change_tile(tile_color, board, x, y, color_to_change=None):
#     if x == 0 and y == 0:
#         color_to_change = board[(x, y)]
#         if tile_color == color_to_change:
#             return
#     board[(x, y)] = tile_color
#
#     if x > 0 and board[(x - 1, y)] == color_to_change:
#         # change left tile's color
#         change_tile(tile_color, board, x - 1, y, color_to_change)
#     if y > 0 and board[(x, y - 1)] == color_to_change:
#         # change bottom tile's color
#         change_tile(tile_color, board, x, y - 1, color_to_change)
#     if x < board_width - 1 and board[(x + 1, y)] == color_to_change:
#         # change right tile's color
#         change_tile(tile_color, board, x + 1, y, color_to_change)
#     if y < board_height - 1 and board[(x, y + 1)] == color_to_change:
#         # change top tile's color
#         change_tile(tile_color, board, x, y + 1, color_to_change)
#
#
# def has_won(board):
#     tile = board[(0, 0)]
#     for x in range(board_width):
#         for y in range(board_height):
#             if board[(x, y)] != tile:
#                 return False
#     return True
#
#
# print("Welcome to Flooder Game!")
# moves_left = moves_per_game
# new_board = get_new_board()
#
# while True:
#     display_board(new_board)
#     print("Moves left:", moves_left)
#     player_move = ask_for_player_move()
#     change_tile(player_move, new_board, 0, 0)
#     moves_left -= 1
#     if has_won(new_board):
#         display_board(new_board)
#         print("You have won!")
#         break
#     elif moves_left == 0:
#         display_board(new_board)
#         print("You have run out of moves!")
#         break


# while True:
#     number = input("Enter a number: ")
#     sum_of_digits = 0
#
#     try:
#         for digit in number:
#             sum_of_digits += int(digit)
#     except TypeError:
#         print("Value is not numberic")
#     else:
#         print("Sum of digits: ", sum_of_digits)
#     finally:
#         break

#
# def is_phone_number(phone):
#     if len(phone) != 12:
#         return False
#     for i in range(0, 3):
#         if not phone[i].isdecimal():
#             return False
#     if phone[3] != "-":
#         return False
#     for i in range(4, 7):
#         if not phone[i].isdecimal():
#             return False
#     if phone[7] != "-":
#         return False
#     for i in range(8, 12):
#         if not phone[i].isdecimal():
#             return False
#     return True
#
#
# print(is_phone_number("2s3-532-4325"))
# print(is_phone_number("213-532-4325"))


import re
#
#
# def find_three_con(p_text):
#     mo = re.search('\d\d\d', p_text)
#
#     if mo is None:
#         return 'Not found'
#     else:
#         return mo.group()
#
#
# text = "My phone number is: 234-456-8765"
# print(find_three_con(text))


# text = "We are testing mathematics 123"
# phone_num = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d)")
#
# mor = phone_num.search("My phone number: 555-532-553")
# mo = re.search('test', text)
#
# print(mo)
# print(mo.group())
# print(mor.group(0))
#
#
# def text_match(text):
#     regex_pattern = re.compile(r'((l|L)ove(rs)?)')
#     mo = regex_pattern.findall(text)
#     count = len(mo)
#     return count
#
#
# text = '''Lovers in love
# Lovers in love
# Love, love, love, love, love
# Love, love, love, love, love
# Love, love, love, love, love
# Love, love, love, love, love
# Lovers loving love just like these lovers are loving love in love
# Lovers loving love just like these lovers are loving love in love'''
#
# print(text_match(text))


import os

#
# def display_cwd():
#     cwd = os.getcwd()
#     print(f"Current working directory: {cwd}")
#
#
# def up_one_directory_level():
#     os.chdir("../")
#
#
# def display_entries_in_directory(directory):
#     entries = os.scandir(directory)
#     for entry in entries:
#         print(entry.name)
#
#
# display_cwd()
# up_one_directory_level()
# up_one_directory_level()
# display_cwd()
# display_entries_in_directory("PythonProjects")


import pathlib
import turtle

# entries = os.scandir(".")
# total = 0
# for entry in entries:
#     if entry.is_file():
#         print(entry.name)
#         total += 1
# print(total)
#
#
# def display_tree():
#     dictionary = pathlib.Path.cwd()
#     print(f"+ {dictionary}")
#     entries = sorted(dictionary.rglob("*"))
#     for entry in entries:
#         depth = len(entry.relative_to(dictionary).parts)
#         spacer = '    ' * depth
#         print(f"{spacer}+ {entry.name}")
#
#
# display_tree()
#
# file = open("read.txt")
# print(file.read())

# with open("read.txt", mode="r") as file:
#     line = file.readline()
#     while line != '':
#         print(line, end = '')
#         line = file.readline()

#
# def number_of_lines_file():
#     file_name = input("Enter the file name: ")
#     try:
#         file = open(file_name)
#     except FileNotFoundError:
#         print("Please enter correct file: ")
#         exit()
#     word = input("enter the word: ")
#     line_count = 0
#     for line in file:
#         line = line.rstrip()
#         if line.startswith(word):
#             line_count += 1
#     print(f"There are {line_count} {word} in {file_name}")
#
#
# number_of_lines_file()

# with open('read.txt') as file:
#     content = file.read()
#     print(content[:100])


# def number_of_characters(path):
#     with open(path) as file:
#         for index, row in enumerate(file, start=1):
#             print(index, len(row))
#
#
# number_of_characters("read.txt")

# with open('write.txt', 'w') as file:
#     for i in range(6):
#         content = f"{i}\n"
#         file.write(content)
#
#
# with open('write.txt', 'w') as file:
#     print("hi")
#


# from openpyxl import load_workbook
# from openpyxl.workbook import Workbook
# from openpyxl.styles import Font, Color

#
#
# workbook = load_workbook("worldcities.xlsx")
# sheet = workbook.active
# cell = sheet.cell(row=3, column=2)
# print(cell.value)
# for col in sheet.iter_cols(min_row=1, max_row=10, min_col=1, max_col=10, values_only=True):
#     print(col)

# for col in list(sheet.columns)[1]:
#     print(col.value)

# reviews = {}
# for row in sheet.iter_cols(min_row=1, max_row=10, min_col=1, max_col=10, values_only=True):
#     print(row)
#     review_id = row[0]
#     review = {
#         "city": row[1],
#         "country": row[5]
#
#     }
#     reviews[review_id] = review
# print(reviews)

#
# new_workbook = Workbook()
# sheet = new_workbook.active
# red_text = Font(color="00ff0000", size=15, bold=True)
# sheet['A1'] = "name"
# sheet['B1'] = "surname"
# sheet['A1'].font = red_text
# sheet['B1'].font = red_text
# sheet['A4'] = "6"
# sheet['B4'] = "5"
# sheet['C4'] = "=Sum(A4+B4)"
# new_workbook.save("newworkbook.xlsx")


# import pyautogui


# pyautogui.moveTo(400, 400, 1)
# pyautogui.moveTo(600, 400, 1)
# pyautogui.moveTo(600, 600, 1)
# pyautogui.moveTo(400, 600, 1)
# # pyautogui.moveTo(400, 400, 1)
#
# time.sleep(3)Í
# pyautogui.drag(100, 0, duration=0.5, button='left')
# pyautogui.drag(0, 100, duration=0.5, button='left')

# pyautogui.screenshot("hea.png")

# pyautogui.hotkey('ctrl', 'alt', 'shift', 's')

#
# from turtle import Turtle, Screen
#
#
# def random_color():
#     r = random.randint(0, 255)/ 255
#     g = random.randint(0, 255)/ 255
#     b = random.randint(0, 255)/ 255
#     return r, g, b
#
#
# new_turtle = Turtle()
# screen = Screen()
# new_turtle.pensize(40)
# new_turtle.pencolor(random_color())

# new_turtle.goto(100, 100)
# new_turtle.left(120)  # < ^
# new_turtle.forward(65)
# new_turtle.left(90)  # < ⌄
# new_turtle.forward(75)
# new_turtle.right(60)  # < ^
# new_turtle.forward(75)
# new_turtle.left(90)  # < ⌄
# new_turtle.forward(65)
# new_turtle.left(75)
# new_turtle.home()
# new_turtle.begin_fill()
# new_turtle.circle(140)
# new_turtle.speed(15)
# new_turtle.pensize(40)
# border_x = 300
# border_y = 300
#
# directions = [0, 90, 180, 270]
# for _ in range(100000):
#     new_turtle.color(random_color())
#     new_turtle.forward(40)
#     new_turtle.setheading(random.choice(directions))
#
#     x, y = new_turtle.position()
#     if abs(x) > border_x or abs(y) > border_y:
#         new_turtle.undo()
#         new_turtle.setheading(new_turtle.heading() + 180)
#
# screen.mainloop()

#
# new_list = [i*i for i in range(1,11)]
# print(new_list)


# def generate_password_lc():
#     letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     nums = "1234567890"
#     symbols = "-+=!@#$%^&*"
#     password_letters = [random.choice(letters) for _ in range(1, random.randint(0, 12))]
#     password_numbers = [random.choice(nums) for _ in range(1, random.randint(3, 5))]
#     password_symbols = [random.choice(symbols) for _ in range(1, random.randint(3, 5))]
#     password_list = password_symbols + password_numbers + password_letters
#     random.shuffle(password_list)
#     password = ''.join(password_list)
#     return password
#
#
# print(generate_password_lc())

# city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']
#
# city_temps = {city: random.randint(20, 30) for city in city_names}
# print(city_temps)
#
# above_25 = {city: temp for (city, temp) in city_temps.items() if temp >25}
# print(above_25)

#
# numbers = {number:number*number for number in range(10, 21)}
# print(numbers)

#
# city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']
#
# def contains_n(p_city):
#     for name in p_city:
#         if 'n' in name:
#             yield name
#
#
# names = contains_n(city_names)
# print(list(names))
import requests

parameters = {
    "lat": 41.616756,
    "lon": 41.636745,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
print(data['results']['sunrise'])
print(data['results']['sunset'])
