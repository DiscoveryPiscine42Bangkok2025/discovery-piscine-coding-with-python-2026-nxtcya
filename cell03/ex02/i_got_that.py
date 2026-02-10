#!/usr/bin/env python3

say = str(input("What you gotta say? : ").strip())

while True:
    key = str(input("I got that! Anything else? : "))
    if key == "STOP":
        break
    