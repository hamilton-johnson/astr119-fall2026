dist_au = [1.0, 1.52, 0.72]
print(dist_au * 2) # just repeats the entries by 2

import numpy as np

dist_au_array = np.array(dist_au)

print(dist_au_array * 2)

def mass(radius):
    '''estimate the mass of the planet of radius, "raidus"'''
    rho = 2 # g per cm^3
    volume = (4/3)*np.pi*(radius**3) # compute the volume based on radius
    mass_g = rho * volume
    return mass_g

print(mass(1e9))

r = np.array([2.4e8, 6e8, 7e9]) # convert a list to an array
print(mass(r))

masses = mass(r)
mass_condition = masses > 1e27

print(mass_condition)

names = np.array(['mercury', 'earth', 'jupiter'])
print(names[masses > 1e27])
print(masses.mean())