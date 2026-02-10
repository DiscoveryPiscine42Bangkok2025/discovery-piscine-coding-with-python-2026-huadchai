#!/usr/bin/env python3
import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    x = 8 - len(text)
    print(text + 'Z' * x)

if len(sys.argv) == 1:
    print("none")
else:
    y = sys.argv[1:]
    
    for i in y:
        if len(i) > 8:
            shrink(i)
        elif len(i) < 8:
            enlarge(i)
        else:
            print(i)