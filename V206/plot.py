import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import R 
import uncertainties.unumpy as unp
from table import TexTable
from uncertainties import ufloat
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
t, T1, pa1, T2, pb1, N = np.genfromtxt("data/dataa.txt", unpack=True)
pa= pa1+1
pb= pb1+1
tab1 = TexTable([t, T1, pb, T2, pa, N], [r"$t /\si{\minute}$", r"$T_{1} /\si{\degreeCelsius}$", r"$p_{b} / \si{\bar}$", r"$T_{2} /\si{\degreeCelsius}$", r"$p_{a} /\si{\bar}$", r"$N /\si{\watt}$"], label="tab1", caption="Die Temperatur in Reservoir 1 und Reservoir 2 und die dazugehörenden Drücke und die Leistungsaufnahme des Kompressors zu verschiedenen Zeitpunkten.", roundPrecision=1)
tab1.writeFile("build/tab1.tex")

tsi= t*60 
T1si= T1+273.15
pasi= pa*1e5
T2si= T2+273.15 
pbsi= pb*1e5

terr = unp.uarray(tsi, 0.5)
T1err = unp.uarray(T1si, 1)
paerr = unp.uarray(pasi, 0.1e5)
T2err = unp.uarray(T2si, 1)
pberr = unp.uarray(pbsi, 0.1e5)
Nerr = unp.uarray(N, 5)

p, T3 = np.genfromtxt("data/datad.txt", unpack=True)
tab2 = TexTable([p,T3], [r"p / \si{\bar}", r"T /\si{\degreeCelsius}"], label="tab2", caption="Druck und Temperaturskala gegeneinander aufgetragen.", roundPrecision=2)
tab2.writeFile("build/tab2.tex")
psi= p*1e5
T3si= T3+273.15 
perr= unp.uarray(psi, 0.1e5)
T3err= unp.uarray(T3si, 1)


#extra values 
#d)
m1= ufloat(1, 0.0004) 
cw= 4182  
mk= 1
ck= 750

#e)
m2= ufloat(1, 0.0004) 
p0= 1
 

#f)
rho= 5.51*1000 
kappa= 1.14
#functions 

def function1(t, a, b, c, d):
     return a*t**3+ b*t**2 + c*t+ d  

def ableitung1(t, a, b, c):
    return 3*a*t**2+2*b*t + c

def function2(t, a, b, c):
     return a/(1+b*(t**c)) 

def function3(t, a, b, c, d):
     return (a*(t**b))/(1+c*(t**b))+d 

#def getL(x,L):
 #   return -(L/R)*x

def getL(m,x,n):
    return m*x+n
#calculate 

#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)

#a) 
newt= np.linspace(tsi[0], tsi[-1], 200)

#b)
params1, pcov1 = curve_fit(function1, tsi, T1si)
params2, pcov2 = curve_fit(function1, tsi, T2si)
param1err= np.sqrt(np.diag(pcov1))
param10= ufloat(params1[0],param1err[0])
param11= ufloat(params1[1],param1err[1])
param12= ufloat(params1[2],param1err[2])
param2err= np.sqrt(np.diag(pcov2))
param20= ufloat(params2[0], param2err[0])
param21= ufloat(params2[1], param2err[1])
param22= ufloat(params2[2], param2err[2])

#c)
dT11 = ableitung1(terr[1], param10, param11, param12)
dT12 = ableitung1(terr[5], param10, param11, param12)
dT13 = ableitung1(terr[10], param10, param11, param12)
dT14 = ableitung1(terr[15], param10, param11, param12)

dT21 = ableitung1(terr[1], param20, param21, param22)
dT22 = ableitung1(terr[5], param20, param21, param22)
dT23 = ableitung1(terr[10], param20, param21, param22)
dT24 = ableitung1(terr[15], param20, param21, param22)

#d) 
v1 = ((m1*cw + mk*ck)*dT11)/Nerr[1]
v2 = ((m1*cw + mk*ck)*dT12)/Nerr[5]
v3 = ((m1*cw + mk*ck)*dT13)/Nerr[10]
v4 = ((m1*cw + mk*ck)*dT14)/Nerr[15]

