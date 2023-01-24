#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for i in range(x):
            print(my_list[i], end="")

        print()

    except IndexError:
        print()
        i -= 1
    finally:
        return i + 1
