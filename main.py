import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import fsolve
import random
# import sympy as sym

'''
CODE CREATED BY MEMBERS OF #SM11
1. Sameep Vani AU1940049
2. Malav Doshi AU1940017
3. Kashvi Gandhi AU1940175
4. Kairavi Shah AU1940177
5. Khushi Shah AU1920171

List of functions created
1. multiplyTwoMatrices(A, B)
2. getNorm(A)
3. getNormalisedVector(vector)
4. getTranspose(A)
5. multiplyScalarToVector(scale, vect)
6. findQR(A)
7. getEigenValues(A)
8. getSingularValues(A)
9. calculateSVD(eValues, eVectors, sv)

List of inbuilt libraries/functions used
1. PIL for image reading
2. Matplotlib for showing the result
3. numpy.linalg for checking the answers

'''
n = 150000
myu1 = 310
sigma1 = 15
myu2 = 95
sigma2 = 5
Sa = 220
f = 0.9
Snf = Sa
Su = 311
Se = 100
print("Su ", Su, " Se ", Se) 

# for i in range(0, 100):
#     x.append(random.randInt(1, n))
#     y.append(random.randInt(1, n))

    
PI = math.pi
e = 2.718281828459045
temp = (-1*((Su - myu1)**2) / 2*(sigma1**2))
print("answer" , temp)
pdfSu = math.exp(temp)
print("LOCHO=" , pdfSu)
print ("answer" , temp)
print(pdfSu)
pdfSu = pdfSu/math.sqrt(2*PI*(sigma1**2))
print("ASONMGIDAFN: ", -1*((Se - myu2)**2)/2*sigma2**2)
pdfSe = (1/math.sqrt(2*PI*sigma2**2))*(e**(-1*((Se - myu2)**2)/2*sigma2**2))
print(pdfSu, pdfSe)
U1 = (pdfSu - myu1)/sigma1
U2 = (pdfSe - myu2)/sigma2

print("U1 ", U1, " U2 ", U2)

power = -1*math.log((f*(U1*sigma1 + myu1))/U2*sigma2 + myu2, 10)/3
temp = (Snf*(U2*sigma2 + myu2)) / ((f * (U1*sigma1 + myu1))**2)
print("temp: ", temp)
Zn = 1 - n/((temp)**power)


'''Lagrange Multiplier Try'''
def func(X):
    x = X[0]
    y = X[1]
    L = X[2] # this is the multiplier. lambda is a reserved keyword in python
    return U1**2 + U2**2 + L * (Zn)

def dfunc(X):
    dLambda = np.zeros(len(X))
    h = 1e-3 # this is the step size used in the finite difference.
    for i in range(len(X)):
        dX = np.zeros(len(X))
        dX[i] = h
        dLambda[i] = (func(X+dX)-func(X-dX))/(2*h)
    return dLambda

#For Finding Minimum
X2 = fsolve(dfunc, [-1, -1, 0])
print(X2, func(X2))


'''Differentiation'''
# x = sym.Symbol('x')
# function = x + 4 + 7 * x + 11
# derivitive = sym.diff(function)
# print(derivitive)


'''Partial Derivative'''
# from sympy import Symbol, Derivative
# x= Symbol('x')
# y= Symbol('y')
# function= x**2 * y**3 + 12*y**4
# partialderiv= Derivative(function, x)
# print("DO IT", partialderiv.doit())


'''Gradient of an equation'''
# import numdifftools as nd
# #one variable 
# g = lambda x:(x**4)+x + 1
# grad1 = nd.Gradient(g)([1]) 
# print("Gradient of x ^ 4 + x+1 at x = 1 is ", grad1) 

# #two variable
# def rosen(x):  
#     return (1-x[0]**2) +(x[1]-x[0]**2)**2
# grad2 = nd.Gradient(rosen)([1, 2]) 
# print("Gradient of (1-x ^ 2)+(y-x ^ 2)^2 at (1, 2) is ", grad2) 


'''Misc'''
# a = (f*pdfSu)**2/U2
# temp = f*pdfSu/pdfSe
# b = (-1*(math.log(temp, 10)))/3
# Snf = (pdfSa*pdfSu)/(pdfSu - Sm)
# Nf = (Snf/a)**(1/b)
# Dn = n/Nf

'''Input'''
# n = int(input("Number of applied cycles: "))
# f = float(input("Fatigue limit strength fraction: "))
# Sa = float(input("Alternating stress (in MPa): "))
# myu1 = float(input("Mean of Ultimate Strength (Su): "))
# sigma1 = float(input("Standard deviation of Ultimate Strength (Su): "))
# myu2 = float(input("Mean of Fatigue Limit (Se): "))
# sigma2 = float(input("Standard Deviation of Fatigue Limit (Se): "))