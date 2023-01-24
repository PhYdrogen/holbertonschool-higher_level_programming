#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_value = 0
    max_key = ''
    for key in a_dictionary.keys():
        if a_dictionary[key] > max_value:
            max_key = key
            max_value = a_dictionary[key]
    return max_key
