import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
phi21, zweiUout2 = np.genfromtxt("data/dataa.txt", unpack=True)
phi2= (phi21/360)*np.pi*2
tab2 = TexTable([phi2,zweiUout2/2], [r"$\varphi/ \si{\radian}$", r"$U_{Out} / \si{\volt}$"], label="tab2", caption=r"Die Phasenverschiebung $\varphi$ wird gegen die Werte der Ausgangsspannung $U_{Out}$ aufgetragen. ", roundPrecision=1)

tab2.writeFile("build/tab2.tex")

phi31, zweiUout3 = np.genfromtxt("data/datab.txt", unpack=True)
phi3= (phi31/360)* np.pi* 2
tab3 = TexTable([phi3,zweiUout3/2], [r"$\varphi / \si{\radian}$", r"$U_{Out} / \si{\volt}$"], label="tab3", caption=r"Die Phasenverschiebung $\varphi$ wird gegen die Werte der Ausgangsspannung $U_{Out}$ aufgetragen.", roundPrecision=1)
tab3.writeFile("build/tab3.tex")

r4, Uout4, GainLP, GainD = np.genfromtxt("data/datac.txt", unpack=True)
tab4 = TexTable([r4*1e2, Uout4, GainLP,GainD], [r"$r / \si{\centi\meter}$", r"$U_{Out} / \si{\volt}$", r"Gain Tiefpass", r"Gain Detektor"], label="tab4", caption=r"Der Abstand $r$ zwischen Leucht- und Photodiode aufgetragen gegen die Spannung $U_{Out}$. Dazu jeweils den Wert für die Verstärkung des Tiefpasses und des Detektors.", roundPrecision=1)
tab4.writeFile("build/tab4.tex")
#extra values 
U_Anfang= 6.56/2

#2 
Uout2 = -zweiUout2/2 
#3 
Uout3 = zweiUout3/2 
#4 

#functions 

def getUout(phi, U0, delta):
    return (2/np.pi)*U0*np.cos(phi +delta)

def func(x, m, n):
    return m*x+n

#calculate 
#2
U02params, pcov2 = curve_fit(getUout, phi2, Uout2, p0=[6.56, 0.5])
errU02 = np.sqrt(np.abs(np.diag(pcov2)))
newphi= np.linspace(phi2[0], phi2[-1], 400)
#3
U03params, pcov3 = curve_fit(getUout, phi3, Uout3, p0=[6.56, 0.5])
errU03 = np.sqrt(np.abs(np.diag(pcov3)))
#4 
newr = np.linspace(r4[0], r4[-1], 4000)
Ueff4= Uout4*(1/(GainLP*GainD))
U04params, pcov4 = curve_fit(func, np.log(r4*1e2),np.log(Ueff4))
errU04 = np.sqrt(np.abs(np.diag(pcov4)))

#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
#parameters, pcov = curve_fit(f, x, y, sigma=err_x)

#save solution 

tab5 = TexTable([r4*1e2, Ueff4*1e6], [r"$r / \si{\centi\meter}$", r"$U_{Out} / \si{\micro\volt}$"], label="tab5", caption=r"Der Abstand $r$ zwischen Leucht- und Photodiode aufgetragen gegen die tatsächliche Spannung $U_{Out}$, nach Division durch die Verstärkerwerte.", roundPrecision=1)
tab5.writeFile("build/tab5.tex")

file = open("build/solution.txt", "w")
file.write("\tU02 = {} Fehler: {} \n\tU03 = {} Fehler: {}\n\t Steigung, Y-Abschnitt:\t{}\n\tFehler:\t{} ".format(U02params, errU02, U03params, errU03, U04params, errU04))

file.close()

#Make plots for data
plt.figure(1)
plt.plot(phi2, Uout2, "xr", label="Daten")
plt.plot(newphi, getUout(newphi, *U02params), "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$\varphi/\si{\radian}$")
plt.ylabel(r"$U_{Out} / \si{\volt}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot2.pdf")

plt.figure(2)
plt.plot(phi3, Uout3, "xr", label="Daten")
plt.plot(newphi, getUout(newphi,*U03params), "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$\varphi/\si{\radian}$")
plt.ylabel(r"$U_{Out} / \si{\volt}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot3.pdf")

plt.figure(3)
plt.plot(r4*1e2,Ueff4, "xr", label="Daten")
plt.plot(newr*1e2, np.exp(func(np.log(newr*1e2), *U04params)), "b", label="Fit", linewidth=1.0)
plt.xlabel(r"$r/\si{\centi\meter}$")
plt.ylabel(r"$U_{Out} / \si{\volt}$")
plt.legend(loc="best")
plt.xscale("log")
plt.yscale("log")
plt.tight_layout()
plt.savefig("build/plot4.pdf")
#curvefit plot

#plt.errorbar(x, y, yerr=err_y, fmt='rx', label='Daten')
#t = np.linspace(-0.5, 2 * np.pi + 0.5)
#plt.plot(t, f(t, *parameters), 'b-', label='Fit')
#plt.plot(t, np.sin(t), 'g--', label='Original')
#plt.xlim(t[0], t[-1])
#plt.xlabel(r'$t$')
#plt.ylabel(r'$f(t)$')
#plt.legend(loc='best')
#plt.tight_layout()
#plt.savefig("build/plot1b.pdf")

