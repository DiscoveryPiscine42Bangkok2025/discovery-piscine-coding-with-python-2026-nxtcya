#!/usr/bin/env python3
origi = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array : {origi}")
i = 0
while i < len(origi) :
    origi[i] = origi[i]+2
    i += 1
print(f"New array : {origi}")
