#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_array = []
    for i in my_list:
        if i == search:
            new_array.append(replace)
        else:
            new_array.append(i)
    return new_array
