'''
CODE CREATED BY MEMBERS OF GROUP SM11
1. Sameep Vani AU1940049
2. Malav Doshi AU1040017
3. Kashvi Gandhi AU1940175
4. Kairavi Shah AU1940177
5. Khushi Shah AU1920

'''

from scipy.special import erf

from matplotlib import style
import matplotlib.pyplot as plt

import math
import numpy as np

######################################################################################################################################

#Max and Min Stress
smax = int(input('Smax '))
smin = int(input('Smin '))

#sa = amplitude of the stress wave
sa = (smax - smin)/2

#sm = mean of stress = 0
sm = (smax + smin)/2

#Mean and SD of Su
su = int((input('Mean of Su ')))
sdSu = int(input('SD of Su '))

#Fatigue Strength (f)
f = float(input('Fatigue Strength Fraction (f) '))

#Corrected alternating stress
snf = sa/(1-(sm/su))

#Innovation using external factors

#Loading factor
cload = int(input('Loading Factor (cload) '))

#Diameter
size = int(input('Diameter (size) '))

if size <= 8:
    csize = 1
elif size > 250:
    csize = 0.6
else:
    csize = 1.189*(size**-0.097)

#Surface Finish
csurf = 1
csurf - int(input('Surface Finish (csurf) '))

#Temperature
temp = int(input('Temperature (temp) '))
if temp <= 450:
    ctemp = 1
elif temp > 550:
    ctemp = 0.1
else:
    ctemp = 1-0.0058*(temp-450)

#Reliability
crel = int(input('Reliability (crel) '))

#Miscellanous
cmisc = int(input('Miscellanous '))

#Stress Concentration
Kt = int(input('Stress Concentration (Kt) '))

#Notch Factor
q = int(input('Notch Factor (q) '))

#Final Factor of notch and stress concentration
Kf = q*(Kt-1)+1

#Mean and SD of Se
se = int(input('Mean Se (se) '))
sdSe = int(input('SD Se (sdSe) '))

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

##########################################################################################################################################

#Applied Cycles
print('Please take the following in proportion to cycles to failure = ', math.floor(nf))
n =  int(input('Applied Cycles (n) '))

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