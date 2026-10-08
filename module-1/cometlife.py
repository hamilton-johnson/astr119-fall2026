from math import sqrt, pi
# constants
R = 1000 # m
A = 0
a = 3.12 * (1.49e11) # m
P = 500 # kg/m^3
e = 0.5
L = 3.8e26 # J/s
GM = 1.3271e20 # m^3/s^2
h_ice = 2.5e6 # J/kg

#expressions
def dr_per_orbit(R, A, P, a, e):
    H_sol = (pi/2)*(1-A)*(R**2)*(L/(sqrt(GM)))*(1/(sqrt(a*(1-(e**2)))))
    dm = H_sol/h_ice
    dr = dm/(4*pi*(R**2)*P)
    return dr

dr_result = dr_per_orbit(R, A, P, a, e)
print(dr_result)