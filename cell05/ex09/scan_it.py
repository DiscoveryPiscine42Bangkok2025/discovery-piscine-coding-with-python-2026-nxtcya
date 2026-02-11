#!/usr/bin/env python3
import sys
import re

if len(sys.argv)-1 !=2 :
    print("none")

else:
    key = sys.argv[1]
    search = sys.argv[2]

    research = re.findall(re.escape(key),search)

    if not research :
        print("none")
    else:
        print(len(research))
