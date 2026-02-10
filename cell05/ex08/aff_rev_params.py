#!/usr/bin/env python3
import sys

world = sys.argv[1:]
if len(world) < 2 :
    print("none")
    
else:
    rev = world[::-1]
    for world in rev:
        print(world)
    