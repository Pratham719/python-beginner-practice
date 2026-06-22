# RANDOM MODULE
# Used to generate random numbers and make random selections

import random


# ------------------
# RANDOM NUMBERS
# ------------------

# random() -> float between 0 and 1
# print(random.random())


# randint(start, end)
# return random integer (inclusive)

# print(random.randint(1, 6))   # dice


# randrange(start, end, step)
# return random value with step

# print(random.randrange(1, 10, 2))


# ------------------
# RANDOM SELECTION
# ------------------

coin = ["Head", "Tail"]

# choice() -> pick one random element

# print(random.choice(coin))


# choice() also works on strings
# print(random.choice("python"))


# sample(iterable, k)
# return k unique random elements

dice = [1, 2, 3, 4, 5, 6]

print(random.sample(dice, 2))


# ------------------
# RANDOM ORDER
# ------------------

# shuffle()
# randomly rearrange original list

# random.shuffle(dice)
# print(dice)


# ------------------
# EXTRA METHODS
# ------------------

# uniform()
# return random float in range

# print(random.uniform(1, 10))


# choices()
# return multiple random values
# duplicates allowed

# print(random.choices(dice, k=3))