from random import randint


def list_comp():
    divbythree = ["Yes" if number % 3 == 0 else "No" for number in range(1, 20)]
    print(divbythree)


list_comp()

random_numbers = [randint(number, 2 * number) for number in range(10)]
print(random_numbers)