#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:19:28 2020

@author: marcolyu
"""
from random import seed
from random import randint

seed(1)

def fma(g, k, p):
    u = g
    y = 1
    while k != 0:
        if k % 2 == 1:
            y = y * u % p
        u = u * u % p
        k //= 2
    return y

class ElgamalPKC:
    def __init__(self, p, g):
        self.publicKey = p
        self.g = g
    
    def getPublicKey(self):
        return self.publicKey
    
    def getG(self):
        return self.g
    
    def getA(self):
        return fma(self.g, self.__secretKey, self.publicKey)
    
    def setSecretKey(self, a):
        self.__secretKey = a
        
    def encrypt(self, m):
        p = self.publicKey
        A = self.getA()
        key = randint(2, p)
            
        c1 = fma(self.g, key, p)
        c2 = (m * fma(A, key, p)) % p
        return c1, c2
    
    def decrypt(self, pair):
        p = self.publicKey
        a = self.__secretKey
        return self.decryptHelper(p, a, pair[0], pair[1])
    
    def decryptHelper(self, p, a, c1, c2):
        return c2 * fma(c1, p - 1 - a, p) % p

def main():
    elgamalPKC = ElgamalPKC(467, 2)
    elgamalPKC.setSecretKey(153)
    print(elgamalPKC.decrypt(elgamalPKC.encrypt(331)))

if __name__ == "__main__":
    main()