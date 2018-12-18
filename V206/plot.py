import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
t, T1, pb, T2, pa, N = np.genfromtxt("data/dataa.txt", unpack=True)
tab1 = TexTable([t, T1, pb, T2, pa, Nmech], [r"$t /\si{\minute}$", r"$T_{1} /\si{\degree\celsius}", r"$p_{b} / \si{\bar}", r"T_{2} /\si{\degree\celsius}", r"p_{a} /\si{\bar}", r"N_{mech} /\si{\joule}"], label="tab1", caption="Die Temperatur in Reservoire 1 und Reservoir 2 und die dazugehörenden Drücke und die Leistungsaufnahme des Kompressors zu verschiedenen Zeitpunkten.", roundPrecision=2)
tab1.writeFile("build/tab1.tex")

p, T3 = np.genfromtxt("data/datad.txt", unpack=True)
#tab2 = TexTable([p,T3], [r"<++>", r"<++>"], label="tab<++>", caption="<++>", roundPrecision=<++>)
#tab<++>.writeFile("build/tab<++>.tex")

#extra values 
#d)
m1= <++> 
cw= <++> 
mk= <++>
ck= <++>
N= <++>

#e)
m2= <++> 
p0= <++>

#f)
rho= 5.51 
kappa= 1.14
#functions 

def function1(t, a, b, c):
     return a*t**2+ b*t + c 

def ableitung1(t, a, b):
    return 2*a*t+ b

def function2(t, a, b, c):
     return a/(1+b*(t**c)) 

def function3(t, a, b, c, d):
     return (a*(t**b))/(1+c*(t**b))+d 

def getL(T,x):
    return np.exp(-x/T)
#calculate 

#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)

#a) 
newt= np.linspace(t[0], t[-1], 200)

#b)
params1, pcov1 = curve_fit(function1, t, T1)
params2, pcov2 = curve_fit(function2, t, T2)

#c)
dT11 = ableitung1(t[0], params1[0], params1[1])
dT12 = ableitung1(t[5], params1[0], params1[1])
dT13 = ableitung1(t[10], params1[0], params1[1])
dT14 = ableitung1(t[15], params1[0], params1[1])

dT21 = ableitung1(t[0], params2[0], params2[1])
dT22 = ableitung1(t[5], params2[0], params2[1])
dT23 = ableitung1(t[10], params2[0], params2[1])
dT24 = ableitung1(t[15], params2[0], params2[1])

#d) 
v1 = ((m1*cw + mk*ck)*dT11)/N[0]
v2 = ((m1*cw + mk*ck)*dT12)/N[5]
v3 = ((m1*cw + mk*ck)*dT13)/N[10]
v4 = ((m1*cw + mk*ck)*dT14)/N[15]

vid1 = T1[0]/(T1[0]-T2[0])
vid2 = T1[5]/(T1[5]-T2[5])
vid3 = T1[10]/(T1[10]-T2[10])
vid4 = T1[15]/(T1[15]-T2[15])

#e)
params3, pcov3= curve_fit(getL, T3, p/p0)
L= -params3[0]/R
m1= ((m2*cw + mk*ck)*dT21)/L
m2= ((m2*cw + mk*ck)*dT22)/L
m3= ((m2*cw + mk*ck)*dT23)/L
m4= ((m2*cw + mk*ck)*dT24)/L

#f)
Nmech1 = (1/(kappa-1))*(pb[0]*(pa[0]/pb[0])**(1/kappa) - pa[0])*(1/rho)*m1
Nmech2 = (1/(kappa-1))*(pb[5]*(pa[5]/pb[5])**(1/kappa) - pa[5])*(1/rho)*m2
Nmech3 = (1/(kappa-1))*(pb[10]*(pa[10]/pb[10])**(1/kappa) - pa[10])*(1/rho)*m3
Nmech4 = (1/(kappa-1))*(pb[15]*(pa[15]/pb[15])**(1/kappa) - pa[15])*(1/rho)*m4

#save solution 

file = open("build/solution.txt", "w")
file.write("a) Plots\n\nb)\n\tFitparameter A,B,C (T1) = {} \n\tFehler: {}\n\t Fitparameter (T2)= {}\n\tFehler: {} \nc)\n\tdT1(0)= {} dT1(5)= {} dT1(10)= {} dT1(15)= {}\n\t dT2(0)= {} dT2(5)= {} dT2(10)= {} dT2(15)= {}\n\nd)\n\t Gütefaktoren: \n\tReal:\n\t v1 ={} v2={} v3={} v4={}\n\t Ideal: \n\t v1={} v2={} v3={} v4={} \n\ne)\n\t L= {}\n\tMassendurchsatz dm/dt\n\tm1= {} m2={} m3={} m4={} \n\nf)\n\t N1={} N2={} N3={} N4={}".format(params1, np.sqrt(np.diag(pcov1)), params2, np.sqrt(np.diag(pcov2)),dT11, dT12, dT13, dT14, dT21, dT22, dT23, dT24, v1, v2, v3, v4, vid1, vid2, vid3, vid4, L, m1, m2, m3, m4, N1, N2, N3, N4))
file.close()

#Make plots for data
plt.figure(1)
plt.plot(t, T1, "xr", label="Daten")
plt.plot(newt, function1(newt, *params1), "r", label="Fit", linewidth=1.0)
plt.plot(t, T2, "xg", label="Daten")
plt.plot(newt, function1(newt, *params2), "g", label="Fit", linewidth=1.0)
plt.xlabel(r"$t/\si{\minute}$")
plt.ylabel(r"$T_{1} / \si{\degree\celsius}$")
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

