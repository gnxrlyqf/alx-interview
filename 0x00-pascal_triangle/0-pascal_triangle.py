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
    list = []
    if n <= 0:
        return list
    list = [[1]]
    for i in range(1, n):
        sublist = [1]
        end = len(list[i - 1])
        for j in range(end - 1):
            current = list[i - 1][j] + list[i - 1][j + 1]
            sublist.append(current)
        sublist.append(1)
        list.append(sublist)
    return (list)
