#!/usr/bin/python3

import sys


def print_msg(codes, size):
    """
    Method to print
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
        parsed = line.split()
        if len(parsed) > 2:
            counter += 1
            if counter <= 10:
                size += int(parsed[-1])
                if (parsed[-2] in codes.keys()):
                    codes[parsed[-2]] += 1
            if (counter == 10):
                print_msg(codes, size)
                counter = 0

finally:
    print_msg(codes, size)
