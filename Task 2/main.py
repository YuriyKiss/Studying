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


def validate_int(info):
    while True:
        try:
            num = int(input(info))
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
        while True:
            elements_amount = validate_int("How much elements you want to generate? ")
            if elements_amount <= 0:
                print("Array should contain more than 0 elements.")
                continue
            break

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
        min_res = min(resulting_array)
        max_res = max(resulting_array)

        print("There are", len(resulting_array), "negative products of X(i) * Y(y)",
              "\nMinimal element is", min_res,
              "\nMaximal element is", max_res, '\n')

        first_processed = array_processing(first_array, min_res, max_res)
        print("First array after processing:", first_processed)
        second_processed = array_processing(second_array, min_res, max_res)
        print("Second array after processing:", second_processed, '\n')

    elif menu_option == 2:
        while True:
            size = validate_int("How much elements you want to be in array? ")
            if size <= 0:
                print("Array should contain more than 0 elements.")
                continue
            break

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
        min_res = min(resulting_array)
        max_res = max(resulting_array)

        print("There are", len(resulting_array), "negative products of X(i) * Y(y)",
              "\nMinimal element is", min_res,
              "\nMaximal element is", max_res, '\n')

        first_processed = array_processing(first_array, min_res, max_res)
        print("First array after processing:", first_processed)
        second_processed = array_processing(second_array, min_res, max_res)
        print("Second array after processing:", second_processed, '\n')

    elif menu_option == 3:
        break
