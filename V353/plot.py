import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable 
from scipy import stats

#Generate data 

#a   
freq1, Amp1 = np.genfromtxt("data/freq1.txt", unpack= True)
tab1 = TexTable([freq1, Amp1, np.log(Amp1)], ["Frequenz", "Amplitude", "logarithmierte Amplitude"])
tab1.writeFile("build/tab1.tex")
#b
U0= 
R=
freq2, Amp2 = np.genfromtxt("data/freq2.txt", unpack= True)
tab2 = TexTable([freq2, Amp2, Amp2/U0], ["Frequenz", "Amplitude", "Amplitude/U0"])
tab2.writeFile("build/tab2.tex")
#c 
freq3, phase3 = np.genfromtxt("data/freq3.txt", unpack= True)
tab3 = TexTable([freq3, phase], ["Frequenz", "Phasenverschiebung"])
tab3.writeFile("build/tab3.tex")
#d
Ampr4, phase = np.genfromtxt("data/freqr4.txt", unpack= True)
tab4 = TexTable([phase, Amp4, Amp4/U0], ["Phasenverschiebung", "Amplitude", "Amplitude/U0"])
tab4.writeFile("build/tab4.tex")


#Functions to calculate with data
#a 
get1RCa(Steigung):
    return -Steigung 
#b 
RC(x, R, C): 
    return np.log(1/np.sqrt(1+(x**2)*(R**2)*(C**2)))
#c 
getRCc(x, R, C):
    return np.arctan(-x*R*C)
#d 
getRCd(x, omega, R, C):
    - np.sin(x)/(omega*R*C)
# Calculate
#a
Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(freq1,np.log(Amp1))
#b
params2, pcov2 = curve_fit(RC, freq2, Amp2/U0)
#c 
params3, pcov3 = curve_fit(getRCc, freq3, phase)
#d 
params4, pcov4 = curve_fit(getRCd, Amp4, phase)
#Save Solutions
#a
taba = TexTable([freq1, Amp1], ["Frequenz", "Amplitude"])
taba.writeFile("build/tabsolutiona.tex")
#b
tabb = TexTable([freq2,Amp2], ["Frequenz", "Amplitude"])
tabb.writeFile("build/tabsolutionb.tex")
#c 
tabc =TexTable([freq3, phase], ["Frequenz", "Phasenverschiebung"])
tabc.writeFile("build/tabsolutionc.tex")
#d 
tabd =TexTable([Amp4, phase], ["Frequenz", "Phasenverschiebung"])
tabc.writeFile("build/tabsolutionc.tex")
#Make plots for data
#a
plt.plot(freq1, np.log(Amp))
plt.plot(freq1, Steigung1*freq1+yAbschnitt1)
plt.savefig("build/plota.pdf")
#b
plt.plot(freq2, np.log(Amp2/U0))
plt.plot(freq2, RC(freq2, *params2))
plt.savefig("build/plotb.pdf")
#c
plt.plot(freq3, np.log(phase))
plt.plot(freq3,getRCc(freq3, *params3))
plt.savefig("build/plotc.pdf")
