# Завдання №3. Linked List. Переписати завдання за допомогою Linked List.

# Завдання повинно бути виконано з мінімальною кількістю операцій та з використанням функцій.
# Передбачити можливість 2 варіанти введення масивів:
# ввести кількість елементів та згенерувати рандомні елементи, або ввести сам масив.
# Користувач має мати право вибирати безліч разів один чи інший варіант введення та тестувати програму.
# По закінченню тестування користувач має мати змогу вийти з меню.

# Задано масиви x та y, які складаються з N чисел.
# Порахувати кількість добутків (x(i) * y(j)) < 0 і знайти максимальне та мінімальне з них.
# Всі числа в масивах x та y, які рівні максимальному елементу, замінити на протилежне,
# а ті числа, які дорівнюють мінімальному, замінити на нулі.
import random
from linked_list import *


def validate_int(info):
    while True:
        try:
            num = int(input(info))
            break
        except ValueError:
            print("WARNING - Please enter an integer.")
    return num


def validate_size(info):
    while True:
        try:
            num = int(input(info))
            if num <= 0:
                print("List should contain more than 0 elements.")
                continue
            break
        except ValueError:
            print("WARNING - Please enter an integer.")
    return num


def negative_products(first, second):
    list_of_negatives = Linked_List()

    for i in first:
        for j in second:
            if i * j < 0:
                list_of_negatives.append(i * j)

    return list_of_negatives


def list_processing(linked, minimal_element, maximal_element):
    for i in range(0, len(linked)):
        if linked[i] == minimal_element:
            linked[i] = 0
        if linked[i] == maximal_element:
            linked[i] *= (-1)

    return linked


def find_min(linked):
    min_el = linked[0]
    for x in linked:
        if x < min_el:
            min_el = x

    return min_el


def find_max(linked):
    max_el = linked[0]
    for x in linked:
        if x > max_el:
            max_el = x

    return max_el


def min_max_manipulations(first, second, resulting):
    min_res = find_min(resulting)
    max_res = find_max(resulting)

    print("\nThere are", len(resulting), "negative products of X(i) * Y(y)",
          "\nMinimal element is", min_res,
          "\nMaximal element is", max_res, '\n')

    print("...Processing lists...")
    first_processed = list_processing(first, min_res, max_res)
    second_processed = list_processing(second, min_res, max_res)
    print_lists(first_processed, second_processed)


def print_lists(first, second):
    print("\nFirst list contains X(i):")
    first.print()
    print('Second list contains Y(i):')
    second.print()


# Main function start #
while True:
    print('-' * 25, "MENU", '-' * 25)
    menu_option = validate_int("1. Input amount of random elements in both lists\n"
                               "2. Input elements of each list\n"
                               "3. Exit\n"
                               "INPUT: ")

    if menu_option != 1 and menu_option != 2 and menu_option != 3:
        print("Input 1, 2 or 3 to choose an option from menu!")
        continue

    elif menu_option == 1:
        elements_amount = validate_size("How much elements you want to generate? ")

        first_list, second_list = Linked_List(), Linked_List()
        lower_rand = validate_int("Input lower limit for generating: ")
        upper_rand = validate_int("Input upper limit for generating: ")
        if lower_rand > upper_rand:
            lower_rand, upper_rand = upper_rand, lower_rand
        for i in range(0, elements_amount):
            first_list.append(random.randint(lower_rand, upper_rand))
            second_list.append(random.randint(lower_rand, upper_rand))

        print_lists(first_list, second_list)

        resulting_list = negative_products(first_list, second_list)
        if len(resulting_list) == 0:
            print("There is no negative products")
            continue
        min_max_manipulations(first_list, second_list, resulting_list)

    elif menu_option == 2:
        size = validate_size("How much elements you want to input? ")

        first_list, second_list = Linked_List(), Linked_List()
        print("Enter elements of first list")
        for i in range(0, size):
            first_list.append(validate_int("[" + str(i) + "] = "))

        print("Enter elements of second list")
        for i in range(0, size):
            second_list.append(validate_int("[" + str(i) + "] = "))

        print_lists(first_list, second_list)

        resulting_list = negative_products(first_list, second_list)
        if len(resulting_list) == 0:
            print("There is no negative products")
            continue
        min_max_manipulations(first_list, second_list, resulting_list)

    elif menu_option == 3:
        break
