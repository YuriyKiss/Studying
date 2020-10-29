# Variant 1
from collection import Collection
from validator import Validator


def print_menu_options():
    print("-" * 25, "MENU", "-" * 25)
    print("1. Read the file")
    print("2. Add new BlaBlaCar")
    print("3. Check the hour")
    print("4. Check the driver")
    print("5. Print BlaBlaCar collection")
    print("6. Exit")


data = Collection()

while True:
    print_menu_options()

    menu_option = Validator.input_positive("Choose an option from menu: ")
    if menu_option > 6:
        print("Menu has only 8 options!")
        continue
    if menu_option == 1:
        file = Validator.input_file("Name of the file: ")

        data.read_a_file(file)
    if menu_option == 3:
        data.time()
    if menu_option == 4:
        file = Validator.input_file("Name of the file: ")

        data.driver(file)
    if menu_option == 5:
        print(data)
    if menu_option == 6:
        break
