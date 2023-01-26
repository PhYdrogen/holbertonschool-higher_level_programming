#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sort_dict = sorted(a_dictionary.items())
    return (sort_dict[-1][0])
