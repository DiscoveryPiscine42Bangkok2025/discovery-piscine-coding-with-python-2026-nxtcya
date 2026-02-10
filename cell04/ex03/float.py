#!/usr/bin/env python3

usInput = input("Give me a number : ")
num = float(usInput)
if(num.is_integer()):
    print("This number is an interger.")
else:
    print("This number is a decimal.")