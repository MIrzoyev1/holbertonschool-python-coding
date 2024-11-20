#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    if my_dict is not None:
        keys = sorted(my_dict.keys())
        for key in keys:
            print(f"{key}: {my_dict[key]}")
