from sequence import Sequence
from Validator import Validator
from generator import prime_luca_numbers_generator as generate


while True:
    print("1. Get sequence from iterator")
    print("2. Get sequence from generator")
    print("3. Exit")

    menu_option = Validator.input_int("Choose an option from menu: ")
    if menu_option == 3:
        break

    if menu_option != 1 and menu_option != 2:
        print("Menu option should be either 1, 2 or 3")
        continue

    quantity = Validator.input_int('How many Luca\'s prime numbers should the code generate: ')

    if menu_option == 1:
        a = Sequence()

        print(a)
        for i in range(quantity - 1):
            print(next(iter(a)))

    if menu_option == 2:
        for item in generate(quantity):
            print(item)
