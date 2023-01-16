#!/usr/bin/python3
for i in range(97, 123):
    if i == 113 or i == 101:
        continue
    else:
        print("{0:c}".format(i), end="")
