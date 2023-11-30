#!/usr/bin/python3
import sys

num_args = len(sys.argv)

if num_args == 0:
    print("0 arguments.")
else:
    print(f"{num_args} arguments:")

for i, arg in enumerate(sys.argv[1:]):
    print(f"{i + 1}: {arg}")
