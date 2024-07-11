#!/usr/bin/python3
"""
    Calculate minimum operations to copy and paste H n times
"""


def minOperations(n):
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
            divisor -= 1
        divisor += 1
    return operations
