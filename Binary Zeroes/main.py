# Для заданих натуральних чисел N і K потрібно обчислити кількість чисел від 1 до N,
# що мають в двійковій запису рівно K нулів.
# Наприклад, якщо N = 8 і K = 1, то ми можемо записати всі числа від 1 до 8 в двійковій системі числення:
# 1, 10, 11, 100, 101, 110, 111 і 1000.
# Очевидно, що тільки числа 10, 101 і 110 мають рівно один нуль в записі, тобто правильну відповідь - 3.


def count_zeroes(num):
    counter = 0
    while num > 1:
        if num % 2 == 0:
            counter += 1
        num //= 2
    return counter


def count_numbers(n, k):
    counter = 0
    for i in range(1, n + 1):
        if count_zeroes(i) == k:
            counter += 1
    return counter


print(count_numbers(256, 8))
