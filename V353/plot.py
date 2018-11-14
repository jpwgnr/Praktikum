import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable 
from scipy import stats

#Generate data 

#a   
U, t = np.genfromtxt("data/dataa.txt", unpack= True)
tab1 = TexTable([U, t], [r"$U/ \si{\volt}$", r"$t/ \si{\second}$"])
tab1.writeFile("build/taba.tex")

U0=1.47 
differentU = U0-U
newU=-np.log(differentU/U0)

#b
freq2, U2, a2 = np.genfromtxt("data/databc.txt", unpack= True)
tab2 = TexTable([freq2, U2, a2], [r"$f/ \si{\Hertz}$", r"$A(\omega)/ \si{V}$",r"$a / \si{\second}$"])
tab2.writeFile("build/tabb.tex")

U1= 621e-3 
A2= np.sqrt(1/(((U1/U2)**2)-1))
omega=2*np.pi*freq2

#c 
b= 1/freq2
phase= (-a2/b)*np.pi
newphase= (-1/np.tan(phase))

#d 
Aw=U2/U1

# Calculate
#a
Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(t,newU)

def Funktion(m, n, x):
    return m*x+n
#b
Steigung2, yAbschnitt2, r_value2, p_value2, std_err2= stats.linregress(1/omega,A2)
#c 
Steigung3, yAbschnitt3, r_value3, p_value3, std_err3= stats.linregress(1/omega,newphase)
#d 
def Kreis(phi, RC):
    return -np.sin(phi)*(1/omega)*RC

#Save Solutions
#a 
taba =TexTable([t, newU], [r"$t/ \si{\second}$", r"$-log(\frac{U(t)}{U_{0}})$"])
taba.writeFile("build/tabsolutiona.tex")
#b
tabb = TexTable([1/omega ,A2], [r"$\frac{1}{\omega}/ \si{\second}$",r"$\sqrt{\frac{1}{(\frac{U_{0}}{A(\omega)})^{2}-1}}$"])
tabb.writeFile("build/tabsolutionb.tex")
#c 
tabc = TexTable([1/omega ,newphase], [r"$\frac{1}{\omega}/ \si{\second}$",r"$-\frac{1}{tan(\phi(\omega))}$"])
tabc.writeFile("build/tabsolutionc.tex")
#d 
tabd =TexTable([phase, Aw], [r"$\phi/ \si{\radian}$", r"$\frac{A(\omega)}{U_{0}}$"])
tabd.writeFile("build/tabsolutiond.tex")

#all solutions 

file = open("build/solutions.txt", "w")
file.write("a) 1/RC= {} +/- {} 1/s \nb) 1/RC= {}  +/- {} 1/s \nc) 1/RC= {}  +/- {} 1/s \n".format(Steigung1, std_err1, Steigung2, std_err2, Steigung3, std_err3))
file.close()

