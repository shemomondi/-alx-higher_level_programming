#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
m = 0
for l in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(l - m)), end="")
    m = 32 if m == 0 else 0

