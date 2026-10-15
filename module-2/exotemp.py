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



if __name__ == '__main__':
    L = float(sys.argv[1])
    d = float(sys.argv[2])
    print(f"{t_eq(L, d):.1f} K")
