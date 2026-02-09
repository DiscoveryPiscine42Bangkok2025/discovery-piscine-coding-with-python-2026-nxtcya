#!/usr/bin/env python3
first_num = int(input("Enter the first number : ").strip())
last_num = int(input("Enter the second number : ").strip())
result = first_num * last_num

print(f"{first_num} x {last_num}")
print(f"{first_num} x {last_num} = {result}" )

if result == 0:
    print("This result is positive and negative.")
elif result > 0 :
    print("This result is positive.")
else : 
    print("This result is negative.")