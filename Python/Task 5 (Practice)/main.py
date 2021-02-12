from Validator import Validator as Valid
from Strategy.Context import Context
from Strategy.StrategyIterator import StrategyIterator
from Strategy.StrategyFile import StrategyFile
from linked_list import Linked_List as List
from Task import the_task


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
    print("-" * 70)


def main_menu():
    cont = Context()
    first, second = List(), List()

    while True:
        menu_text()
        menu_option = Valid.input_positive_int("Choose an option from menu: ")

        if menu_option == 0 or menu_option > 8:
            print("None such option exists")
            continue

        if menu_option == 1:
            cont.set_strategy(StrategyIterator())
        if menu_option == 2:
            cont.set_strategy(StrategyFile())
        if menu_option == 3:
            if Valid.check_context(cont):
                continue
            if choose_list():
                modify_list(first, cont)
            else:
                modify_list(second, cont)
        if menu_option == 4:
            if choose_list():
                remove_el(first)
            else:
                remove_el(second)
        if menu_option == 5:
            if choose_list():
                remove_few(first)
            else:
                remove_few(second)
        if menu_option == 6:
            the_task(first, second)
        if menu_option == 7:
            print_lists(first, second)
        if menu_option == 8:
            break


def choose_list():
    while True:
        list_n = Valid.input_positive_int("We are modifying list № ")

        if list_n == 0 or list_n >= 3:
            print("There are only two lists")
            continue

        if list_n == 1:
            return True
        else:
            return False


def modify_list(op_list, cont):
    print("P stands for position of inserting(0; " + str(len(op_list)) + ")")
    position = Valid.input_int_in_bounds("P = ", 0, len(op_list))

    if cont.get_strategy() == "Iterator":
        print("N stands for amount of generated numbers (0; any)")
        amount = Valid.input_positive_int("N = ")
        cont.use_strategy(op_list, amount, position)
    if cont.get_strategy() == "File":
        print("F stands for file any_text.txt")
        file = Valid.input_file("F = ")
        cont.use_strategy(op_list, file, position)


@Valid.check_op_list
def remove_el(op_list):
    print("P stands for position of removing (0; " + str(len(op_list)) + ")")
    position = Valid.input_int_in_bounds("P = ", 0, len(op_list))

    op_list.remove(position)


@Valid.check_op_list
def remove_few(op_list):
    print("L stands for left bound of removing (0; " + str(len(op_list)) + ")")
    pos1 = Valid.input_int_in_bounds("L = ", 0, len(op_list))

    print("R stands for right bound of removing (" + str(pos1) + "; " + str(len(op_list)) + ")")
    pos2 = Valid.input_int_in_bounds("R = ", pos1, len(op_list))

    for i in range(pos2 - pos1 + 1):
        op_list.remove(pos1)


def print_lists(first, second):
    print("1. " + str(first))
    print("2. " + str(second))


main_menu()
