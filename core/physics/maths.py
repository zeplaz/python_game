
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_*****************************
@author: matthew
##########################
"""
"""
##########################
maths.py
##########################

##########################
|*  -> some math functions and numpy stuff
##########################
________________________________
@USAGE
::valid FOR:: MIT - UNLESS OTHERWISE OVERWRITTEN

_________________________________//
################

"""
#FOR DEBUG
import sys


import numpy as np

def map_to_pi_range(a):
    while a > np.pi:
        a -=2* np.pi
    while a <  -np.pi:
        a += 2* np.pi
    return a

def compute_ED_matrix_gram(X):
    m,n = X.shape
    G = np.dot(X.T,X)
    H = np.tile(np.diag(G),(n,1))
    return H+H.T -2 * G

def map_to_range(val, a, b, min, max):
    return (b - a)*(val - min)/( max- min) 

def __test__():
    a = map_to_pi_range(24)

    a = np.matrix([[1.2, 2.2], [3.2, a]])
