#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    X = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            X += 1
    except IndexError:
        pass
    finally:
        print("")
        return X
