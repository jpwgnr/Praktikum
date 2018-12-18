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
tab1 = TexTable([t, T1, pb, T2, pa, N], [r"$t /\si{\minute}$", r"$T_{1} /\si{\degree\celsius}", r"$p_{b} / \si{\bar}", r"T_{2} /\si{\degree\celsius}", r"p_{a} /\si{\bar}", r"N /\si{\watt}"], label="tab1", caption="Die Temperatur in Reservoire 1 und Reservoir 2 und die dazugehörenden Drücke und die Leistungsaufnahme des Kompressors zu verschiedenen Zeitpunkten.", roundPrecision=2)
tab1.writeFile("build/tab1.tex")

tsi= t*60 
T1si= T1+273.15
pasi= pa*1e5
T2si= T2+273.15 
pbsi= pb*1e5

terr = ufloat(tsi, 0.5)
T1err = ufloat(T1si, 1)
paerr = ufloat(pasi, 0.1e5)
T2err = ufloat(T2si, 1)
pberr = ufloat(pbsi, 0.1e5)
Nerr = ufloat(N, 5)

p, T3 = np.genfromtxt("data/datad.txt", unpack=True)
tab2 = TexTable([p,T3], [r"p / \si{\bar}", r"T /\si{\degree\celsius}"], label="tab2", caption="Druck und Temperaturskala gegeneinander aufgetragen.", roundPrecision=2)
tab2.writeFile("build/tab2.tex")
psi= p*1e5
T3si= T3+273.15 
perr= ufloat(psi, 0.1e5)
T3err= ufloat(T3si, 1)


#extra values 
#d)
m1= ufloat(1, 0.0004) 
cw= 4.182  
mk= 1
ck= 750

#e)
m2= ufloat(1, 0.0004) 
p0= 1
 

#f)
rho= 5.51 
kappa= 1.14
#functions 

def function1(t, a, b, c, d):
     return a*t**3+ b*t**2 + c*t+ d  

def ableitung1(t, a, b, c):
    return 3*a*t**2+ b*t + c

def function2(t, a, b, c):
     return a/(1+b*(t**c)) 

def function3(t, a, b, c, d):
     return (a*(t**b))/(1+c*(t**b))+d 

def getL(T,L):
    return -(L/R)*(1/T)
#calculate 

#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)

#a) 
newt= np.linspace(tsi[0], tsi[-1], 200)

#b)
params1, pcov1 = curve_fit(function1, tsi, T1si)
params2, pcov2 = curve_fit(function2, tsi, T2si)
param1err= np.sqrt(np.diag(pcov1))
param10= ufloat(params1[0],param1err[0])
param11= ufloat(params1[1],param1err[1])
param12= ufloat(params1[2],param1err[2])
param2err= np.sqrt(np.diag(pcov2))
param20= ufloat(params2[0], param2err[0])
param21= ufloat(params2[1], param2err[1])
param22= ufloat(params2[2], param2err[2])

#c)
dT11 = ableitung1(terr[0], params10, params11, params12)
dT12 = ableitung1(terr[5], params10, params11, params12)
dT13 = ableitung1(terr[10], params10, params11, params12)
dT14 = ableitung1(terr[15], params10, params11, params12)

dT21 = ableitung1(terr[0], params20, params21, params22)
dT22 = ableitung1(terr[5], params20, params21, params22)
dT23 = ableitung1(terr[10], params20, params21, params22)
dT24 = ableitung1(terr[15], params20, params21, params22)

#d) 
v1 = ((m1*cw + mk*ck)*dT11)/Nerr[0]
v2 = ((m1*cw + mk*ck)*dT12)/Nerr[5]
v3 = ((m1*cw + mk*ck)*dT13)/Nerr[10]
v4 = ((m1*cw + mk*ck)*dT14)/Nerr[15]

