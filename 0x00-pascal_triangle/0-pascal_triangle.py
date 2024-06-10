#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    if n == 0:
        return []
    else:
        result = pascal_triangle(n - 1)
        current_row = [1]
        last_row = result[-1]

        for i in range(len(last_row) - 1):
            current_row.append(last_row[i] + last_row[i + 1])

        current_row.append(1)
        result.append(current_row)

        return result
