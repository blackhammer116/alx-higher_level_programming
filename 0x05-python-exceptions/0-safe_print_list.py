#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = ''
    c = 0
    try:
        for i in my_list:
            if i > x:
                break
            print(i, end="")
            c += 1
        print()
    except IndexError:
        print("index out of range")
        return c
    finally:
        return c
