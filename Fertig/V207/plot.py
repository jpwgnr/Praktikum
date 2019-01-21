import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
from math import *
#Generate data 

#from txt
t1small, t1big = np.genfromtxt("data/dataa.txt", unpack=True)
tab1 = TexTable([t1small,t1big], [r"$t_\text{klein} /\si{\second}$", r"$t_\text{groß} /\si{\second}$"], label="tab1", caption= r"Die Falldauer der kleinen Kugel und die Falldauer der großen Kugel.", roundPrecision=1)
tab1.writeFile("build/tab1.tex")

T11, t1 = np.genfromtxt("data/datab.txt", unpack=True)
T1= T11+273.15
tab2 = TexTable([T1,t1], [r"$T_1 /\si{\kelvin}$", r"$t /\si{\second}$"], label="tab2", caption= r"Die Fallzeit in Abhängigkeit zur Temperatur der Flüssigkeit.", roundPrecision=1)
tab2.writeFile("build/tab2.tex")

T21, t2 = np.genfromtxt("data/datac.txt", unpack=True)
T2= T21+273.15
tab3 = TexTable([T2,t2], [r"$T_2 /\si{\kelvin}$", r"$t /\si{\second}$"], label="tab3", caption= r"Die Fallzeit in Abhängigkeit zur Temperatur der Flüssigkeit.", roundPrecision=1)
tab3.writeFile("build/tab3.tex")
#extra values 
#a)
mbig=4.21/1000 #kg
msmall=3.71/1000 #kg
Vbig=(0.0158/2)**3 *(4/3)*np.pi #m^3
Vsmall=(0.0156/2)**3 * (4/3) *np.pi #m^3

#b)
rhoFl= 0.9982067*1000 # kg/m^3
x = 0.1 #m 
Ksmall= 0.07640*1e-6 #Pa/kg *m^3

#e)
dbig= 0.0158
dsmall= 0.0156
#functions 

def getEta(T, A, B):
    return np.log(A*np.exp(B*T)) 

#calculate 
#a)
rhobig= mbig/Vbig 
rhosmall = msmall/Vsmall 

#b)
tsmall=ufloat(t1small.mean(), t1small.std())
tbig= ufloat(t1big.mean(), t1big.std())

#c)
eta= Ksmall* (rhosmall- rhoFl)*tsmall
Kbig= eta/((rhobig-rhoFl)*tbig)

#d) 
eta1=Kbig*(rhobig- rhoFl)*t1 
eta2=Kbig*(rhobig- rhoFl)*t2 

eta11=Kbig.nominal_value*(rhobig- rhoFl)*t1 
eta21=Kbig.nominal_value*(rhobig- rhoFl)*t2 
vwater1= x/tsmall
vwater2= x/tbig
vwater21= x/t1
vwater22= x/t2

#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
params1, pcov1 = curve_fit(getEta, 1/T1,np.log(eta11))
params2, pcov2 = curve_fit(getEta, 1/T2,np.log(eta21))
paramserr1= np.sqrt(np.diag(pcov1))
paramserr2= np.sqrt(np.diag(pcov2))

newT1= np.linspace(T1[0]-3, T1[-1]+3, 200)
newT2= np.linspace(T2[0]-3, T2[-1]+3, 200)

#e)
rey1=(rhoFl*dsmall*vwater1)/eta 
rey2=(rhoFl*dbig*vwater2)/eta 
rey21=(rhoFl*dbig*vwater21)/eta1 
rey22=(rhoFl*dbig*vwater22)/eta2 


#save solution 

tab4 = TexTable([eta1*1e3,eta2*1e3], [r"$\eta_1 /\si{\milli\pascal\second}$", r"$\eta_2 /\si{\milli\pascal\second}$"], label="tab4", caption= r"Die Viskosität für die erste und zweite Messung.", roundPrecision=3)
tab4.writeFile("build/tab4.tex")

tab5 = TexTable([1e3/T1, unp.log(eta1)], [r"$\frac{10^{3}}{T_1} /\si[per-mode=fraction]{\per\kelvin}$", r"$ln(\eta_1) /\si{\pascal\second}$"], label="tab5", caption= r"Die invertierte Temperatur gegen die logarithmierte Viskosität für die erste Messung.", roundPrecision=1)
tab5.writeFile("build/tab5.tex")

tab6 = TexTable([1e3/T2, unp.log(eta2)], [r"$\frac{10^{3}}{T_2} /\si[per-mode=fraction]{\per\kelvin}$", r"$ln(\eta_2) /\si{\pascal\second}$"], label="tab6", caption= r"Die invertierte Temperatur gegen die logarithmierte Viskosität für die zweite Messung.", roundPrecision=1)
tab6.writeFile("build/tab6.tex")

tab7 = TexTable([T1, rey21, rey22], [r"$T /\si{\kelvin}$", r"$Re_1$", r"$Re_2$"], label="tab7", caption= r"Die Temperatur und die Reynoldszahlen der erste und zweite Messung.", roundPrecision=2)
tab7.writeFile("build/tab7.tex")


file = open("build/solution.txt", "w")
file.write("Dichte_klein= {} kg/m^3\nDichte_groß= {} kg/m^3\nDichte_Fl= {} kg/m^3\nDurchmesser_klein= {} m\nDurchmesser_groß= {} m\nt_klein= {} s\nt_groß= {} s\nK_klein= {} Pa*m^3/kg\nK_groß= {} Pa*m^3/kg\nEta_klein= {} Pa*s\nA1= {} +/- {} Pa*s\nB1= {} +/- {} K\nA2= {} +/- {} Pa*s\nB2= {} +/- {} K\nv_klein= {} m/s\nv_groß= {} m/s\nReynoldsche Zahl Kugel_small= {}\nReynoldsche Zahl Kugel_big= {}".format(rhosmall, rhobig, rhoFl, dsmall, dbig, tsmall, tbig, Ksmall, Kbig, eta, params1[0], paramserr1[0], params1[1], paramserr1[1], params2[0], paramserr2[0], params2[1], paramserr2[1], vwater1, vwater2, rey1, rey2))
file.close()

#Make plots for data
plt.figure(1)
plt.plot(1/T1, np.log(eta11), "xr", label="Daten")
plt.plot(1/newT1, getEta(1/newT1, *params1), "r--", label="Ausgleichsgerade", linewidth=1.0)
plt.xlabel(r"$\frac{1}{T} /\si[per-mode=fraction]{\per\kelvin}$")
plt.ylabel(r"$ln(\eta)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

plt.figure(2)
plt.plot(1/T2, np.log(eta21), "xr", label="Daten")
plt.plot(1/newT2, getEta(1/newT2, *params2), "r--", label="Ausgleichsgerade", linewidth=1.0)
plt.xlabel(r"$\frac{1}{T} /\si[per-mode=fraction]{\per\kelvin}$")
plt.ylabel(r"$ln(\eta)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot2.pdf")

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

