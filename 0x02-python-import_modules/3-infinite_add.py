#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    n = 0
    if argc == 0:
        print("0")
    else:
        for args in argv[1:]:
            n += int(args)
        print(n)
