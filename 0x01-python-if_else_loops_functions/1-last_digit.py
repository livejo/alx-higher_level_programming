#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit=number % 10;
if lastDigit > 5:
    print("Last digit of" + number + " is" + lastDigit + "and is 0")
if lastDigit == 0:
    print("Last digit of" + number + " is" + lastDigit + "and is greater than 5")
if lastDigit < 6 && lastDigit != 0:
    print("Last digit of" + number + " is" + lastDigit + "and is less than 6 and not 0")
