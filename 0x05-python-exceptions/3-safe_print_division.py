#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    result = ''
    try:
        result = a / b
    except ZeroDivisionError:
        c = -1
        result = 'None'
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        if c == -1:
            print("Inside result: None")
            return result
