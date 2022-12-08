#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    res = {key: val for key, val in sorted(a_dictionary.items(), key = lambda ele: ele[0])}
    for i, j in res.items():
        print(i, ':', j)
