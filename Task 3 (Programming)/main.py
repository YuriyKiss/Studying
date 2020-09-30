# Завдання повинно бути виконано з мінімальною кількістю операцій,
# використанням мінімальної кількості циклів та з використанням функцій.
# Користувач має мати право безліч разів тестувати програму.
# По закінченню тестування користувач має мати змогу вийти з меню.

# Утворити матрицю і вивести її на екран:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 0, 0, 1, 2, 3, 4, 5, 6, 7]
# [0, 0, 0, 0, 1, 2, 3, 4, 5, 6]
# [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
# [0, 0, 0, 0, 0, 0, 1, 2, 3, 4]
# [0, 0, 0, 0, 0, 0, 0, 1, 2, 3]
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


def validation(info):
    while True:
        try:
            num = int(input(info))
            if num <= 0:
                print("This number should be bigger than 0.")
                continue
            break
        except ValueError:
            print("WARNING - Please enter an integer.")
    return num


def create_empty_matrix(n, m):
    a = [[0] * n for i in range(m)]
    return a


def apply_algorithm(a):
    for i in range(0, len(a)):
        k = 1
        for j in range(i, len(a[0])):
            a[i][j] = k
            k += 1


def print_matrix(a):
    for i in range(len(a)):
        print(a[i])


while True:
    print('-' * 25, "MENU", '-' * 25)
    menu_option = validation("1. Print task given matrix;\n"
                             "2. Classify matrix size and print it;\n"
                             "3. Exit;\n"
                             "INPUT: ")

    rows, columns = 1, 1
    if menu_option != 1 and menu_option != 2 and menu_option != 3:
        print("Input 1, 2 or 3 to choose an option from menu.")
        continue

    elif menu_option == 1:
        rows = 10
        columns = 10

    elif menu_option == 2:
        rows = validation("Input number of rows: ")
        columns = validation("Input number of columns: ")

    elif menu_option == 3:
        break

    task_matrix = create_empty_matrix(columns, rows)
    apply_algorithm(task_matrix)
    print_matrix(task_matrix)
    continue

