#!/usr/bin/python3
def no_c(my_string):
    """ remove all characters c and C from a String."""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
