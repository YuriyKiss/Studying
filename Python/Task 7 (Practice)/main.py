from Validator import Validator as Valid
from Strategy.Context import Context
from Strategy.StrategyIterator import StrategyIterator
from Strategy.StrategyFile import StrategyFile
from linked_list import Linked_List as List
from Task import the_task
from Observer import Logger, Observer
from copy import deepcopy
from threading import Thread

counting_array = ['first', 'second', 'third', 'fourth', 'fifth']  # allows to use up to five threads


def few_threads(amount, target, **kwargs):
    for i in range(amount):
        new_thread = Thread(target=target, args=kwargs[counting_array[i]])
        new_thread.start()
        new_thread.join()


def initialization():
    print("-"*30 + "INITIALIZATION" + 30*"-")
    log_to = Valid.input_file("File to log all list changes: ")

    open(log_to, "w")

    obs = Observer(["add_to_list", "remove_from_list"], log_to)

    first_list = Logger("First list")
    second_list = Logger("Second list")

    obs.register("add_to_list", first_list)
    obs.register("remove_from_list", first_list)
    obs.register("add_to_list", second_list)
    obs.register("remove_from_list", second_list)

    return obs


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

    obs = initialization()

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
                modify_list("First list", first, cont, obs)
            else:
                modify_list("Second list", second, cont, obs)
        elif menu_option == 4:
            if len(first) > len(second):
                print("P stands for position of removing (0; " + str(len(second)) + ")")
                position = Valid.input_int_in_bounds("P = ", 0, len(second))
            else:
                print("P stands for position of removing (0; " + str(len(first)) + ")")
                position = Valid.input_int_in_bounds("P = ", 0, len(first))

            few_threads(2, remove_el, first=("First list", first, obs, position, 0),
                        second=("Second list", second, obs, position, 0))
        elif menu_option == 5:
            if len(first) > len(second):
                print("L stands for left bound of removing (0; " + str(len(second)) + ")")
                pos1 = Valid.input_int_in_bounds("L = ", 0, len(second))

                print("R stands for right bound of removing (" + str(pos1) + "; " + str(len(second)) + ")")
                pos2 = Valid.input_int_in_bounds("R = ", pos1, len(second))
            else:
                print("L stands for left bound of removing (0; " + str(len(first)) + ")")
                pos1 = Valid.input_int_in_bounds("L = ", 0, len(first))

                print("R stands for right bound of removing (" + str(pos1) + "; " + str(len(first)) + ")")
                pos2 = Valid.input_int_in_bounds("R = ", pos1, len(first))
            
            few_threads(2, remove_few, first=("First list", first, obs, pos1, pos2),
                        second=("Second list", second, obs, pos1, pos2))
        elif menu_option == 6:
            the_task(first, second)
        elif menu_option == 7:
            few_threads(2, print, first=("1. ", str(first)), second=("2. ", str(second)))
        elif menu_option == 8:
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


def modify_list(name, op_list, cont, obs):
    print(f"Generating {name}")
    print("P stands for position of inserting(0; " + str(len(op_list)) + ")")
    position = Valid.input_int_in_bounds("P = ", 0, len(op_list))

    if cont.get_strategy() == "Iterator":
        print("N stands for amount of generated numbers (0; any)")
        amount = Valid.input_positive_int("N = ")
        original = deepcopy(op_list)
        cont.use_strategy(op_list, amount, position)
        obs.dispatch(name, "add_to_list", position, original, op_list, amount)
    if cont.get_strategy() == "File":
        print("F stands for file any_text.txt")
        file = Valid.input_file("F = ")
        original = deepcopy(op_list)
        cont.use_strategy(op_list, file, position)
        obs.dispatch(name, "add_to_list", position, original, op_list, file)


@Valid.check_op_list
def remove_el(name, op_list, obs, position, x):
    original = deepcopy(op_list)
    op_list.remove(position)
    obs.dispatch(name, "remove_from_list", position, original, op_list)


@Valid.check_op_list
def remove_few(name, op_list, obs, pos1, pos2):
    original = deepcopy(op_list)

    arr = []
    for i in range(pos2 - pos1 + 1):
        arr.append(pos1 + i)
        op_list.remove(pos1)

    obs.dispatch(name, "remove_from_list", arr, original, op_list)


main_menu()
