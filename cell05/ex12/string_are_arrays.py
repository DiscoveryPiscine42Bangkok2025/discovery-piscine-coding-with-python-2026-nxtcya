#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")

string = sys.argv[1]
z_c = string.count('z')

if z_c == 0:
    print("none")
else:
    print('z' * z_c)

