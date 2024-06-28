#!/usr/bin/python3
"""
definition of pascal triangle funciton
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal`s triangle
    return:
        two dimensional list of integers
    """
    arr = []
    if n <= 0:
        return arr
    arr = [[1]]
    for i in range(1, n):
        subarr = [1]
        end = len(arr[i - 1])
        for j in range(end - 1):
            current = arr[i - 1][j] + arr[i - 1][j + 1]
            subarr.append(current)
        subarr.append(1)
        arr.append(subarr)
    return arr
