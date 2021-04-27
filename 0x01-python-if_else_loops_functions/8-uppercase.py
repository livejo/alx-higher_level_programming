#!/usr/bin/python3
def uppercase(str):
    upperString =""
    for i in str:
        upper = ord(i)
        if ord('a') <= upper <= ord('z'):
            upper=upper - 32
        upperString = upperString + chr(upper)
    print("{}".format(upperString))
