#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:08:32 2020

@author: marcolyu
"""

import math

def factor_two(p):
    k = 0
    while p % 2 == 0:
        k += 1
        p //= 2
    return p, k

def gcd(a, b):
    """greatest common divisor
    
    Calculates the greatest common divisor with
    Euclidean algorithm.
    example:
        
        val = gcd(33, 6)
        print(val) ## 3
    
    Args:
        a: an int representing the first argument
        b: an int representing the second argument
    
    Returns:
        an int representing the greatest common divisor
    """
    if (a < b):
        a, b = b, a
    temp = -1
    while a % b != 0:
        temp = a
        a = b
        b = temp % b
    return b

def find_first_divisor(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return i
    return N

def euler_phi(N):
    result = N
    divisor = 1
    p = find_first_divisor(N)
    while p != N:
        while N % p == 0:
            N //= p
        result *= p - 1
        divisor *= p
        p = find_first_divisor(N)
    if p != 1:
        return result * (p - 1) // (divisor * p)
    else:
        return result // divisor
    
if __name__ == "__main__":
    print(euler_phi(33))
    
    