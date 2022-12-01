#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    list_ = dir()
    for names in list_:
        if names[:2] != "__":
            print(names)
