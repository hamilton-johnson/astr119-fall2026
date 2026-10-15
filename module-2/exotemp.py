import sys

from scipy.constants import sigma  # Stefan-Boltzmann constant, W m^-2 K^-4
import numpy as np


def t_eq(L, d):
    """Equilibrium temperature of a planet with zero albedo.

    L : luminosity of the star, in watts
    d : star-planet distance, in meters
    Returns the temperature in kelvin.
    """

    # TODO(human):
    # 1. Compute the denominator 16 * pi * sigma * d**2  (use np.pi)
    # 2. Divide L by that denominator
    # 3. Take the fourth root of the result (** 0.25)
    # 4. Return it

    denominator = 16 * np.pi * sigma * d**2
    result = L / denominator
    return result ** 0.25

planets = [   # name, luminosity (solar units), distance (AU)
    ["Earth",        1.0,     1.000],
    ["Mars",         1.0,     1.524],
    ["HD 209458 b",  1.6,     0.047],
    ["51 Peg b",     1.3,     0.052],
    ["TRAPPIST-1 e", 0.00055, 0.029],
    ["Kepler-22 b",  0.79,    0.85],
    ["55 Cnc e",     0.58,    0.0154],
    ["HD 189733 b",  0.34,    0.031],
    ["Kepler-452 b", 1.2,     1.046],
    ["Proxima b",    0.0016,  0.0485],
]

if __name__ == '__main__':
    L = float(sys.argv[1])
    d = float(sys.argv[2])
    print(f"{t_eq(L, d):.1f} K")
