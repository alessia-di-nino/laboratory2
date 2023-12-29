import pylab
import numpy as np
from scipy.optimize import curve_fit

path='./es2_Thevenin/'
data='dati.txt'

R, DR, I, DI = pylab.loadtxt(path+data, unpack=True, delimiter=",")

pylab.errorbar(R, I, DI, DR, linestyle ="", color = "black", marker = "")

pylab.rc("font", size = 16)
pylab.xlabel("R [ohm]", fontsize = 18)
pylab.xscale("log")
pylab.ylabel("I [A]", fontsize = 18)
pylab.yscale("log")
pylab.minorticks_on()

init = (4.96, 28.79)

sigma = DI
w = 1/sigma**2

def ff(R, V0, r_g):
    return V0/(R + r_g)

pars, covm = curve_fit(ff, R, I, init, sigma, absolute_sigma=False)

kappa2 = ((w*(I-ff(R, *pars))**2)).sum()

ndof = 14

print(pars)
print(covm)
print(kappa2, ndof, kappa2/ndof)

for i in range (5):

    s_e = np.sqrt(((pars[0]/R**2)*DR)**2 + DI**2)
    pars, covm = curve_fit(ff, R, I, init, sigma=s_e, absolute_sigma=False)

w1 = 1/s_e**2
kappa3 = ((w1*(I-ff(R, *pars))**2)).sum()

print(pars, np.sqrt(covm.diagonal()))
print(covm)
print(kappa3, ndof, kappa3/ndof)

xx = np.logspace(1, 7, 500)
pylab.plot(xx,ff(xx,*pars), color = "red")

pylab.show()