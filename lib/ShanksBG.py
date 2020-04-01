#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:41:44 2020

@author: marcolyu
"""

import math
import numpy as np

def stepsHelper(start, multiplier, n, p):
    res = [0 for i in range(n + 1)]
    res[0] = start
    for i in range(1, n + 1):
        res[i] = res[i - 1] * multiplier % p
    return res

def inverseMod(x, p):
    return pow(x, p - 2, p)

def findMatch(list1, list2):
    """
    Input:
        list1: unsorted list (index matters)
        list2: unsorted list (index matters)
    Output:
        i, j: i is the index of the matched element in list1, j in list2
    """
    iniArr1 = np.array(list1)
    iniArr2 = np.array(list2)
    
    outIndArr1 = np.argsort(iniArr1)
    outIndArr2 = np.argsort(iniArr2)
    
    outArr1 = iniArr1[outIndArr1]
    outArr2 = iniArr2[outIndArr2]
    
    i, j = 0, 0
    while i != len(list1) and j != len(list2):
        if outArr1[i] == outArr2[j]:
            return outIndArr1[i], outIndArr2[j]
        elif outArr1[i] > outArr2[j]:
            j += 1
        else:
            i += 1
    return -1, -1

def shanks(g, h, N, p):
    """
    Input:
        g: g \in G of order N \geq 2
        h: base
        N: order of g in G
        p: prime number mod
    Output:
        i, j: x = i + jn
    """
    
    n = 1 + int(math.sqrt(N))
    babystep = stepsHelper(1, g, n, p)
    giantstep = stepsHelper(h, inverseMod(babystep[n], p), n, p)
    a, b = findMatch(babystep, giantstep)
    print(a + n * b)
    return a, b
    
def main():
    
    g = int(input())
    h = int(input())
    p = int(input())
    N = int(input())
    print("%d + %dn" % (shanks(g, h, N, p)))
    return 0

if __name__ == "__main__":
    main()

