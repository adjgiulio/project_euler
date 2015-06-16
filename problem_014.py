# -*- coding: utf-8 -*-
"""
PROJECT EULER

PROBLEM: 14 - Longest Collatz sequence

DESCRIPTION: The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def lcs(n):
    s = [n]
    l = n
    while l != 1:
        if l % 2 == 0:
            l = l/2
            
        else:
           l = 3*l + 1
        
        s.append(l)
    return s

maxn = 0 
maxl = 0       
for i in range(1,1000000):
    newl = len(lcs(i))
    if newl > maxl:
        maxn = i
        maxl = newl
    if i % 100 == 0:
        print i,
        
print maxn