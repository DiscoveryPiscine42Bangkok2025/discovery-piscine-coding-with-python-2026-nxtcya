#!/usr/bin/env python3

x = int(input("Give me the first number : ").strip())
y = int(input("Give me the second number : ").strip())
print("Thank you!")
add = x + y
sub = x - y
div = x/y
mul = x*y
print(f"{x} + {y} = {add}")
print(f"{x} - {y} = {sub}")
print(f"{x} / {y} = {div}")
print(f"{x} * {y} = {mul}")