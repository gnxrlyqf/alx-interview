#!/usr/bin/python3
"""makeChange funciton module"""


def makeChange(coins, total):
    """
    Function that returns the fewest number of coins to make a number
    """
    if not coins or coins is None:
        return -1
    result = 0
    new_coins = sorted(coins, key=None, reverse=True)
    for coin in new_coins:
        if total <= 0:
            return int(result)
        mod = total % coin
        result += (total - mod) / coin
        total = mod
    return -1
