#!/usr/bin/python3
def uniq_add(my_list=[]):
    didi = {0: 0}
    res = 0
    for i in my_list:
        didi[i] = i

    for x in didi.keys():
        res += x

    return res
