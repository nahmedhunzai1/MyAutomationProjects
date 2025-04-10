import random


def random_strings_function():
    list = ["one", "two", "three", "four", "five"]

    random_strings = random.choice(list)
    return  random_strings


def using_random_strings_here():
    lists = random_strings_function()

    for i in lists:
        print(lists)

using_random_strings_here()