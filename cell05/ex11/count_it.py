#!/usr/bin/env python3

import sys

word = sys.argv[1:]
if len(word) == 0:
    print("none")
else:
    print(f"parameters : {len(word)}")
    for x in word :
        print(f"{x} : {len(x)}")