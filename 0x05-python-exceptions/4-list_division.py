#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i,j in my_list_1,my_list_2:
            k = 0
            if len(result) < list_length:
                '''
                if type(i) != int or type(j) != int:
                    result[k] = 0
                    raise TypeError
                elif j == 0:
                    result[k] = 0
                    raise ZeroDivisionError
                elif len(my_list_1) < len(my_list_2):
                    result[k] = 0
                    raise IndexError
                else:
                '''
                result[k] = my_list_1[k] / my_list_2[k]
            k += 1
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return result
