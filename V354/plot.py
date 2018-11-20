import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from table import TexTable
from scipy import stats

#Generate data 

#from txt

#a)
t, U1 = np.genfromtxt("data/dataa.txt", unpack=True)
tab1 = TexTable([t*1e6,U1], [r"$t$ /\si{\micro\second}", r"$U$ /\si{\volt}"], label="tab1", caption="Die einhüllende Funktion der gedämpften Schwingung. Zeit $t$ gegen die Spannung $U$", roundPrecision=2)
tab1.writeFile("build/tab1.tex")

#c),d) 
f, U_2, deltat = np.genfromtxt("data/datac.txt", unpack=True)
tab1 = TexTable([f/1e3, U_2, deltat*1e-6], [r"$f$ /\si{\kilo\hertz}", r"$2U$ /\si{\volt}", r"$t$ /\si{\micro\second}"], label="tab2", caption="Kondensatorspannung und Generatorspannung. Verschiedene Frequenzen, Amplitude der Kondensatorspannung und Zeitdifferenz der beiden Spannungen.", roundPrecision=2)
tab1.writeFile("build/tab2.tex")


#extra values 
#allgemein:(Gerät2) 
LmV= ufloat(10.11, 0.03)
L= LmV/1000
CnF= ufloat(2.098, 0.006)
C=CnF/1e9
R1=ufloat(48.1, 0.1)
R2=ufloat(509.5, 0.5)

#a)
#b)
Rap= 3.5e3

#c),d)
U0= 8.4
U2=U_2/2
#give back data
file = open("build/databegin.txt", "w")
file.write("L = {} mV \nC: {} nF \nR1= {} Ohm \nR2= {} Ohm \nU0= {}".format(LmV, CnF, R1, R2, U0))
file.close()

#functions 

def function(m,x,n):
    return m*x+n

#calculate 
#a)
logU= np.log(U1)

Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(t,logU)
Reff= ufloat(-Steigung1,std_err1)
Texp=1/Reff 

#b)
theoRap= 2*unp.sqrt(L/C)

#c) 
#experimental:
Amp=U2/U0
omega= 2*np.pi*f
q= max(Amp)
omegares= omega[15]
omegaminus= omega[10]
omegaplus= omega[20]
diffomega=omegaplus- omegaminus
linAmp=Amp[10:21]
linOmega= omega[10:21]

Steigung2, yAbschnitt2, r_value2, p_value2, std_err2= stats.linregress(linOmega,linAmp)
#theoretisch:
qtheo= (1/R2)*unp.sqrt(L/C)
diffomegatheo=R2/L  

#d) 
b=1/f
phase=2*np.pi*(deltat/b) 
linPhase= phase[10:21] 

Steigung3, yAbschnitt3, r_value3, p_value3, std_err3= stats.linregress(linOmega,linPhase)

#save solution 

#a)
taba = TexTable([t*1e6,logU], [r"$t$ /\si{\micro\second}", r"log $U$"], label="taba", caption="Die linearisierten Werte der einhüllende Funktion der gedämpften Schwingung. Zeit $t$ gegen die logarithmierte Spannung log $U$", roundPrecision=2)
taba.writeFile("build/taba.tex")

#b)
file = open("build/solution.txt", "w")
file.write("Reff = 2*pi*mü = R/2L= {}  \nTexp=1/Reff =2L/R= {}\nRap= {} Ohm\n theo Rap= {} Ohm \nexperimental: \n q= {} \n omegares= {} \n omegaminus= {} \n omegaplus= {} \ndiff+-= {} \n theoretisch: \nqtheo= {}, \ndiffomegatheo= {} ".format(Reff, Texp, Rap, theoRap, q, omegares, omegaminus, omegaplus, diffomega, qtheo, diffomegatheo))
file.close()

#c)
tabc = TexTable([omega/1e5,Amp], [r"$\omega\cdot 10^{5}$ /\si[per-mode=fraction]{\per\second}", r"Amplitude $\frac{U_C(\omega}{U_0}$"], label="tabc", caption="Kreisfrequenz $\omega$ gegen die Amplitude der Kondensatorspannung $U_C$ durch die Generatorspannung $U_0$ dividiert.", roundPrecision=2)
tabc.writeFile("build/tabc.tex")

#d) 
tabd = TexTable([omega/1e5,phase], [r"$\omega\cdot 10^{5}$ /\si[per-mode=fraction]{\per\second}", r"$Phase \varphi$"], label="tabd", caption=r"Kreisfrequenz $\omega$ gegen die Phasenverschiebung $\varphi$ der Kondensatorspannung $U_C$ und der Generatorspannungi $U_0$.", roundPrecision=2)
tabd.writeFile("build/tabd.tex")


#Make plots for data
#a)
plt.figure(1)
plt.plot(t, logU, "xr", label="Daten")
plt.plot(t, function(Steigung1,t,yAbschnitt1), "r", label="Fit", linewidth=1.0)
plt.xlim(t[0], t[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"log $U$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plota.pdf")

#c)
#experimental:
plt.figure(2)
plt.plot(omega/1e5, Amp, "xr", label="Daten")
#plt.plot(linOmega, function(Steigung2,linOmega,yAbschnitt2), "r", label="Fit", linewidth=1.0)
plt.xlim(omega[0]/1e5, omega[-1]/1e5)
plt.xlabel(r"$\omega\cdot 10^{5}/\si[per-mode=fraction]{\per\second}$")
plt.ylabel(r"$\frac{U_C(\omega)}{U_0}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotc.pdf")

#d) 
plt.figure(3)
plt.plot(omega/1e5, phase, "xr", label="Daten")
plt.plot(linOmega, function(Steigung3,linOmega,yAbschnitt3), "r", label="Fit", linewidth=1.0)
plt.xlim(omega[0]/1e5, omega[-1]/1e5)
plt.xlabel(r"$\omega/\cdot 10^{5}\si[per-mode=fraction]{\per\second}$")
plt.ylabel(r"$\varphi$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotd.pdf")

