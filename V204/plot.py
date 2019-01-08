import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
T1, T2 = np.genfromtxt("data/data<++>.txt", unpack=True)
tab<++> = TexTable([<++>,<++>], [r"<++>", r"<++>"], label="tab<++>", caption="<++>", roundPrecision=<++>)
tab<++>.writeFile("build/tab<++>.tex")

laenge, breite, tiefe, rho, c= np.genfromtxt("data/dataextra.txt", unpack=True)
tab2 = TexTable([laenge*1e2, breite*1e2, tiefe*1e2, rho ,c], [r"Länge / \si{\centi\meter}", r"Breite / \si{\centi\meter}", r"Tiefe / \si{\centi\meter}", r"\rho / \si{\kilo\gram\per\cubic\meter}", r"c / \si{\joule\per\kilo\gram\kelvin}"], label="tab2", caption="Die Materialeigenschaften der einzelnen Stäbe. Reihe 1: Messing. Reihe 2: Messing. Reihe 3: Aluminium. Reihe 4: Edelstahl.", roundPrecision=1)
tab2.writeFile("build/tab2.tex")

<++>, <++> = np.genfromtxt("data/data<++>.txt", unpack=True)
tab<++> = TexTable([<++>,<++>], [r"<++>", r"<++>"], label="tab<++>", caption="<++>", roundPrecision=<++>)
tab<++>.writeFile("build/tab<++>.tex")
#extra values 
T1700= <++>
T4700= <++>
T5700= <++>
T8700= <++>

A=breite*tiefe
K=np.array([120, 120, 236, 15])
L=np.array([<++>, <++>, <++>, <++>])

Ampnah1= <++>
Ampfern1= <++>
delt1= <++>
phase1= 2*np.pi*delt1/80

Ampnah2= <++>
Ampfern2= <++>
delt2= <++>
phase2= 2*np.pi*delt2/80

Ampnah3= <++>
Ampfern3= <++>
delt3= <++>
phase3= 2*np.pi*delt3/80
#functions 

def func(x):
    return x+1

def f(x, a, b, c, d):
     return a * np.sin(b * x + c) + d
#calculate 

Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
 
parameters, pcov = curve_fit(f, x, y, sigma=err_x)

delT11= (T1[1]-T2[1])/L[0]
delT12= (T1[5]-T2[5])/L[0]
delT13= (T1[10]-T2[10])/L[0]
delT14= (T1[15]-T2[15])/L[0]
delT15= (T1[20]-T2[20])/L[0]
delQ1= -K[0]*A[0]*delT11
delQ2= -K[0]*A[0]*delT12
delQ3= -K[0]*A[0]*delT13
delQ4= -K[0]*A[0]*delT14
delQ5= -K[0]*A[0]*delT15

Tdiff1= T2-T1
Tdiff2= T7-T8

K1= (rho[0]*c[0]*(L[0])**2)/(2*delt1*np.log(Ampnah1/Ampfern1))
K2= (rho[2]*c[2]*(L[2])**2)/(2*delt2*np.log(Ampnah2/Ampfern2))
K3= (rho[3]*c[3]*(L[3])**2)/(2*delt3*np.log(Ampnah3/Ampfern3))
#save solution 

file = open("build/solution.txt", "w")
file.write("delQ1/delt= {} W\ndelQ2/delt= {} W\ndelQ3/delt= {} W\ndelQ4/delt= {} W\ndelQ5/delt= {} W\n\nMessing:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\n\nAluminium:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\n\nEdelstahl:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\n\n ".format(delQ1, delQ2, delQ3, delQ4, delQ5, Ampnah1, Ampfern1, delt1, phase1, Ampnah2, Ampfern2, delt2, phase2, Ampnah3, Ampfern3, delt3, phase3 ))
file.close()

#Make plots for data
plt.figure(1)
plt.plot(t, T1, "xr", label="Daten")
plt.plot(t, T4, "xb", label="Daten")
plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlim([0], x[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$y(x)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")


plt.figure(2)
plt.plot(t, T5, "xr", label="Daten")
plt.plot(t, T8, "xb", label="Daten")
plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlim([0], x[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$y(x)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

plt.figure(3)
plt.plot(t, Tdiff1, "xr", label="Daten")
plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlim([0], x[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$y(x)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

plt.figure(4)
plt.plot(t, Tdiff2, "xr", label="Daten")
plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlim([0], x[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$y(x)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

plt.figure(5)
plt.plot(t, T12, "xr", label="Daten")
plt.plot(t, T22, "xb", label="Daten")
plt.xlim([0], x[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$y(x)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

plt.figure(6)
plt.plot(t, T52, "xr", label="Daten")
plt.plot(t, T62, "xb", label="Daten")
plt.xlim([0], x[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$y(x)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

plt.figure(7)
plt.plot(t, T72, "xr", label="Daten")
plt.plot(t, T82, "xb", label="Daten")
plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlim([0], x[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$y(x)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")
#curvefit plot

plt.errorbar(x, y, yerr=err_y, fmt='rx', label='Daten')
t = np.linspace(-0.5, 2 * np.pi + 0.5)
plt.plot(t, f(t, *parameters), 'b-', label='Fit')
plt.plot(t, np.sin(t), 'g--', label='Original')
plt.xlim(t[0], t[-1])
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot1b.pdf")