vid1 = T1err[0]/(T1err[0]-T2err[0])
vid2 = T1err[5]/(T1err[5]-T2err[5])
vid3 = T1err[10]/(T1err[10]-T2err[10])
vid4 = T1err[15]/(T1err[15]-T2err[15])

#e)
params3, pcov3= curve_fit(getL, T3si ,np.log(psi))
params3err= np.sqrt(np.diag(pcov3))
L= ufloat(params3[0],params3err[0]) 
m1= ((m2*cw + mk*ck)*dT21)/L
m2= ((m2*cw + mk*ck)*dT22)/L
m3= ((m2*cw + mk*ck)*dT23)/L
m4= ((m2*cw + mk*ck)*dT24)/L

#f)

rho0= 5.51/18.01528
rho1= (paerr[0]*rho0*273.15)/(1e5*T2err[0])
rho2= (paerr[5]*rho0*273.15)/(1e5*T2err[5])
rho3= (paerr[10]*rho0*273.15)/(1e5*T2err[10])
rho4= (paerr[15]*rho0*273.15)/(1e5*T2err[15])

Nmech1 = (1/(kappa-1))*(pberr[0]*(paerr[0]/pberr[0])**(1/kappa) - paerr[0])*(1/rho1)*m1
Nmech2 = (1/(kappa-1))*(pberr[5]*(paerr[5]/pberr[5])**(1/kappa) - paerr[5])*(1/rho2)*m2
Nmech3 = (1/(kappa-1))*(pberr[10]*(paerr[10]/pberr[10])**(1/kappa) - paerr[10])*(1/rho3)*m3
Nmech4 = (1/(kappa-1))*(pberr[15]*(paerr[15]/pberr[15])**(1/kappa) - paerr[15])*(1/rho4)*m4

#save solution 

file = open("build/solution.txt", "w")
file.write("a) Plots\n\nb)\n\tFitparameter A,B,C (T1) = {} \n\tFehler: {}\n\t Fitparameter (T2)= {}\n\tFehler: {} \nc)\n\tdT1(0)= {} dT1(5)= {} dT1(10)= {} dT1(15)= {}\n\t dT2(0)= {} dT2(5)= {} dT2(10)= {} dT2(15)= {}\n\nd)\n\t Gütefaktoren: \n\tReal:\n\t v1 ={} v2={} v3={} v4={}\n\t Ideal: \n\t v1={} v2={} v3={} v4={} \n\ne)\n\t L= {}\n\tMassendurchsatz dm/dt\n\tm1= {} m2={} m3={} m4={} \n\nf)\n\t N1={} N2={} N3={} N4={}".format(params1, np.sqrt(np.diag(pcov1)), params2, np.sqrt(np.diag(pcov2)),dT11, dT12, dT13, dT14, dT21, dT22, dT23, dT24, v1, v2, v3, v4, vid1, vid2, vid3, vid4, L, m1, m2, m3, m4, N1, N2, N3, N4))
file.close()

#Make plots for data
plt.figure(1)
plt.errorbar(tsi, T1si, yerr=1, xerr=0.5, fmt='rx', label='Daten')
plt.plot(newt, function1(newt, *params1), "r", label="Fit", linewidth=1.0)
plt.errorbar(tsi, T2si, yerr=1,xerr=0.5,  fmt='rx', label='Daten')
plt.plot(newt, function1(newt, *params2), "g", label="Fit", linewidth=1.0)
plt.xlabel(r"$t/\si{\second$")
plt.ylabel(r"$T_{1} / \si{\kelvin}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

#curvefit plot
T3sinew= np.linspace(T3si[0], T3si[-1], 200)
plt.errorbar(1/T3si, np.log(psi),xerr=1, yerr=0.1e5, fmt='rx', label='Daten')
plt.plot(1/T3si, f(T3si, *parameters), 'b-', label='Fit')
plt.xlabel(r'$T / \si{\kelvin}$')
plt.ylabel(r'$p / \si{\pascal}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot2.pdf")

