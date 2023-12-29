import math as mt
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import odr

##dividere le incertrezze per 4
## import dei dati

path='./es8_int-dev/'
data='dati.txt'

t, s_t, DV, s_DV = np.loadtxt(path+data, unpack=True)

## scatter-plot semplice dei dati: d.d.p-tempo

fig = plt.figure('carica', figsize=(10,6), dpi=100)

ax1, ax2 = fig.subplots(2, 1, sharex=True, gridspec_kw=dict(height_ratios=[2, 1], hspace=0.05))

ax1.errorbar(t, DV, s_DV, s_t, fmt='.', label='d.d.p')
ax1.set_ylabel('d.d.p [digit]')
#plt.show()
mask1=(t<935)


##numerical recepeis
## fit minimi quadrati carica

def carica(t, A, B, tau1): return A - B*np.exp(-t/tau1)

popt, pcov = curve_fit(carica, t[mask1], DV[mask1], p0=(3522, 3522, 150), sigma=s_DV[mask1], absolute_sigma=True)

A_hat, B_hat, tau1_hat = popt
s_A, s_B, s_tau1 = np.sqrt(pcov.diagonal())

chisq1 = sum(((DV[mask1]-carica(t[mask1], A_hat, B_hat, tau1_hat))/s_DV[mask1])**2)

ndof1 = t[mask1].size-popt.size

print(f'Chi quadro: {chisq1}', '\n', f'Gradi di libertà e dev std: {ndof1} +/- {mt.ceil(np.sqrt(2*ndof1))}', '\n')

#controllo sugli errori

C = abs((B_hat/tau1_hat)*np.exp(-t[mask1]/tau1_hat))*s_t[mask1]

mask=(C - s_DV[mask1]*0.1 > 0)

print(f'Controllo: {sum(mask)}')

#ax1.plot(t, carica(t, fem_hat, tau1_hat), marker='', linestyle='-')


#incertezze efficaci
'''
for i in range(5):

    sigma_eff1 = np.sqrt(((popt[1]/popt[2])*np.exp(-t[mask1]/popt[2])*s_t[mask1])**2 + s_DV[mask1]**2)
    popt, pcov = curve_fit(carica, t[mask1], DV[mask1], p0=(3522, 3522, 150), sigma=sigma_eff1, absolute_sigma=True)
    chisq1 = sum(((DV[mask1]-carica(t[mask1], *popt))/sigma_eff1)**2)
'''
print(popt, np.sqrt(pcov.diagonal()), '\n')
print(pcov)
print(f'chi quadro= {chisq1}', '\n')

res1 = DV[mask1] - carica(t[mask1], *popt)

ax1.plot(t[mask1], carica(t[mask1], *popt))

#plt.show()


##grafico dei residui

ax2.errorbar(t[mask1], res1, s_DV[mask1], fmt='.', label='scarica')
#ax2.errorbar(t[mask2], res2, s_DV[mask2], fmt='.', label='scarica')
xgrid = np.linspace(np.min(t[mask1]), np.max(t[mask1]), 1000)
ax2.plot(xgrid, np.full(xgrid.shape, 0.0))
ax2.set_xlabel('tempo [$\\mu s$]')
ax2.set_ylabel('residui [digit]')
ax2.legend()

#plt.xlim(0.0, 10.0)
fig.align_ylabels((ax1, ax2))



## fit minimi quadrati scarica

##dividere le incertrezze per 4
## import dei dati

path='/home/marco/Desktop/Uni_anno2/Laboratorio_2/eser_0/datifit/'
data='data_s.txt'

t, s_t, DV, s_DV = np.loadtxt(path+data, unpack=True)

## scatter-plot semplice dei dati: d.d.p-tempo

fig2 = plt.figure('Scarica', figsize=(10,6), dpi=100)

ax3, ax4 = fig2.subplots(2, 1, sharex=True, gridspec_kw=dict(height_ratios=[2, 1], hspace=0.05))

ax3.errorbar(t, DV, s_DV, s_t, fmt='.', label='d.d.p')
ax3.set_ylabel('d.d.p [digit]')
#plt.show()



##numerical recepeis
## fit minimi quadrati scarica

def scarica(t, C, D, tau): return C*np.exp(-t/tau) + D

popt, pcov = curve_fit(scarica, t[mask1], DV[mask1], p0=(3522, 104, 150), sigma=s_DV[mask1], absolute_sigma=True)

C_hat, D_hat, tau2_hat = popt
s_C, s_D, s_tau2 = np.sqrt(pcov.diagonal())

chisq1 = sum(((DV[mask1]-scarica(t[mask1], *popt))/s_DV[mask1])**2)

ndof1 = t[mask1].size-popt.size

print(f'Chi quadro: {chisq1}', '\n', f'Gradi di libertà e dev std: {ndof1} +/- {mt.ceil(np.sqrt(2*ndof1))}', '\n')

#controllo sugli errori

C = abs((C_hat/tau2_hat)*np.exp(-t[mask1]/tau2_hat))*s_t[mask1]

mask=(C - s_DV[mask1]*0.1 > 0)

print(f'Controllo: {sum(mask)}')

#ax1.plot(t, carica(t, fem_hat, tau1_hat), marker='', linestyle='-')


#incertezze efficaci
'''
for i in range(5):

    sigma_eff2 = np.sqrt(((popt[1]/popt[2])*np.exp(-t[mask1]/popt[2])*s_t[mask1])**2 + s_DV[mask1]**2)
    popt, pcov = curve_fit(scarica, t[mask1], DV[mask1], p0=(3522, 3522, 150), sigma=sigma_eff2, absolute_sigma=True)
    chisq1 = sum(((DV[mask1]-carica(t[mask1], *popt))/sigma_eff2)**2)
'''
print(popt, np.sqrt(pcov.diagonal()), '\n')
print(pcov)
print(f'chi quadro= {chisq1}', '\n')

res2 = DV[mask1] - scarica(t[mask1], *popt)

ax3.plot(t[mask1], scarica(t[mask1], *popt))

##grafico dei residui

ax4.errorbar(t[mask1], res2, s_DV[mask1], fmt='.', label='scarica')
#ax2.errorbar(t[mask2], res2, s_DV[mask2], fmt='.', label='scarica')
xgrid = np.linspace(np.min(t[mask1]), np.max(t[mask1]), 1000)
ax4.plot(xgrid, np.full(xgrid.shape, 0.0))
ax4.set_xlabel('tempo [$\\mu s$]')
ax4.set_ylabel('residui [digit]')
ax4.legend()

#plt.xlim(0.0, 10.0)
fig2.align_ylabels((ax3, ax4))



plt.show()
