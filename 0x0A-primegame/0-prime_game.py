#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Prime game function
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    ben = 0
    maria = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        mul_rm(a, i)
    for num in nums:
        if sum(a[0:num + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def mul_rm(list, x):
    """
    removes prime multiples
    """
    for num in range(2, len(list)):
        try:
            list[num * x] = 0
        except (ValueError, IndexError):
            break
