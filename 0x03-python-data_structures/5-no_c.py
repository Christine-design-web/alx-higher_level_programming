#!/usr/bin/python3

def no_c(my_string):
    updated_str = ''
    for j in my_string:
        if j != 'c' and j != 'C':
            updated_str += j
    return (updated_str)
