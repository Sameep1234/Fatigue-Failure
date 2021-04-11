'''
CODE CREATED BY MEMBERS OF GROUP SM11
1. Sameep Vani AU1940049
2. Malav Doshi AU1040017
3. Kashvi Gandhi AU1940175
4. Kairavi Shah AU1940177
5. Khushi Shah AU1920171

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
f = 0.9
#Corrected alternating stress
sm = 0
sa = 220
su = 310
snf = sa/(1-(sm/su))

# #Innovation using external factors

# #Loading factor
# cload = int(input('Loading Factor (cload) '))

# #Diameter
# size = int(input('Diameter (size) '))

# if size <= 8:
#     csize = 1
# elif size > 250:
#     csize = 0.6
# else:
#     csize = 1.189*(size**-0.097)

# #Surface Finish
# csurf = 1
# csurf - int(input('Surface Finish (csurf) '))

# #Temperature
# temp = int(input('Temperature (temp) '))
# if temp <= 450:
#     ctemp = 1
# elif temp > 550:
#     ctemp = 0.1
# else:
#     ctemp = 1-0.0058*(temp-450)

# #Reliability
# crel = int(input('Reliability (crel) '))

# #Miscellanous
# cmisc = int(input('Miscellanous '))

# #Stress Concentration
# Kt = int(input('Stress Concentration (Kt) '))

# #Notch Factor
# q = int(input('Notch Factor (q) '))

# #Final Factor of notch and stress concentration
# Kf = q*(Kt-1)+1

#Mean and SD of Se
se = int(input('Mean Se (se) '))
sdSe = int(input('SD Se (sdSe) '))

# if su < 1400:
#     se_ =  (se*cload*csize*csurf*ctemp*crel*cmisc)/Kf
# else:
#     se_ = 700
se_ = se
#parameter 1 in basquin equation
se_ = 95
a = ((f*su)**2)/se_

#parameter 2 in basquin equation
b = (-1/4.35)*math.log10(f*su/se_)

#basquin equation to find cycles to failure
nf = (snf/a)**(1/b)

#######################################################################################################

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
su = 240

#Fatigue Strength (f)
f = float(input('Fatigue Strength Fraction (f) '))
f = 0.9

#Corrected alternating stress
sa = 160
sm = 0
snf1 = sa/(1-(sm/su))

# #Innovation using external factors

# #Loading factor
# cload = int(input('Loading Factor (cload) '))

# #Diameter
# size = int(input('Diameter (size) '))

# if size <= 8:
#     csize = 1
# elif size > 250:
#     csize = 0.6
# else:
#     csize = 1.189*(size**-0.097)

# #Surface Finish
# csurf = 1
# csurf - int(input('Surface Finish (csurf) '))

# #Temperature
# temp = int(input('Temperature (temp) '))
# if temp <= 450:
#     ctemp = 1
# elif temp > 550:
#     ctemp = 0.1
# else:
#     ctemp = 1-0.0058*(temp-450)

# #Reliability
# crel = int(input('Reliability (crel) '))

# #Miscellanous
# cmisc = int(input('Miscellanous '))

# #Stress Concentration
# Kt = int(input('Stress Concentration (Kt) '))

# #Notch Factor
# q = int(input('Notch Factor (q) '))

# #Final Factor of notch and stress concentration
# Kf = q*(Kt-1)+1

#Mean and SD of Se
se = int(input('Mean Se (se) '))
sdSe = int(input('SD Se (sdSe) '))

# if su < 1400:
#     se_ =  (se*cload*csize*csurf*ctemp*crel*cmisc)/Kf
# else:
#     se_ = 700
se_ = se
#parameter 1 in basquin equation
a1 = ((f*su)**2)/se_

#parameter 2 in basquin equation
b1 = (-1/4.35)*math.log10(f*su/se_)

#basquin equation to find cycles to failure
nf1 = (snf1/a1)**(1/b1)



#############################################################################################################
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

sa = 250
sm = 0
su = 395
#Corrected alternating stress
snf2 = sa/(1-(sm/su))

# #Innovation using external factors

# #Loading factor
# cload = int(input('Loading Factor (cload) '))

# #Diameter
# size = int(input('Diameter (size) '))

# if size <= 8:
#     csize = 1
# elif size > 250:
#     csize = 0.6
# else:
#     csize = 1.189*(size**-0.097)

# #Surface Finish
# csurf = 1
# csurf - int(input('Surface Finish (csurf) '))

# #Temperature
# temp = int(input('Temperature (temp) '))
# if temp <= 450:
#     ctemp = 1
# elif temp > 550:
#     ctemp = 0.1
# else:
#     ctemp = 1-0.0058*(temp-450)

# #Reliability
# crel = int(input('Reliability (crel) '))

# #Miscellanous
# cmisc = int(input('Miscellanous '))

# #Stress Concentration
# Kt = int(input('Stress Concentration (Kt) '))

# #Notch Factor
# q = int(input('Notch Factor (q) '))

# #Final Factor of notch and stress concentration
# Kf = q*(Kt-1)+1

#Mean and SD of Se
se = int(input('Mean Se (se) '))
sdSe = int(input('SD Se (sdSe) '))

# if su < 1400:
#     se_ =  (se*cload*csize*csurf*ctemp*crel*cmisc)/Kf
# else:
#     se_ = 700

#parameter 1 in basquin equation
se_ = se
se_ = 110
f = 0.9

a2 = ((f*su)**2)/se_

#parameter 2 in basquin equation
b2 = (-1/4.35)*math.log10(f*su/se_)

#basquin equation to find cycles to failure
nf2 = (snf2/a2)**(1/b2)

##########################################################################################################################################

#Applied Cycles
maximum = max(max(nf1, nf2), nf)
# maximum = max(nf, nf1)
print('Please take the following in proportion to cycles to failure = ', math.floor(maximum))
n =  int(input('Applied Cycles (n) '))

sd = nf/10
sd1 = nf1/10
sd2 = nf2/10

sdDc = sd/nf
sdDc1 = sd1/nf1
sdDc2 = sd2/nf2

a1 = np.arange(0,n,5000)

meanD = a1/nf
meanD1 = a1/nf1
meanD2 = a1/nf2

Z = -(1-meanD)/np.sqrt((sdDc**2)+meanD*((sd/nf)**2))
Z1 = -(1-meanD1)/np.sqrt((sdDc1**2)+meanD*((sd1/nf1)**2))
Z2 = -(1-meanD2)/np.sqrt((sdDc2**2)+meanD*((sd2/nf2)**2))

#CDF
cdf =(1.0 +erf(Z/np.sqrt(2)))/2
cdf1 =(1.0 +erf(Z1/np.sqrt(2)))/2
cdf2 =(1.0 +erf(Z2/np.sqrt(2)))/2

#Plot graphs
# style.use("dark_background")

f1 = plt.figure(figsize=(10,7))
plt.plot(a1,cdf, label = "Boeing 787 Dreamliner", linewidth=1)
plt.plot(a1,cdf1, label = "Boeing 747", linewidth=1)
plt.plot(a1,cdf2, label = "Boeing 777", linewidth=1)

plt.xlabel("Number of Cycles")
plt.ylabel("Probability of Failure")

plt.legend()

plt.show()