vid1 = T1err[1]/(T1err[1]-T2err[1])
vid2 = T1err[5]/(T1err[5]-T2err[5])
vid3 = T1err[10]/(T1err[10]-T2err[10])
vid4 = T1err[15]/(T1err[15]-T2err[15])

#e)

Steigung3, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(1/(T3si*R),np.log(psi))
L= ufloat(Steigung3,std_err1) 
m1= ((m2*cw + mk*ck)*dT21)/L
m2= ((m2*cw + mk*ck)*dT22)/L
m3= ((m2*cw + mk*ck)*dT23)/L
m4= ((m2*cw + mk*ck)*dT24)/L

#f)

rho0= 5.51/120.91
rho1= (paerr[1]*rho0*273.15)/(1e5*T2err[1])
rho2= (paerr[5]*rho0*273.15)/(1e5*T2err[5])
rho3= (paerr[10]*rho0*273.15)/(1e5*T2err[10])
rho4= (paerr[15]*rho0*273.15)/(1e5*T2err[15])

Nmech1 = (1/(kappa-1))*(pberr[1]*(paerr[1]/pberr[1])**(1/kappa) - paerr[1])*(1/rho1)*m1/1000
Nmech2 = (1/(kappa-1))*(pberr[5]*(paerr[5]/pberr[5])**(1/kappa) - paerr[5])*(1/rho2)*m2/1000
Nmech3 = (1/(kappa-1))*(pberr[10]*(paerr[10]/pberr[10])**(1/kappa) - paerr[10])*(1/rho3)*m3/1000
Nmech4 = (1/(kappa-1))*(pberr[15]*(paerr[15]/pberr[15])**(1/kappa) - paerr[15])*(1/rho4)*m4/1000

#save solution 

file = open("build/solution.txt", "w")
file.write("a) Plots\n\nb)\n\tFitparameter A,B,C,D (T1) = {} \n\tFehler: {}\n\tFitparameter A,B,C,D (T2)= {}\n\tFehler: {} \nc)\n\tdT1(1)={}\tdT1(5)={}\tdT1(10)={}\tdT1(15)={}\n\tdT2(0)={}\tdT2(5)={}\tdT2(10)={}\tdT2(15)={}\n\nd)\n\tGütefaktoren:\n\tReal:\n\tv1={}\tv2={}\tv3={}\tv4={}\n\tIdeal:\n\tv1={}\tv2={}\tv3={}\tv4={}\n\ne)\n\tL={}\n\tMassendurchsatz dm/dt:\n\tm1={}\tm2={}\tm3={}\tm4={}\n\nf)\n\tN1={}\tN2={}\tN3={}\tN4={}".format(params1, np.sqrt(np.diag(pcov1)), params2, np.sqrt(np.diag(pcov2)),dT11, dT12, dT13, dT14, dT21, dT22, dT23, dT24, v1, v2, v3, v4, vid1, vid2, vid3, vid4, L, m1, m2, m3, m4, Nmech1, Nmech2, Nmech3, Nmech4))
file.close()


tabd = TexTable([1/T3si ,np.log(psi)], [r"\frac{1}{T}/ \si[per-mode=fraction]{\per\kelvin}", r"log(p/p0)"], label="tabd", caption="Die Temperatur und der logarithmierte Druck gegeneinander aufgetragen.", roundPrecision=2)
tabd.writeFile("build/tabd.tex")

#Make plots for data
plt.figure(1)
plt.errorbar(tsi, T1si, yerr=1, xerr=0.5, fmt='rx', label='Daten')
plt.plot(newt, function1(newt, *params1), "r--", label="Fit", linewidth=1.0)
plt.errorbar(tsi, T2si, yerr=1,xerr=0.5,  fmt='gx', label='Daten')
plt.plot(newt, function1(newt, *params2), "g--", label="Fit", linewidth=1.0)
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$T/\si{\kelvin}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

#curvefit plot
plt.figure(2)
T3sinew= np.linspace(T3si[0], T3si[-1], 200)
plt.errorbar(1/T3si, np.log(psi), fmt='rx', label='Daten')
plt.plot(1/T3sinew, getL(Steigung3, 1/(T3sinew*R), yAbschnitt1), 'b--', label='Fit')
plt.xlabel(r'$\frac{1}{T}/ \si[per-mode=fraction]{\per\kelvin}$')
plt.ylabel(r'$log(p)$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot2.pdf")

