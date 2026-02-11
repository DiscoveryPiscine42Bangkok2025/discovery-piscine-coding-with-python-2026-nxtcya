#!/usr/bin/env python3

import sys
if len(sys.argv) != 3:
    print("none")
else:
    st = int(sys.argv[1])
    en = int(sys.argv[2])
    result = list(range(st,en + 1))
    print(result)
