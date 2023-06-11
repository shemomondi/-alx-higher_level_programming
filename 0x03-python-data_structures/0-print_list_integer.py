#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """Should Print all intergers of a list."""
    for num in range(len( my_list)):
        print("{:o}".format(my_list[num]))

