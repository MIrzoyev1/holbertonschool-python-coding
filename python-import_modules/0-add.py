#!/usr/bin/python:wq
3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
    occurrences = lazy_int(number_of_occurrences("0-add.py", "add_0", case_sensitive=True))
    if occurrences != 1:
        print("Error: number_of_occurrences did not return the correct count.")

