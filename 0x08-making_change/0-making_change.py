#!/usr/bin/python3
"""makeChange funciton module"""


def makeChange(coins, total):
    """
    Function that returns the fewest number of coins to make a number
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    result = 0
    new_coins = sorted(coins, key=None, reverse=True)
    for coin in new_coins:
        mod = total % coin
        result += (total - mod) / coin
        if mod == 0:
            return int(result)
        total = mod
    return -1
