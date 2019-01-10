import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
from uncertainties import ufloat
#Generate data 

#from txt
laenge, breite, tiefe, rho, c= np.genfromtxt("data/dataextra.txt", unpack=True)
tab2 = TexTable([laenge*1e2, breite*1e2, tiefe*1e2, rho ,c], [r"Länge / \si{\centi\meter}", r"Breite / \si{\centi\meter}", r"Tiefe / \si{\centi\meter}", r"\rho / \si{\kilo\gram\per\cubic\meter}", r"c / \si{\joule\per\kilo\gram\kelvin}"], label="tab2", caption="Die Materialeigenschaften der einzelnen Stäbe. Reihe 1: Messing. Reihe 2: Messing. Reihe 3: Aluminium. Reihe 4: Edelstahl.", roundPrecision=1)
tab2.writeFile("build/tab2.tex")

s, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt("data/dataa.txt", unpack=True)
tab1 = TexTable([s,T1, T2, T3, T4, T5, T6, T7, T8], [r"$t /\si{\second}$", r"$T_1 /\si{\degreeCelsius}$", r"$T_2 /\si{\degreeCelsius}$", r"$T_3 /\si{\degreeCelsius}$", r"$T_4 /\si{\degreeCelsius}$", r"$T_5 /\si{\degreeCelsius}$", r"$T_6 /\si{\degreeCelsius}$", r"$T_7 /\si{\degreeCelsius}$", r"$T_8 /\si{\degreeCelsius}$"], label="tab1", caption="Zeit gegen Temperaturen der einzelnen Elemente", roundPrecision=2)
tab1.writeFile("build/tab1.tex")


phasemax1, phasemin1= np.genfromtxt("data/datab1.txt", unpack=True)
links11, rechts11, links12, rechts12  = np.genfromtxt("data/datab2.txt", unpack=True)
phasemax11= ufloat(phasemax1.mean(), phasemax1.std())
phasemin11= ufloat(phasemin1.mean(), phasemin1.std())
phase12= (phasemax11+phasemin11)/2
amp11= links11+ rechts11 
amp21= links12+ rechts12 
amp1= ufloat(amp11.mean(), amp11.std())
amp2= ufloat(amp21.mean(), amp21.std())

phasemax2, phasemin2= np.genfromtxt("data/datac1.txt", unpack=True)
links21, rechts21, links22, rechts22  = np.genfromtxt("data/datac2.txt", unpack=True)
phasemax21= ufloat(phasemax2.mean(), phasemax2.std())
phasemin21= ufloat(phasemin2.mean(), phasemin2.std())
phase78= (phasemax21+phasemin21)/2
amp71= links21+ rechts21 
amp81= links22+ rechts22 
amp7= ufloat(amp71.mean(), amp71.std())
amp8= ufloat(amp81.mean(), amp81.std())

phasemax3, phasemin3= np.genfromtxt("data/datad1.txt", unpack=True)
links31, rechts31, links32, rechts32  = np.genfromtxt("data/datad2.txt", unpack=True)
phasemax31= ufloat(phasemax3.mean(), phasemax3.std())
phasemin31= ufloat(phasemin3.mean(), phasemin3.std())
phase56= (phasemax31+phasemin31)/2
amp51= links31+ rechts31 
amp61= links32+ rechts32 
amp5= ufloat(amp51.mean(), amp51.std())
amp6= ufloat(amp61.mean(), amp61.std())

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

Ampnah1= amp1/2*4
Ampfern1= amp2/2*4
delt1= phase12*50
phase1= 2*np.pi*delt1/80

Ampnah2= amp5/2*5/1.5
Ampfern2= amp6/2*5/1.5
delt2= phase56*50
phase2= 2*np.pi*delt2/80

Ampnah3= amp7/2*10/2.6 
Ampfern3= amp8/2*10/2.6
delt3= phase78*500/4
phase3= 2*np.pi*delt3/80
#functions 

#calculate 

delT12= (T2new-T1new)/L[0]
delT34= (T3new-T4new)/L[1]
delT56= (T6new-T5new)/L[2]
delT78= (T7new-T8new)/L[3]
delQ12= -K[0]*A[0]*delT12
delQ34= -K[1]*A[1]*delT34
delQ56= -K[2]*A[2]*delT56
delQ78= -K[3]*A[3]*delT78

K1= (rho[0]*c[0]*(L[0])**2)/(2*delt1*unp.log(Ampnah1/Ampfern1))
K2= (rho[2]*c[2]*(L[2])**2)/(2*delt2*unp.log(Ampnah2/Ampfern2))
K3= (rho[3]*c[3]*(L[3])**2)/(2*delt3*unp.log(Ampnah3/Ampfern3))
#save solution 

file = open("build/solution.txt", "w")
file.write("delQ12/delt= {} W\ndelQ34/delt= {} W\ndelQ56/delt= {} W\ndelQ78/delt= {} W\n\nMessing:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\nK= {}\n\nAluminium:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\nK= {}\n\nEdelstahl:\n\tAmpNah= {} K\n\tAmpFern= {} K\n\tdelt= {} s\n\tPhase= {}\nK= {}\n\n ".format(delQ12, delQ34, delQ56, delQ78, Ampnah1, Ampfern1, delt1, phase1, K1, Ampnah2, Ampfern2, delt2, phase2, K2, Ampnah3, Ampfern3, delt3, phase3, K3 ))
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

