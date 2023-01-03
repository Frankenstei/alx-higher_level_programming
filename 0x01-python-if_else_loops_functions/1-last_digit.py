#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(f'Last digit of {number} is {number%10} and is')
if abs(number%10) > 5:
    print("greater than 5")
elif abs(number%10) == 0:
    print("0")
elif abs(number%10) < 6 and abs(umber%10) != 0:
    print("less than 6 and not 0")
