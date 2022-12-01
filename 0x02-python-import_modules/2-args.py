#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("{}: arguments:".format(argc))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc))
        i = 1
        for args in argv[1:]:
            print("{}: {}".format(i, args))
            i += 1
