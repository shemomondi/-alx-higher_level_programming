#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase."""
    for l in str:
        if ord(l) >= 97 and ord(l) <= 122:
            l = chr(ord(l) - 32)
        print("{}".format(l), end="")
    print("")
