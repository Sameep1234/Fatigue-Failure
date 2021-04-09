#The method that matters is from 870 to 1187
import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

import matplotlib.animation as animation
from matplotlib import style

from matplotlib.figure import Figure

import matplotlib.dates as mdates
import matplotlib.ticker as mticker

from scipy import stats
from scipy.stats import norm
import scipy.special
from scipy.special import erf


import numpy as np
import matplotlib.pyplot as plt
import math

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import numpy as np

import pylab
from pylab import *

from scipy.optimize import fsolve



############################################################################################################################
# class Deterministic(tk.Frame):

#     def calculatecycles(self):
#             smax = 220
#             smin = 0

#             sa = (smax - smin)/2
#             sm = (smax + smin)/2

#             su = [310, 15]
#             f = 0.9

#             snf = sa/(1-(sm/su))

#             cload = 1

#             size = 1
#             if size <= 8:
#                 csize = 1
#             elif size > 250:
#                 csize = 0.6
#             else:
#                 csize = 1.189*(size**-0.097)

#             csurf = 1

#             temp = 1
#             if temp <= 450:
#                 ctemp = 1
#             elif temp > 550:
#                 ctemp = 0.1
#             else:
#                 ctemp = 1-0.0058*(temp-450)

#             crel = 1

#             cmisc = 1

#             Kt = 0

#             q = 0

#             Kf = q*(Kt-1)+1

#             se = [95,5]

#             if su < 1400:
#                 se_ =  (se*cload*csize*csurf*ctemp*crel*cmisc)/Kf
#             else:
#                 se_ = 700

#             a = ((f*su)**2)/se_
#             b = (-1/4.35)*math.log10(f*su/se_)

#             nf = (snf/a)**(1/b)
#             # self.entrynf.delete(0, 'end')
#             # self.entrynf.insert(0, int(nf))

#             x1 = ([1,1000000, 1000000000])
#             y1 = ([su, se, se_])
#             plt.semilogx(x1,y1, color='r', linewidth=5)

#             x2 =([1, nf])
#             y2 = ([snf, snf])
#             markers_on = [1,2,3]
#             plt.semilogx(x2, y2, color='g',marker='s',markersize=12,  linewidth=5)
#             print("Hi")
#             plt.axis([0,1000000000,0,1000])
#             plt.show()

# KKAAMMMMM NU FUNCTIONNNNNNNNNNNNN
    # def calculatedamage(self):
    #     try:
    #         float(self.entryn.get())
    #         float(self.entrynf.get())

    #     except ValueError:
    #         errormsg("MASUKIN ANGKANNA LAH LEK")
    #         print("")

    #     else:
    #         n =  float(self.entryn.get())
    #         nf = float(self.entrynf.get())
    #         D = n/nf
    #         self.entrydam.delete(0, 'end')
    #         self.entrydam.insert(0, "%.3f" % D)






############################################################################################################################








smax = 220
smin = 0

sa = (smax - smin)/2
sm = (smax + smin)/2

su = 310
f = 0.9

snf = sa/(1-(sm/su))

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
plt.semilogx(x1,y1, color='r', linewidth=5)

x2 =([1, nf])
y2 = ([snf, snf])
markers_on = [1,2,3]
plt.semilogx(x2, y2, color='g',marker='s',markersize=12,  linewidth=5)
plt.xlabel("Number of Cycles")
plt.ylabel("Probability of Failure")
plt.axis([0,1000000000,0,1000])
plt.show()