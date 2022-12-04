#!/usr/bin/python3
def element_at(my_list, idx):
    count = 0
    if idx < 0:
        return None
    for i in my_list:
        count += 1
    if idx >= count:
        return None
    else:
        return my_list[idx]
