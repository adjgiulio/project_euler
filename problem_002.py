# -*- coding: utf-8 -*-
"""
PROJECT EULER

PROBLEM: 2 - Even Fibonacci numbers

DESCRIPTION: Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


fib_seq = [1, 2]
next_fib = 0
while next_fib <= 4000000:
    next_fib = sum(fib_seq[-2:])
    fib_seq.append(next_fib)
print sum([k for k in fib_seq if k % 2 == 0])