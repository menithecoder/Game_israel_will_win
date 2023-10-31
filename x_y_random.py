import random


def rand(x_or_y,max_x):
    if x_or_y=='y':
        random_integer = random.randint(270, 400)
    else:
        random_integer = random.randint(0,max_x)

    return random_integer