#Theoriekurve d, dafür Theoriewerte phi
Phi1= np.arctan(-omega*(1/Steigung1))
Phi2= np.arctan(-omega*(1/Steigung2))
Phi3= np.arctan(-omega*(1/Steigung3))
#Make plots for data
#a
plt.figure(1)
plt.plot(t, newU, "xr", label="Daten")
plt.plot(t, Funktion(Steigung1, yAbschnitt1, t), "r", label="Fit")
plt.plot(t, Funktion(Steigung1+std_err1, yAbschnitt1, t), "b--", label="Fehler des Fits", linewidth=0.5)
plt.plot(t, Funktion(Steigung1-std_err1, yAbschnitt1, t), "b--", linewidth=0.5)
plt.xlim(t[0], t[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$-log(\frac{U(t)}{U_{0}})$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plota.pdf")
#b
plt.figure(2)
plt.plot(1/omega, A2, "xr", label="Daten")
plt.plot(1/omega, Funktion(Steigung2, yAbschnitt2, 1/omega), "r", label="Fit")
plt.plot(1/omega, Funktion(Steigung2+std_err2, yAbschnitt2, 1/omega), "b--", label="Fehler des Fits", linewidth=0.5)
plt.plot(1/omega, Funktion(Steigung2-std_err2, yAbschnitt2, 1/omega), "b--", linewidth=0.5)
plt.xlim(t[0], t[-1])
plt.xlabel(r"$\frac{1}{\omega}/ \si{\second}$")
plt.ylabel(r"$\sqrt{\frac{1}{(\frac{U_{0}}{A(\omega)})^{2}-1}}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotb.pdf")
#c
plt.figure(3)
plt.plot(1/omega, newphase, "xr", label="Daten")
plt.plot(1/omega, Funktion(Steigung3, yAbschnitt3, 1/omega), "r", label="Fit")
plt.plot(1/omega, Funktion(Steigung3+std_err3, yAbschnitt3, 1/omega), "b--", label="Fehler des Fits", linewidth=0.5)
plt.plot(1/omega, Funktion(Steigung3-std_err3, yAbschnitt3, 1/omega), "b--", linewidth=0.5)
plt.xlim(t[0], t[-1])
plt.xlabel(r"$\frac{1}{\omega}/ \si{\second}$")
plt.ylabel(r"$-\frac{1}{tan(\phi(\omega))}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotc.pdf")
#d Plot1
plt.figure(4)
ax = plt.subplot(111, projection="polar")
ax.plot(phase, Kreis(phase, Steigung1),  "r", label="Fit")
ax.plot(phase, Kreis(phase, Steigung1+std_err1),  "b--", label="Fehler des Fit", linewidth= 0.5)
ax.plot(phase, Kreis(phase, Steigung1-std_err1),  "b--", linewidth=0.5)
ax.plot(phase, Aw, "rx", label="Daten")
ax.plot(Phi1, Kreis(Phi1, Steigung1),  "g", label="Theoriekurve")
#ax.plot(Phi1, Kreis(Phi1, Steigung1+std_err1),  "g--", label="Fehler der Theoriekurve", linewidth= 0.5)
#ax.plot(Phi1, Kreis(Phi1, Steigung1+std_err1),  "g--", linewidth=0.5)
ax.legend(loc="best")
plt.savefig("build/plotd1.pdf")
#d Plot2
plt.figure(5)
ax = plt.subplot(111, projection="polar")
ax.plot(phase, Kreis(phase, Steigung2),  "r", label="Fit")
ax.plot(phase, Kreis(phase, Steigung2+std_err2),  "b--", label="Fehler des Fit", linewidth= 0.5)
ax.plot(phase, Kreis(phase, Steigung2-std_err2),  "b--", linewidth=0.5)
ax.plot(phase, Aw, "rx", label="Daten")
ax.plot(Phi2, Kreis(Phi2, Steigung2),  "g", label="Theoriekurve")
#ax.plot(Phi2, Kreis(Phi2, Steigung2+std_err2),  "g--", label="Fehler der Theoriekurve", linewidth= 0.5)
#ax.plot(Phi2, Kreis(Phi1, Steigung2+std_err2),  "g--", linewidth=0.5)
ax.legend(loc="best")
plt.savefig("build/plotd2.pdf")
#d Plot3
plt.figure(6)
ax = plt.subplot(111, projection="polar")
ax.plot(phase, Kreis(phase, Steigung3),  "r", label="Fit")
ax.plot(phase, Kreis(phase, Steigung3+std_err3),  "b--", label="Fehler des Fit", linewidth= 0.5)
ax.plot(phase, Kreis(phase, Steigung3-std_err3),  "b--", linewidth=0.5)
ax.plot(phase, Aw, "rx", label="Daten")
ax.plot(Phi2, Kreis(Phi3, Steigung3),  "g", label="Theoriekurve")
#ax.plot(Phi2, Kreis(Phi3, Steigung3+std_err3),  "g--", label="Fehler der Theoriekurve", linewidth= 0.5)
#ax.plot(Phi2, Kreis(Phi3, Steigung3+std_err3),  "g--", linewidth=0.5)
ax.legend(loc="best")
plt.savefig("build/plotd3.pdf")
