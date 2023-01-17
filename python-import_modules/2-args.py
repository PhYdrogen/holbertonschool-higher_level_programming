#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb_elem = len(sys.argv) - 1
    if nb_elem > 0:
        print("{} arguments:".format((nb_elem)))
        for i in range(1, nb_elem + 1):
            print("{}: {}".format(i, sys.argv[i]))
    if nb_elem == 1:
        print("1 argument:")
        for i in range(1, nb_elem + 1):
            print("{}: {}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
