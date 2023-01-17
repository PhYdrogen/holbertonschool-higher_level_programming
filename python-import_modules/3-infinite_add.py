#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb_elem = len(sys.argv)
    result = 0
    for i in range(1, nb_elem):
        result += int(sys.argv[i])
    print("{}".format(result))
