#!/usr/bin/env python3

num = int(input("Enter a number : ").strip())
x = 0

while x <= 8:
    result = x * num
    print(f"{x} x {num} = {result}")
    x +=1
