#!/usr/bin/python3
def no_c(my_string):
    string_no_c = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        string_no_c = string_no_c + "{}".format(char)
    return string_no_c
