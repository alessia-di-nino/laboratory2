import numpy as np
import pylab as py

nomefile = "./es12/c3.txt"

x,y = np.loadtxt(nomefile, unpack=True)

py.figure()

py.plot(x,y)
py.rc("font", size = 14)
py.xlabel("time [us]", fontsize = 14)
py.ylabel("signal [digit]", fontsize=14)
py.tight_layout()

py.figure()

ASD = abs(np.fft.rfft(y))
numpunti=int(len(y)/2)+1
risfreq=1/(1e-6*max(x))

print("frequency resolution [Hz]", risfreq)
freqmax = numpunti*risfreq
freq=np.linspace(0, freqmax,numpunti)

py.plot(freq, ASD, color="red")
py.rc("font", size = 14)
py.xlabel("frequency [Hz]", fontsize = 14)
py.ylabel("ASD [arb.un.]", fontsize = 14)

py.show()