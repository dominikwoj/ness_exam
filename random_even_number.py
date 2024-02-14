import random

while True:
    x = random.randint(0, 10)
    if x == 0: # <- order is important here, check if x is equel 0 first
        break
    elif (x % 2) == 0: # checks if number is even
        print(x)