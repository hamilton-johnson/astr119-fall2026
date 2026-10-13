# cometlife_ref.py -- how many orbits does a sublimating comet have left?
# Reference version of the Pod 0 program, used in Pod 1B. Everything in SI units.
# Pod 1B works on a copy of this file (cometlife.py). Leave this one as it is, so you can always go back to it.
import sys
from math import sqrt, pi

L = 3.8e26          # solar luminosity, J/s
GM = 1.3271e20      # G times the Sun's mass, m^3/s^2
h_ice = 2.5e6       # energy to sublimate 1 kg of ice, J/kg
AU = 1.49e11        # meters per AU

R = float(sys.argv[1])         # comet radius, m (2 km)
rho = 500.0         # comet density, kg/m^3
A = float(sys.argv[2])   # albedo, read from the command line (second argument)
a = 3.12 * AU       # semi-major axis, m
e = 0.5             # eccentricity

H_sol = (pi / 2) * (1 - A) * R**2 * L / sqrt(GM) / sqrt(a * (1 - e**2))   # J absorbed per orbit
dM = H_sol / h_ice                                                       # kg lost per orbit
dr = dM / (4 * pi * rho * R**2)                                          # m of radius lost per orbit

print("dr =", dr, "m per orbit")
print("orbits left =", R / dr)

# TODO(human): compute the comet's lifetime with Kepler's third law
#   1. P = the orbital period in years, using P = a**1.5 (careful: a must be in AU here)
#   2. lifetime = how many years the comet lasts (orbits left times the period)
#   3. death_year = the year the comet runs out of ice, starting from 2026

P = (a / AU) ** 1.5
lifetime = P * (R / dr)
death_year = 2026 + lifetime
print(f"period = {P:.2f} years")
print(f"the comet lasts about {lifetime:.0f} years and dies around the year {death_year:.0f}")
print(f"Mark your calendar for {death_year:.0f}: bring snacks, the comet won't.")
