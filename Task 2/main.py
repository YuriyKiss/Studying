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
from binary_search import *


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
                print("Array should contain more than 0 elements.")
                continue
            break
        except ValueError:
            print("WARNING - Please enter an integer.")
    return num


def negative_products(first, second):
    array_of_negatives = []

    for i in first:
        for j in second:
            if i * j < 0:
                array_of_negatives.append(i * j)

    return array_of_negatives


def array_processing(array, minimal_element, maximal_element):
    for i in range(0, len(array)):
        if array[i] == minimal_element:
            array[i] = 0
        if array[i] == maximal_element:
            array[i] *= (-1)

    return array


def find_min(array):
    min_el = array[0]
    for x in array:
        if x < min_el:
            min_el = x

    return min_el


def find_max(array):
    max_el = array[0]
    for x in array:
        if x > max_el:
            max_el = x

    return max_el


def min_max_manipulations(first, second, resulting):
    min_res = find_min(resulting)
    max_res = find_max(resulting)

    print("There are", len(resulting), "negative products of X(i) * Y(y)",
          "\nMinimal element is", min_res,
          "\nMaximal element is", max_res, '\n')

    first_processed = array_processing(first, min_res, max_res)
    print("First array after processing:", first_processed)
    second_processed = array_processing(second, min_res, max_res)
    print("Second array after processing:", second_processed, '\n')


def search(resulting):
    print("Array of negative products:", resulting)
    index_array = []
    for i in range(0, len(resulting)):
        index_array.append(i)

    simultaneous_sort(resulting, index_array)

    while True:
        value = validate_int("\nWhich value's position we are looking for: ")
        print("\nSorted array:      ", resulting)
        print("Sorted index array:", index_array)
        middle_el = binary_search(resulting, value)
        if middle_el == -1:
            print("There are no such value in the array")
            continue
        else:
            print("\n", value, "is", index_array[middle_el], "element of an array\n")
            several_elements(middle_el, resulting, index_array, value)
        break


while True:
    print('-' * 25, "MENU", '-' * 25)
    menu_option = validate_int("1. Input amount of random elements in both arrays\n"
                               "2. Input elements of each array\n"
                               "3. Exit\n"
                               "INPUT: ")

    if menu_option != 1 and menu_option != 2 and menu_option != 3:
        print("Input 1, 2 or 3 to choose an option from menu!")
        continue

    elif menu_option == 1:
        elements_amount = validate_size("How much elements you want to generate? ")

        first_array, second_array = [], []
        lower_rand = validate_int("Input lower limit for generating: ")
        upper_rand = validate_int("Input upper limit for generating: ")
        if lower_rand > upper_rand:
            lower_rand, upper_rand = upper_rand, lower_rand
        for i in range(0, elements_amount):
            first_array.append(random.randint(lower_rand, upper_rand))
            second_array.append(random.randint(lower_rand, upper_rand))

        print("\nFirst array contains:", first_array,
              '\nSecond array contains:', second_array, '\n')

        resulting_array = negative_products(first_array, second_array)
        if len(resulting_array) == 0:
            print("There is no negative products")
            continue
        min_max_manipulations(first_array, second_array, resulting_array)

        search(resulting_array)

    elif menu_option == 2:
        size = validate_size("How much elements you want to input? ")

        first_array, second_array = [], []
        print("Enter elements of first array")
        for i in range(0, size):
            first_array.append(validate_int("[" + str(i) + "] = "))

        print("Enter elements of second array")
        for i in range(0, size):
            second_array.append(validate_int("[" + str(i) + "] = "))

        print("\nFirst array contains: ", first_array,
              '\nSecond array contains: ', second_array, '\n')

        resulting_array = negative_products(first_array, second_array)
        if len(resulting_array) == 0:
            print("There is no negative products")
            continue
        min_max_manipulations(first_array, second_array, resulting_array)

        search(resulting_array)

    elif menu_option == 3:
        break
