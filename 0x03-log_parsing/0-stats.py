#!/usr/bin/python3

import sys


def print_msg(codes, size):
    """
    Prints code dictionary after each 10
    Args:
        codes: dictionary of codes
        size: total size of the files
    Returns:
        Nothing
    """

    print("File size: {}".format(size))
    for k, v in sorted(codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


size = 0
count = 0
codes = {"200": 0,
         "301": 0,
         "400": 0,
         "401": 0,
         "403": 0,
         "404": 0,
         "405": 0,
         "500": 0}

try:
    for line in sys.stdin:
        parsed = line.split()[::-1] 
        if len(parsed) > 2:
            counter += 1
            if counter <= 10:
                size += int(parsed[0])
                if (parsed[1] in codes.keys()):
                    codes[parsed[1]] += 1
            if (counter == 10):
                print_msg(codes, size)
                counter = 0

finally:
    print_msg(codes, size)
