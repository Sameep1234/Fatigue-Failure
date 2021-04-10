from scipy.special import erf

from matplotlib import style
import matplotlib.pyplot as plt

import math
import numpy as np


#################################################################################################################################


smax = 220
smin = -smax

#sa = amplitude of the stress wave
sa = (smax - smin)/2

#sm = mean of stress = 0
sm = (smax + smin)/2

# Myu of su 
su = 310

#fatigue strength fraction
f = 0.9

#corrected alternating stress
snf = sa/(1-(sm/su))

#Innovation using external factors

cload = 1

size = 1
if size <= 8:
    csize = 1
elif size > 250:
    csize = 0.6
else:
    csize = 1.189*(size**-0.097)

csurf = 1

temp = 1
if temp <= 450:
    ctemp = 1
elif temp > 550:
    ctemp = 0.1
else:
    ctemp = 1-0.0058*(temp-450)

crel = 1

cmisc = 1

Kt = 0

q = 0

Kf = q*(Kt-1)+1

se = 95

if su < 1400:
    se_ =  (se*cload*csize*csurf*ctemp*crel*cmisc)/Kf
else:
    se_ = 700

#parameter 1 in basquin equation
a = ((f*su)**2)/se_

#parameter 2 in basquin equation
b = (-1/4.35)*math.log10(f*su/se_)

#basquin equation to find cycles to failure
nf = (snf/a)**(1/b)

#################################################################################################################################

#Applied Cycles
n =  nf

sd = nf/10

sdDc = sd/nf

a1 = np.arange(0,n,5000)

meanD = a1/nf

Z = -(1-meanD)/np.sqrt((sdDc**2)+meanD*((sd/nf)**2))

#CDF
cdf =(1.0 +erf(Z/np.sqrt(2)))/2

#Plot graphs
style.use("dark_background")

f1 = plt.figure(figsize=(10,7))
plt.plot(a1,cdf, label= str(sa)+" Mpa", color='#4dffdb', linewidth=1)
plt.plot(a1,cdf, label= str(sa)+" Mpa", color='#4dffdb', linewidth=1)

plt.xlabel("Number of Cycles")
plt.ylabel("Probability of Failure")

plt.show()