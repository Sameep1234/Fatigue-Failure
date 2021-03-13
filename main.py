import numpy as np
import matplotlib.pyplot as plt
import math
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

n = int(input("Number of applied cycles: "))
f = float(input("Fatigue limit strength fraction: "))
Sa = float(input("Alternating stress (in MPa): "))
[myu1, sigma1] = float(input("Mean and stadard deviation of ultimate strength"))
[myu2, sigma2] = float(input("Mean and stadard deviation of Fatigue Limit"))

PI = math.pi
Su = (1/math.sqrt(2*PI*sigma1**2))*(e**(-1*((x - myu1)**2)/2*sigma1**2))
Se = (1/math.sqrt(2*PI*sigma2**2))*(e**(-1*((y - myu2)**2)/2*sigma2**2))
U1 = (Su - myu1)/sigma1
U2 = (Se - myu2)/sigma2


power = -1*math.log((f*U1)/U2, 10)/3
temp = ((U1 - Sm) * U1 * (f**2))/(Sa*U2)
Zn = 1 - n*((temp)**power)


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
# a = (f*Su)**2/U2
# temp = f*Su/Se
# b = (-1*(math.log(temp, 10)))/3
# Snf = (Sa*Su)/(Su - Sm)
# Nf = (Snf/a)**(1/b)
# Dn = n/Nf