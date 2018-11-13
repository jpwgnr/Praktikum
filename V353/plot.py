import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable 
from scipy import stats

#Generate data 

#a   
U, t = np.genfromtxt("data/dataa.txt", unpack= True)
tab1 = TexTable([U, t], [r"Spannung in \si{\volt}", r"t in \si{\second}"])
tab1.writeFile("build/taba.tex")

U0=1.47 
differentU = U0-U
newU=-np.log(differentU/U0)

#b
freq2, U2, a2 = np.genfromtxt("data/databc.txt", unpack= True)
tab2 = TexTable([freq2, U2, a2], [r"Frequenz in \si{\Hertz}", r"Amplitude der Spannung in \si{\hertz}",r"Phasenverschiebung in \si{\second}"])
tab2.writeFile("build/tabb.tex")

U1= 621e-3 
A2= np.sqrt(1/(((U1/U2)**2)-1))
omega=2*np.pi*freq2

#c 
b= 1/freq2
phase= (a2/b)*np.pi
newphase= -1/np.tan(phase)

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
taba =TexTable([t, newU], [r"t in \si{\second}", r"$log (\frac{U(t)}{U_{0}})"])
taba.writeFile("build/tabsolutiona.tex")
#b
tabb = TexTable([1/omega ,A2], [r"\frac{1}{\omega}",r"\sqrt{\frac{1}{\frac{U_{0}{A(\omega)}}^{2}}}"])
tabb.writeFile("build/tabsolutionb.tex")
#d 
tabd =TexTable([phase, Aw], [r"Phasenverschiebung in \si{\radian}", r"\frac{A(\omega)}{U_{0}}"])
tabd.writeFile("build/tabsolutiond.tex")
#Make plots for data
#a
plt.figure(1)
plt.plot(t, newU, "xr")
plt.plot(t,Funktion(Steigung1, yAbschnitt1, t), "r")
plt.savefig("build/plota.pdf")
#b
plt.figure(2)
plt.plot(1/omega, A2, "xr")
plt.plot(1/omega, Funktion(Steigung2, yAbschnitt2, 1/omega), "r" )
plt.savefig("build/plotb.pdf")
#c
plt.figure(3)
plt.plot(1/omega, newphase, "xr")
plt.plot(1/omega, Funktion(Steigung3, yAbschnitt3, 1/omega), "r")
plt.savefig("build/plotc.pdf")
#d Plot1
plt.figure(4)
plt.plot(phase, Kreis(phase, Steigung1), "r")
plt.plot(phase, Aw, "r")
plt.savefig("build/plotd1.pdf")
#d Plot2
plt.figure(5)
plt.plot(phase, Kreis(phase, Steigung2), "r")
plt.plot(phase, Aw, "r")
plt.savefig("build/plotd2.pdf")
#d Plot3
plt.figure(6)
plt.plot(phase, Kreis(phase, Steigung3), "r")
plt.plot(phase, Aw, "r")
plt.savefig("build/plotd3.pdf")
