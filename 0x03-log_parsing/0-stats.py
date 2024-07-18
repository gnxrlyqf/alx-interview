#!/usr/bin/python3
"""
    Task 0
"""

import sys
import re


def stats(codes, size):
    """
    Prints code dictionary after each 10
    Args:
        codes: dictionary of status code count
        size: total file size
    """
    print("File size: {}".format(size))
    for k, v in sorted(codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


count = 0
size = 0
codes = {"200": 0,
         "301": 0,
         "400": 0,
         "401": 0,
         "403": 0,
         "404": 0,
         "405": 0,
         "500": 0}

ip = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
datetime = r'(\[(\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2}:\d{2}\.\d{6})\])'
request = r'"GET \/projects\/260 HTTP\/1\.1"'
code = r'(\d{3})'
bytes = r'(\d+)'

pattern = rf'{ip}\s-\s{datetime}\s{request}\s{code}\s{bytes}'

try:
    for line in sys.stdin:
        match = re.match(pattern, line)
        if match:
            codes[match.group(5)] += 1
            count += 1
            size += int(match.group(6))
            if count == 10:
                stats(codes, size)
                count = 0
finally:
    stats(codes, size)
