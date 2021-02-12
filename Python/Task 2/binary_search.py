# Виробнича практика. Доповнити завдання з програмування.
# В результуючому масиві знайти число, яке дорівнює К за допомогою бінарного пошуку.
# Вивести позицію елемента, якщо елементів декілька, то позиції всіх елементів.
# Вивести кількість операцій, необхідних для пошуку, та всі здійснені операції.

def simultaneous_sort(elements, indexes):
    for i in range(0, len(elements) - 1):
        for j in range(0, len(elements) - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                indexes[j], indexes[j + 1] = indexes[j + 1], indexes[j]


def binary_search(array, value):
    low = 0
    mid = len(array) // 2
    high = len(array) - 1

    operations = 1

    print("\nLooking in range from", low, "to " + str(high), ",", array[mid], "is the middle element")
    while array[mid] != value and low <= high:
        if value > array[mid]:
            print(value, "is bigger than", array[mid])
            low = mid + 1
        else:
            print(value, "is smaller than", array[mid])
            high = mid - 1
        operations += 1
        mid = (low + high) // 2
        print("\nLooking in range from", low, "to " + str(high), ",", array[mid], "is the middle element")

    print("It took", operations, "operation(-s) to calculate")

    if low > high:
        return -1
    else:
        return mid


def several_elements(mid_pos, resulting, indexes, value):
    for i in range(mid_pos - 1, -1, -1):
        if resulting[mid_pos] == resulting[i] and i != mid_pos:
            print("Also,", value, "found on", indexes[i], "before first appearance of element")
        else:
            break
    for i in range(mid_pos + 1, len(resulting)):
        if resulting[mid_pos] == resulting[i] and i != mid_pos:
            print("Also,", value, "found on", indexes[i], "after first appearance of element")
        else:
            break
