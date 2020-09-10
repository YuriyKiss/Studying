# Згенерувати послідовність простих чисел Люка розмірності n.
# Просте число  — це натуральне число, яке має рівно два різних натуральних дільники (одиницю та саме число)
# Числа Люка задаються рекурентною формулою L(n) = L(n-1) + L(n-2), де L(0) = 2 та L(1) = 1.
from math import sqrt
from math import ceil


# Часова складність алгоритму (Time Complexity) приблизно O(sqrt(n)),
# якщо займатись оптимізацією, то саме цієї функції
def is_prime(num):
    if num == 1 or num == 4:
        return False  # Число 1 не є простим числом (не має двох дільників),
        # а корінь числа 4 дорівнює 2 через що не проходить наступну перевірку

    for i in range(2, ceil(sqrt(num))):
        if num % i == 0:
            return False

    return True


def prime_luca_numbers(num):
    if num == 0:
        return

    a = 2  # Нульова позиція
    b = 1  # Перша позиція

    print(a)

    counter = 1  # Змінна, яка обмежує розмірність послідовності заданим числом
    while counter < int(num):
        if is_prime(b):
            counter += 1
            print(b)

        c = a + b
        a = b
        b = c


print('How many Luca\'s prime numbers should the code generate?')
quantity = input('Attention! Generating more than 16 numbers can considerably slow down the process! ')
prime_luca_numbers(quantity)
