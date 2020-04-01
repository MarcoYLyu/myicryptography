#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 08:59:39 2020

@author: marcolyu
"""

import math

def factorTwo(p):
    """
    factorize p - 1 = q * 2^s
    """
    k = 0
    while p % 2 == 0:
        k += 1
        p //= 2
    return p, k

def searchNonResidue(p):
    for z in range(2, p):
        if pow(z, (p - 1) // 2, p) == p - 1:
            return z
    return -1

def tonelliShanks(p, n):
    """
    Solve the equation x^2 = n mod p
    """
    if pow(n, (p - 1) // 2, p) != 1:
        return -1, -1
    
    q, s = factorTwo(p - 1)
    
    z = searchNonResidue(p)
    
    if z == -1:
        return -1, -1
    
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)
    
    while t != 1:
        i = 0
        div = False
        while (not div):
            i += 1
            t = int(math.pow(t, 2)) % p
            if (t % p == 1):
                div = True
        b = pow(c * c, m - i - 1, p)
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p
        m = i
    
    return r, p - r

if __name__ == "__main__":
    arr = [i for i in range(2, 12)]
    n = 247
    """
    template = "The solution of x^2 = {0} (mod {1}) are r_1 = {2}, r_2 = {3}"
    for p in arr:
        r1, r2 = tonelliShanks(p, n)
        if (r1 == -1 and r2 == -1):
            print("No Solution for", p)
        else:
            print(template.format(n, p, r1, r2))
    """
    print(tonelliShanks(3, n))

    res = [i for i in range(23, 39)]
    nums = [T * T - n for T in range(23, 39)]
    arrowres = ""
    for p in range(2, 13):
        arrowres = ""
        r1, r2 = tonelliShanks(p, n)
        if r1 == -1 and r2 == -1:
            continue
        for itr in res:
            print(itr, p, r1, r2)
            if itr % p == r1 or itr % p == r2:
                arrowres += "$\\downarrow {0}$ ".format(p)
            arrowres += "& "
        arrowres += "\\\\"
        print(arrowres)
        print()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    