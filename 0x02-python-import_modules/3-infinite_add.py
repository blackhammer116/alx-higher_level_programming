#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = 0
    for args in argv[1:]:
        n += int(args)
    print(n)
