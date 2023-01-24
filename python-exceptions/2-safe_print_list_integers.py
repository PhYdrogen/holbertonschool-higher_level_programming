#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        count += 1
        try:
            print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            count -= 1
            pass
    print()
    return count
