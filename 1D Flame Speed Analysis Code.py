from __future__ import print_function

import cantera as ct
import numpy as np 
import matplotlib.pyplot as plt 

# Simulation Parameters
p = ct.one_atm
Tin = 300.0 
reactants = 'CH4:0.45, O2:1.0, N2:3.76'

width = 0.03 # meters

# Ideal Gas mix object used to compute mixtrure properties
gas = ct.Solution('gri30.xml', 'gri30_mix')
gas.TPX = Tin, p, reactants

gas_H = ct.Solution('H2_mech.cti')
gas_H.TPX = Tin, p, reactants

# Flame Object for gri mech
f = ct.FreeFlame(gas, width=width) 
f.set_refine_criteria(ratio=3, slope=0.07, curve=0.14)

f.solve(loglevel=1, auto=True)

# Flame Object for H2 mech
f1 = ct.FreeFlame(gas_H, width=width)
f1.set_refine_criteria(ratio=3, slope=0.07, curve=0.14)

f1.solve(loglevel=1, auto=True)

plt.subplot(3,1,1)
plt.plot(f1.grid, f1.T)
plt.xlabel('Domain')
plt.ylabel('Temperature')

plt.subplot(3,1,2)
plt.plot(f1.grid, f1.u)
plt.xlabel('Domain')
plt.ylabel('Velocity')

plt.subplot(3,1,3)
plt.plot(f.grid, f.net_rates_of_progress[15,:])
plt.xlabel('Domain')
plt.ylabel('CO2 Production Rate')
plt.show()