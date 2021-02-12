from Validator import Validator


def prime_luca_numbers_generator(quantity):
    if quantity == 0:
        return

    a = 2
    b = 1

    counter = 0
    while counter < int(quantity):
        if Validator.is_prime(a):
            counter += 1
            yield a

        c = a + b
        a = b
        b = c
