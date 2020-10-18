from Validator import Validator as v
from linked_list import Linked_List as List


def menu_text():
    print("-"*30 + "MAIN MENU" + 30*"-")
    print("1. First  strategy")
    print("2. Second strategy")
    print("3. Generate numbers")
    print("4. Delete an element by position")
    print("5. Delete several elements in bounds")
    print("6. Apply task on lists")
    print("7. Print both lists")
    print("8. Exit")


def main_menu():
    while True:
        menu_text()
        menu_option = v.input_int("Choose an option from menu: ")

        if menu_option <= 0 or menu_option > 8:
            print("None such option exists")
            continue

        if menu_option == 1:
            # placeholder
            break
        if menu_option == 2:
            # placeholder
            break
        if menu_option == 3:
            # placeholder
            break
        if menu_option == 4:
            # placeholder
            break
        if menu_option == 5:
            # placeholder
            break
        if menu_option == 6:
            # placeholder
            break
        if menu_option == 7:
            # placeholder
            break
        if menu_option == 8:
            break


main_menu()
