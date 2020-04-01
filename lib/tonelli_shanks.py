#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Implements the Tonelli-Shanks Algorithm

"""

import math
import algorithm as algo

def tonelli_shanks(n, p):
    """Tonelli Shanks algorithm
    
    Solves the equation x^2 = n mod p
    
    Args:
        n: an integer representing the base
        p: an integer (prime number)
        
    Returns:
        two integers representing the possible x
        -1, -1 if n is not a quadratic residue of p

    """
    if pow(n, (p - 1) // 2, p) != 1:
        return -1, -1
    
    q, s = algo.decompose_two(p - 1)
    
    z = algo.search_non_residue(p)
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    