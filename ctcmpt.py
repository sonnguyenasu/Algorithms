import numpy as np

pH = float(input("Enter value of pH: "))
aT = float(input("Enter value of A_T (in muMol*kg-1): ")) #muMol*kg-1
aT = aT*10**(-6)
bT = 0.000416 #total boric acid
kB = 2.53e-9 # dissociation constant of boric acid
kW = 6.06e-14 # dissociation constant of water
k1 = 1.42e-6
k2 = 1.08e-9
fH = 0.7 #activity coeficient of H+ in seawater
hCon = (10**(-pH))/(fH)# [H+]

aC = aT - kB*bT/(kB+hCon) - kW/hCon + hCon #carbonate alkalinity

cT = (aC*hCon/(k1*(hCon + 2*k2))) + (aC*hCon/(hCon+2*k2)) + (aC*k2/(hCon+2*k2))
print("Value of C_T is: {:0.2f}".format(cT), "muMol*kg-1")