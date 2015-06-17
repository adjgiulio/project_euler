# -*- coding: utf-8 -*-
"""
PROJECT EULER

PROBLEM: 30 - Digit fifth powers

DESCRIPTION: Surprisingly there are only three numbers that
can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as
the sum of fifth powers of their digits.
"""

list_pow = []
for i in range(2,10000000):
    n = sum([int(k)**5 for k in str(i)])
    if i == n:
        list_pow.append(n)
        
print sum(list_pow)