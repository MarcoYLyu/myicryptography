#!/usr/bin/env python3
"""This file contains a model of the Lattice

The Lattice class takes in an array of vectors as the basis
for the lattice and generates the lattice accordingly.

    Typical usage example:
        
    bar = [[6513996, 6393464], [66586820, 65354729]]
    foo = Lattice(bar)
    orthogonal_basis = foo.orthogonalize() ## [[-1324 -2376], [ 2280 -1001]]
"""
import math
import numpy as np

class Lattice:
    """The Lattice class
    
    The Lattice class takes in an array of vectors as the basis
    for the lattice and generates the lattice accordingly.
    
    Attributes:
        vecs: A python array of arrays representing the vectors
        of the basis (using row vectors rather than column vectors).
    """
    def __init__(self, vecs):
        """ Initiates Lattice class with an array of arrays  """
        self.basis = np.array(vecs)
        self.length = np.shape(self.basis)[0]
        self.dimension = np.shape(self.basis)[1]

    def is_in_lattice(self, vec):
        """ Determines whether the vector is in the lattice """
        vec = np.array(vec)
        inverse = np.linalg.inv(self.basis)
        coeffs = np.dot(vec, inverse).astype(int)
        res = np.dot(coeffs, self.basis)
        for i in range(len(res)):
            if res[i] != vec[i]:
                return False
        return True

    def hadamard_ratio(self):
        """ Calculates the Hadamard Ratio of the lattice """
        det = np.linalg.det(self.basis)
        divisor = 1
        for itr in self.basis:
            divisor *= self._vec_length(itr)
        return np.power(np.abs(det / divisor), 1.0 / self.length)

    def orthogonalize(self):
        """Returns an orthogonal basis
        
        Applies the Lenstra-Lenstra-Lovasz (LLL) lattice reduction algorithm
        on the basis and returns it. The function does not modify the original
        basis for the lattice.
        
        Returns:
            a numpy-array representing the orthogonal basis in the lattice.
            example:
                
            [[-1324 -2376], [2280 -1001]]
        """
        basis = self.basis.copy()
        k = 1
        while k < self.length:
            basis_gm = basis.copy().astype(float)
            for i in range(k - 1, -1, -1):
                ## Gram Schmidt
                basis_gm[k] = basis_gm[k] - \
                self._projection_length(basis_gm[k], basis_gm[i]) * basis_gm[i]
                ## Gauss' lattice reduction
                basis[k] = basis[k] - round(self._projection_length(basis[k], basis[i])) * basis[i]
            if self._check_lovasz(basis_gm[k], basis_gm[k - 1]):
                ## Lovasz condition
                k += 1
            else:
                ## swap basis[k] with basis[k - 1]
                temp = basis[k].copy()
                basis[k] = basis[k - 1].copy()
                basis[k - 1] = temp
                k = max(k - 1, 1)
        return basis

    ## Helper Functions
    def _vec_length(self, vec):
        res = 0
        for itr in vec:
            res += itr * itr
        return math.sqrt(res)

    def _inner_product(self, vec1, vec2):
        res = 0
        for i in range(len(vec1)):
            res += vec1[i] * vec2[i]
        return res

    def _projection_length(self, vec1, vec2):
        return self._inner_product(vec1, vec2) / self._vec_length(vec2)**2

    def _check_lovasz(self, vec1, vec2):
        lhs = self._vec_length(vec1) ** 2
        rhs = (3.0 / 4 - self._projection_length(vec1, vec2)) * (self._vec_length(vec2) ** 2)
        return lhs >= rhs
