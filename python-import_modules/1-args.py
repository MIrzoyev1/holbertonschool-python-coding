#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")

    for i in range(1, num_args + 1):
        print(f"{i}: {sys.argv[i]}")
        0 arguments.
        1 argument:
1: Hello

