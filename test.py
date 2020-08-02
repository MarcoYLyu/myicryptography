#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:00:11 2020

@author: marcolyu
"""

import myicrypto as algo

bar = [[6513996, 6393464], [66586820, 65354729]]
foo = algo.Lattice(bar)
orthogonal_basis = foo.orthogonalize()

pkc = algo.crypto.ElgamalPKC(467, 2)
pkc.set_secret_key(153)
print(pkc.decrypt(pkc.encrypt(331)))