# 2022-2023 Programacao 2 LTI
# Grupo 17
# 60260 Guilherme Pinto
# 60262 André Guo

import math

def minkowskiDist(v1, v2, p):
    """
    Minkowski distance
    
    Requires:
    v1 and v2 are equal-dimension lists of numbers,
    representing feature vectors;
    p represents Minkowski order
    Ensures:
    Minkowski distance of order p between v1 and v2
    """
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1.0/p)