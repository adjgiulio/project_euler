# -*- coding: utf-8 -*-
"""
PROJECT EULER

PROBLEM: 21 - Amicable numbers

DESCRIPTION: Let d(n) be defined as the sum of proper divisors of 
n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def sum_div(n):
    div_list = []
    for i in range(1,n):
        if n % i == 0:
            div_list.append(i)
    return sum(div_list)

list_amicable = []    
for i in range(1,10000):
    amicable = sum_div(i)
    if (sum_div(amicable) == i) & (amicable != i):
        list_amicable.append(i)
    if i % 10 == 0:
        print i,

print sum(list_amicable)