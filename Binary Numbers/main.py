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


while True:
    try:
        nu = int(input("Enter N. N = How much numbers from 1 to N we check "))      # nu - numbers
        am = int(input("Enter K. K = How much zeroes should binary number have "))  # am - amount of zeroes

        if nu > 109 or am > 109:
            print("\nEither N or K is bigger than 109")
            continue
        break
    except ValueError:
        print("\nBoth N and K should be an integers")

print("There are", count_numbers(nu, am), "numbers between 1 and", nu, "that have", am, "zeroes in binary")
