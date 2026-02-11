#!/usr/bin/env python3
import sys
word = sys.argv[1:]
if not word :
    print("none")
for x in word:
    if not x.endswith("ism"):
        print(f"{x}ism")
