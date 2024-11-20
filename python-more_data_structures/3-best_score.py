#!/usr/bin/python3
def best_score(a_dictionary):
    """ Return the key with the highest integer value in the dictionary """
    if not a_dictionary:
        return None

    best_key = None
    best_value = -float('inf')

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
