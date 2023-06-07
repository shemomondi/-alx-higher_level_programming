#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, k):
    """Create a copy of the string without the character at position k."""
    if k < 0:
        return (str)
    return (str[:k] + str[k+1:])
