#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i == j or (i == 1 and j == 0):
            continue
        if i == 1 and j < 2:
            continue
        if i == 2 and j < 3:
            continue
        if i == 3 and j < 4:
            continue
        if i == 4 and j < 5:
            continue
        if i == 5 and j < 6:
            continue
        if i == 6 and j < 7:
            continue
        if i == 7 and j < 8:
            continue
        if i >= 8 and j < 10:
            continue
        print("{0}{1}, ".format(i, j), end="")
print("{89}")
