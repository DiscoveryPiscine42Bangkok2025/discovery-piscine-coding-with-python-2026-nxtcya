#!/usr/bin/env python3
origi = [2, 8, 9, 48, 8, 22, -12, 2]
print(origi)

new = []

for x in origi :
    if x > 5 :
        new.append(x+2)
setN = set(new)
print(setN)