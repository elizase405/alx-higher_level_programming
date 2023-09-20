#!/usr/bin/python3
def best_score(a_dictionary):
    max_v = 0
    max_k = None

    if a_dictionary == None:
        return None

    for k, v in a_dictionary.items():
        if v > max_v:
            max_v = v
            max_k = k
    return max_k
