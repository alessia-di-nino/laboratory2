import matplotlib.pyplot as plt
import numpy as np
import math as mt
from scipy.optimize import curve_fit

##import dei dati

path='./es2_Thevenin/'
data='dati.txt'

R, s_R, I, s_I = np.loadtxt(path+data, unpack=True, delimiter=',')

##plot semplice dei dati

fig = plt.figure('Grafico di fit 1', figsize=(10,6), dpi=100,)
ax1, ax2 = fig.subplots(2,1, sharex=True, gridspec_kw=dict(height_ratios=[2, 1], hspace=0.05))

ax1.errorbar(R, I, s_I, s_R, fmt='.', label='datas', color='black')
ax1.set_yscale('log')
ax1.set_ylabel('intensità di corrente I [A]')
ax2.set_xscale('log')
ax2.set_xlabel('Resistenze R [ohm]')

##primo fit dei minimi quadrati

def f1(R, V0): return V0/R

popt1, pcov1 = curve_fit(f1, R, I, p0=(2.66), sigma=s_I, absolute_sigma=False)

print(popt1, np.sqrt(pcov1.diagonal()))

k1=sum(((I-f1(R, *popt1))/s_I)**2)
#ndof = R.shape-popt1.shape, dà dei problemi documentati sul perchè, il problema sta nel tipo di oggetto che è popt1 e R.
print(k1, 14, k1/14, '\n')

##controllo 1

c = abs(popt1[0]/R**2)*s_R

mask=(c-s_I*0.1 < 0)

print(f'Controllo: {sum(mask)}', '\n')

##incertezze efficaci 1

for i in range(5):

    s_eff1= np.sqrt(((popt1[0]/R**2)*s_R)**2 + s_I**2)
    popt1, pcov1 = curve_fit(f1, R, I, p0=(2.66), sigma=s_eff1, absolute_sigma=False)


k1_eff=sum(((I-f1(R, *popt1))/s_eff1)**2)
print(popt1, np.sqrt(pcov1.diagonal()))
print(k1_eff, 14, k1_eff/14, '\n')

res1 = I - f1(R, *popt1)

##plot del grafico di fit e residui

ax1.plot(R, f1(R, *popt1), label='fit 1', color='red')

ax2.errorbar(R, res1, s_eff1, fmt='.', color='black', label='residuals')
mline=np.logspace(1, 7, 100)
ax2.plot(mline, np.full(mline.shape, 0.0), label='fit', color='red')


ax1.legend()
ax2.legend()
fig.align_ylabels((ax1, ax2))
plt.show()


##plot semplice dei dati2

fig1 = plt.figure('Grafico di fit 2', figsize=(10,6), dpi=100,)
ax3, ax4 = fig1.subplots(2,1, sharex=True, gridspec_kw=dict(height_ratios=[2, 1], hspace=0.05))

ax3.errorbar(R, I, s_I, s_R, fmt='.', label='datas', color='black')
ax3.set_yscale('log')
ax3.set_ylabel('intensità di corrente I [A]')
ax4.set_xscale('log')
ax4.set_xlabel('Resistenze R [ohm]')
plt.show()
##secondo fit dei minimi quadrati

def f2(R, V0, rg): return V0/(R + rg)

popt2, pcov2 = curve_fit(f2, R, I, p0=(4.96, 28.79), sigma=s_I, absolute_sigma=False)

print(popt2, np.sqrt(pcov2.diagonal()))

k2=sum(((I-f2(R, *popt2))/s_I)**2)
#ndof = R.shape-popt1.shape, dà dei problemi documentati sul perchè, il problema sta nel tipo di oggetto che è popt1 e R.
print(k2, 13, k2/13, '\n')

##controllo 2

c = abs(popt2[0]/R**2)*s_R

mask=(c-s_I*0.1 < 0)

print(f'Controllo: {sum(mask)}', '\n')

##incertezze efficaci 2

for i in range(5):

    s_eff2= np.sqrt(((popt2[0]/R**2)*s_R)**2 + s_I**2)
    popt2, pcov2 = curve_fit(f2, R, I, p0=(2.66, 29.79), sigma=s_eff2, absolute_sigma=False)


k2_eff=sum(((I-f2(R, *popt2))/s_eff2)**2)
print(popt2, np.sqrt(pcov2.diagonal()))
print(k2_eff, 14, k2_eff/14, '\n')

res2 = I - f2(R, *popt2)

##plot del grafico di fit e residui2

ax3.plot(R, f2(R, *popt2), label='fit 2', color='red')

ax4.errorbar(R, res2, s_eff2, fmt='.', color='black', label='residuals')
mline=np.logspace(1, 7, 100)
ax4.plot(mline, np.full(mline.shape, 0.0), label='fit', color='red')


ax3.legend()
ax4.legend()
fig.align_ylabels((ax3, ax4))
plt.show()
plt.savefig(".")
































