#!/usr/bin/python3
# 7-add_tuple.py


def add_tuple(tuple_a=(), tuple_b=()):
    # Retrieve the first two elements from each tuple (or use 0 if not present)
    a1, a2 = tuple_a[:2] + (0, 0)
    b1, b2 = tuple_b[:2] + (0, 0)

    # Perform the addition of corresponding elements
    result = (a1 + b1, a2 + b2)

    return result

