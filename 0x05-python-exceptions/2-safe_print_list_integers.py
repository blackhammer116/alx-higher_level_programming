#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    c = 0
    j = 0
    try:
        for i in my_list:
            j += 1
        for i in my_list:
            if c < x:
                if type(i) == str:
                    continue
                elif type(i) == int:
                    print("{:d}".format(i), end="")
                    c += 1
        if x > j:
            raise IndexError('list index out of range')
        print()
    except IndexError:
        raise
    else:
        return c
