# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def countTwoDivisor(N):
    num = 0
    while N % 2 == 0:
        N //= 2
        num += 1
    return num, N

def millerrabin(n, x):
    a = x
    if n % 2 == 0 or gcd(a, n) > 1:
        return 1
    k, q = countTwoDivisor(n - 1)
    a = pow(a, q, n)
    if a % n == 1:
        return 0
    for i in range(0, k):
        if a % n == n - 1:
            return 0
        a = pow(a, 2, n)
    print("Composite")
    return 1
    

def p1Factorize(N):
    a = 2
    for i in range(2, int(math.sqrt(N))):
        a = pow(a, i, N)
        d = gcd(a - 1, N)
        if d < N and d > 1:
            print(a, i)
            return d
    return -1
    
if __name__ == "__main__":
    print(p1Factorize(247))