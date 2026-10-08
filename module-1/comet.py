# This script with a function takes the known constants for a sublimating comet problem with an input from user for radius
# and uses differentiation, and the relation between delta mass, H_sol, and h_ice to calculate how much radius is lost in meters 
# per orbit. The functinon returns these values and the script prints delta radius and the life of the comet.
# You can access this by using "python comet.py" in the terminal with the same working directory or by calling the
# function individually using "from comet.py import dr_per_orbit" in the correct working directory 



from math import sqrt, pi 

# take radius as input from user
R = float(input("raidus (meters): "))

# constants
A = 0
a = 3.12 * (1.49e11) # m
P = 500 # kg/m^3
e = 0.5
L = 3.8e26 # J/s
GM = 1.3271e20 # m^3/s^2
h_ice = 2.5e6 # J/kg

# function that calculates delta radius given R, A, P, a, e, constants and returns it
def dr_per_orbit(R, A, P, a, e):
    H_sol = (pi/2)*(1-A)*(R**2)*(L/(sqrt(GM)))*(1/(sqrt(a*(1-(e**2)))))
    dm = H_sol/h_ice
    dr = dm/(4*pi*(R**2)*P)
    return dr

# printing result from dr_per_orbit function by assigning a variable dr_result to what the function returns
dr_result = dr_per_orbit(R, A, P, a, e)
print(f"Radius lost per orbit (delta radius): {dr_result: .2f}m")

# comet life, orbits, calculation and printing
comet_life = R / dr_result
print(f"comet_life: {comet_life: .0f} orbits")