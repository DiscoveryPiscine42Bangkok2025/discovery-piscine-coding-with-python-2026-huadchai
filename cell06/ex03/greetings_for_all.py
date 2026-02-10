#!/usr/bin/env python3
def greetings(x="noble stranger"):
    if isinstance(x, str):
        print(f"Hello, {x}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)