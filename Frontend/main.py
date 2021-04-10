#The method that matters is from 870 to 1187
import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

from matplotlib import style

from matplotlib.figure import Figure

from scipy import stats
from scipy.stats import norm
import scipy.special
from scipy.special import erf


import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np

from scipy.optimize import fsolve


smax = 220
smin = -smax

#sa = amplitude of the stress wave
sa = (smax - smin)/2

#sm = mean of stress = 0
sm = (smax + smin)/2  #doubt

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

a = ((f*su)**2)/se_
b = (-1/4.35)*math.log10(f*su/se_)


# self.entrynf.delete(0, 'end')
# self.entrynf.insert(0, int(nf))


nf = (snf/a)**(1/b)

x1 = ([1,1000000, 1000000000])
y1 = ([su, se, se_])

x2 =([1, nf])
y2 = ([snf, snf])


#######################################################################################



n =  nf
sd = nf/10

sdDc = sd/nf

a1 = np.arange(0,n,5000)

meanD = a1/nf

print("type of: ", type(meanD))
print('meanD ', meanD[0])

Z = -(1-meanD)/np.sqrt((sdDc**2)+meanD*((sd/nf)**2))

#CDF
pof1 =(1.0 +erf(Z/np.sqrt(2)))/2

style.use("dark_background")

f1 = plt.figure(figsize=(10,7))
plt.plot(a1,pof1, label= str(sa)+" Mpa", color='#4dffdb', linewidth=1)

plt.xlabel("Number of Cycles")
plt.ylabel("Probability of Failure")

# ax = plt.subplot(111)

plt.show()









'''
smax = 220
smin = 0

sa = (smax - smin)/2
sm = (smax + smin)/2  #doubt

su = 310
f = 0.9

snf = sa/(1-(sm/su))  

se = 95

a = ((f*su)**2)/se_
b = (-1/4.35)*math.log10(f*su/se_)

nf = (snf/a)**(1/b)

x1 = ([1,1000000, 1000000000])
y1 = ([su, se, se_])

x2 =([1, nf])
y2 = ([snf, snf])

n =  nf
sd = nf/10

sdDc = sd/nf

a1 = np.arange(0,n,5000)

meanD = a1/nf

Z = -(1-meanD)/np.sqrt((sdDc**2)+meanD*((sd/nf)**2))
pof1 =(1.0 +erf(Z/np.sqrt(2)))/2

print(pof1.shape)
style.use("dark_background")

f1 = plt.figure(figsize=(10,7))
plt.plot(a1,pof1, label= str(sa)+" Mpa", color='#4dffdb', linewidth=1)

plt.xlabel("Number of Cycles")
plt.ylabel("Probability of Failure")

ax = plt.subplot(111)

plt.show()

'''
