# -*- coding: utf-8 -*-
"""
PROJECT EULER

PROBLEM: 25 - 1000-digit Fibonacci number

DESCRIPTION: The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

fib_seq = [1,1]

i = 0
while len(str(fib_seq[-1]))<1000:
    fib_seq.append(sum(fib_seq[-2:]))
    i += 1
    if i % 100 == 0:
        print i,
        
print i + 2