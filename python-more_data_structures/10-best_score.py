#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_value = 0
    max_key = ''
    for i in a_dictionary.keys():
        if a_dictionary[i] > max_value:
            max_key = i
    return max_key
