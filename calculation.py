"""calculate the projected semi-major axis of a star"""

import numpy as np


def get_projected_a(P, Mp, Ms):
    """calculate the projected distance"""
    a = 4*np.pi*P**2*(Mp/(Mp+Ms))
    return a


def get_many_planets(N):
    Mp = np.random.rand(N)*10+0.1
    Ms = np.random.rand(N)*4+1
    P = np.random.rand(N)*9+1
    return P, Mp, Ms
