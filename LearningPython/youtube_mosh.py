# patient = "John Smith"
# age = "20"
# is_new = True
#
# if is_new:
#     is_new = "new"
# else:
#     is_new = "not new"
#
# print("We check in a patient named" + patient + ". He's " + age + " years old and is a " + is_new + " patient.")

# name = input("What's your name? ")
# color = input("What's your favorite color? ")
# print(f'Hello {name}, your favorite color is {color}')

# birth_year = input("Your birth year? ")
# age = 2023 - int(birth_year)
# print(age)

# pounds = float(input("What's your weight in pounds? "))
# kg = pounds * 0.453592
# print(f'You are {kg} Kilograms.')

# string = "Hello World"
# print(string[1])
# print(string[0:5])
# print(len(string))
# print(string.upper())
# print(string.find("W"))
# print(string.replace("World", "Becca"))
# print("Hello" in string)

# house_price = 1000000
# is_credit = "good"
#
# if is_credit == "good":
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price
# print(f"Down payment ${down_payment}")

# word = "Sea"
# if len(word) <= 3:
#     print("Word is too short.")
# elif len(word) > 50:
#     print("Word is too long.")
# else:
#     print("Success")


# weight = float(input("What's your weight? "))
#
# unit = (input("In Pounds (L) or in Kilograms (K)? "))
# if unit == "L":
#     kg = weight * 0.453592
#     print(f'You are {kg} Kilograms.')
# else:
#     pounds = weight / 0.453592
#     print(f'You are {pounds} pounds.')

# secret_number = 5
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess_number = int(input("Guess Number: "))
#     guess_count += 1
#     if guess_number == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry, you lost.")

# started = False
#
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started.")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print(" start - to start the car \n stop- to stop the car \n quit - to exit")
#     elif command == "quit":
#         break
#     else:
#         print("I don't understand... ")

# prices = [5, 10, 15]
#
# total = 0
# for price in prices:
#     total = total + price
# print(f'Total {total}')

# for x in range(4):
#     for y in range(3):
#         print(f' ({x}, {y})')

# numbers = [2, 2, 2, 2, 5]
#
# for x in numbers:
#     output = ''
#     for count in range(x):
#         output += 'x'
#     print(output)

# numbers = [5, 4, 2, 7, 6]
# max = numbers[0]
#
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5, 4, 2, 7, 7, 6, 1]
#
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# phone = input("Enter numbers: ")
#
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
#
# output = ""
# for ch in phone:
#     output += digits_mapping.get(ch, "!") + " "
# print(output)

# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)": "😁",
#     ":(": "😞"
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)


# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😁",
#         ":(": "😞"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     print(output)
#
#
# message = input("> ")
# emoji_converter(message)


# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except ValueError:
#     print("Enter number.")


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'''Hi, I'm {self.name}''')
#
#
# becca = Person("Becca")
# becca.talk()

# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     pass
#
#
# class Cat(Mammal):
#     pass
#
#
# dog = Dog()
# dog.walk()

