#!/usr/bin/env python3
"""Implements the Elgamal Public Key Cryptography

Depends on the hardness of Diffie Hellman Problem.
Example:
    
    >>> elgamal_pkc = ElgamalPKC(467, 2)
    >>> elgamal_pkc.set_secret_key(153)
    >>> elgamalPKC.decrypt(elgamalPKC.encrypt(331)))
    331

"""
from random import seed
from random import randint
import algorithm as algo

seed(1)

class ElgamalPKC:
    def __init__(self, p, g):
        self.public_key = p
        self.g = g
    
    def get_public_key(self):
        return self.public_key
    
    def get_g(self):
        return self.g
    
    def get_a(self):
        return algo.fast_modular_multiply(self.g, self._secret_key, self.public_key)
    
    def set_secret_key(self, a):
        self._secretKey = a
        
    def encrypt(self, m):
        p = self.publicKey
        A = self.getA()
        key = randint(2, p)
            
        c1 = algo.fast_modular_multiply(self.g, key, p)
        c2 = (m * algo.fast_modular_multiply(A, key, p)) % p
        return c1, c2
    
    def decrypt(self, pair):
        p = self.publicKey
        a = self._secretKey
        return self.decryptHelper(p, a, pair[0], pair[1])
    
    def decryptHelper(self, p, a, c1, c2):
        return c2 * algo.fast_modular_multiply(c1, p - 1 - a, p) % p

def main():
    elgamalPKC = ElgamalPKC(467, 2)
    elgamalPKC.setSecretKey(153)
    print(elgamalPKC.decrypt(elgamalPKC.encrypt(331)))

if __name__ == "__main__":
    main()