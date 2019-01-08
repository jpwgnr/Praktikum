import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
laenge, breite, tiefe, rho, c= np.genfromtxt("data/dataextra.txt", unpack=True)
tab2 = TexTable([laenge*1e2, breite*1e2, tiefe*1e2, rho ,c], [r"Länge / \si{\centi\meter}", r"Breite / \si{\centi\meter}", r"Tiefe / \si{\centi\meter}", r"\rho / \si{\kilo\gram\per\cubic\meter}", r"c / \si{\joule\per\kilo\gram\kelvin}"], label="tab2", caption="Die Materialeigenschaften der einzelnen Stäbe. Reihe 1: Messing. Reihe 2: Messing. Reihe 3: Aluminium. Reihe 4: Edelstahl.", roundPrecision=1)
tab2.writeFile("build/tab2.tex")

s, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt("data/dataa.txt", unpack=True)
tab1 = TexTable([s,T1, T2, T3, T4, T5, T6, T7, T8], [r"$t /\si{\second}$", r"$T_1 /\si{\degreeCelsius}$", r"$T_2 /\si{\degreeCelsius}$", r"$T_3 /\si{\degreeCelsius}$", r"$T_4 /\si{\degreeCelsius}$", r"$T_5 /\si{\degreeCelsius}$", r"$T_6 /\si{\degreeCelsius}$", r"$T_7 /\si{\degreeCelsius}$", r"$T_8 /\si{\degreeCelsius}$"], label="tab1", caption="Zeit gegen Temperaturen der einzelnen Elemente", roundPrecision=2)
tab.writeFile("build/tab1.tex")
T1new= T1+273.15
T2new= T2+273.15
T3new= T3+273.15
T4new= T4+273.15
T5new= T5+273.15
T6new= T6+273.15
T7new= T7+273.15
T8new= T8+273.15

#extra values 
#T1700= 46.06
#T4700= 40.10
#T5700= 49.94
#T8700= 36.20

A=breite*tiefe
K=np.array([120, 120, 236, 21])
L=np.array([0.03, 0.03, 0.03, 0.03])

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

#calculate 

delT12= (T1new-T2new])/L[0]
delT34= (T3new-T4new)/L[1]
delT56= (T5new-T6new)/L[2]
delT78= (T7new-T8new)/L[3]
delQ12= -K[0]*A[0]*delT12
delQ34= -K[1]*A[1]*delT34
delQ56= -K[2]*A[2]*delT56
delQ78= -K[3]*A[3]*delT78

K1= (rho[0]*c[0]*(L[0])**2)/(2*delt1*np.log(Ampnah1/Ampfern1))
K2= (rho[2]*c[2]*(L[2])**2)/(2*delt2*np.log(Ampnah2/Ampfern2))
K3= (rho[3]*c[3]*(L[3])**2)/(2*delt3*np.log(Ampnah3/Ampfern3))
#save solution 

file = open("build/solution.txt", "w")
file.write("delQ12/delt= {} W\ndelQ34/delt= {} W\ndelQ56/delt= {} W\ndelQ78/delt= {} W\n\nMessing:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\n\nAluminium:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\n\nEdelstahl:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\n\n ".format(delQ12, delQ34, delQ56, delQ78, Ampnah1, Ampfern1, delt1, phase1, Ampnah2, Ampfern2, delt2, phase2, Ampnah3, Ampfern3, delt3, phase3 ))
file.close()

#Make plots for data
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

