#!/usr/bin/python3
# 7-islower.py


def islower(l):
    """Check for lowercase characters."""
    if ord(l) >= 97 and ord(l) <= 122:
        return True
    else:
        return False
