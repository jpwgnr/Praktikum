import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
import scipy.constants as const 
#Generate data 

#from txt
#a)
B1lang, x1lang= np.genfromtxt("data/dataa1.txt", unpack=True)
taba1 = TexTable([B1lang*1e3,x1lang*1e2], [r"$B$/ \si{\milli\tesla}", r"$x$/ \si{\centi\meter}"], label="taba1", caption=r"Der magnetische Fluss $B$ an verschiedenen Stellen $x$ in der langen Spule.", roundPrecision=3)
taba1.writeFile("build/taba1.tex")

B1kurz, x1kurz= np.genfromtxt("data/dataa2.txt", unpack=True)
taba2 = TexTable([B1kurz,x1kurz], [r"$B$/ \si{\milli\tesla}", r"$x$/ \si{\centi\meter}"], label="taba2", caption=r"Der magnetische Fluss $B$ an verschiedenen Stellen $x$ in der kurzen Spule.", roundPrecision=3)
taba2.writeFile("build/taba2.tex")

#b)
B2r, x2r = np.genfromtxt("data/datab1.txt", unpack=True)
tabb1 = TexTable([B2r*1e3,x2r*1e2], [r"$B$/ \si{\milli\tesla}", r"$x$/ \si{\centi\meter}"], label="tabb1", caption=r"Der magnetische Fluss $B$ an verschiedenen Stellen $x$ in- und außerhalb des Spulenpaares bei einem Abstand von \SI{3.125}{\centi\meter} und einem Strom $I$ von \SI{4}{\ampere}", roundPrecision=3)
tabb1.writeFile("build/tabb1.tex")

B2d, x2d = np.genfromtxt("data/datab2.txt", unpack=True)
tabb2 = TexTable([B2d*1e3,x2d*1e2], [r"$B$/ \si{\milli\tesla}", r"$x$/ \si{\centi\meter}"], label="tabb2", caption=r"Der magnetische Fluss $B$ an verschiedenen Stellen $x$ in- und außerhalb des Spulenpaares bei einem Abstand von \SI{6.25}{\centi\meter} und einem Strom $I$ von \SI{4}{\ampere}", roundPrecision=3)
tabb2.writeFile("build/tabb2.tex")

B23, x23 = np.genfromtxt("data/datab3.txt", unpack=True)
tabb3 = TexTable([B23*1e3,x23*1e2], [r"$B$/ \si{\milli\tesla}", r"$x$/ \si{\centi\meter}"], label="tabb3", caption=r"Der magnetische Fluss $B$ an verschiedenen Stellen $x$ in- und außerhalb des Spulenpaares bei einem Abstand von \SI{6.25}{\centi\meter} und einem Strom $I$ von \SI{3}{\ampere}", roundPrecision=3)
tabb3.writeFile("build/tabb3.tex")

#c)
B3, I3 = np.genfromtxt("data/datac.txt", unpack=True)
tabc = TexTable([B3*1e3,I3], [r"$B$/ \si{\milli\tesla}", r"$I$/ \si{\ampere}"], label="tabc", caption=r"Der magnetische Fluss $B$ des gemessenen Magnetfelds gegen den Strom $I$ des erzeugenden Magnetfelds", roundPrecision=1)
tabc.writeFile("build/tabc.tex")

#extra values 
#a)
#lang
n1lang=300
l1lang=24e-2
mu_rlang=1
mu_0=4*np.pi*1e-7 
Ilang= 1
#kurz
n1kurz=300
l1kurz=24e-2
mu_rkurz=1
Ikurz= 1

#b) 
R2=6.25e-2
n2=100
d21=3.125e-2
d22=6.5e-2 
I21=4
I23=3
#c)
Spalt= 3e-3 #mm
n3= 595 

#functions 

#a)
def getBlong(mu_r, mu_0, n, l, I):
    return mu_r*mu_0*(n/l)*I

#b)
def getBhelm(mu_0, I, n, R, x):
    return n*mu_0*I*(R**2)/((R**2+x**2)**(3/2))

def getBhelmgrad(mu_0, I, n, R, x):
    return (-3*mu_0*I*R**2*x)/((R**2+x**2)**(5/2))

def getBtorus(mu_r, mu_0, n, R, I):
    return mu_r*mu_0*(n/(2*np.pi*R)*I)

#def f(x, a, b, c, d):
#    return a * np.sin(b * x + c) + d


#calculate 
#a)
parameterslang, pcovlang = curve_fit(getBlong, x1lang, B1lang)

parameterskurz, pcovkurz = curve_fit(getBlong, x1kurz, B1kurz)

#b) 
parametersHelm1, pcovHelm1 = curve_fit(getBhelm, x2r, B2r)

parametersHelm2, pcovHelm2 = curve_fit(getBhelm, x2d, B2d)

parametersHelm3, pcovHelm3 = curve_fit(getBhelm, x23, B23)

#c)
parametersTorus, pcovTorus = curve_fit(getBtorus, I3, B3)

#allgemeine Rechnungen
#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
 
#parameters, pcov = curve_fit(f, x, y, sigma=err_x)

#save solution 

#file = open("build/solution.txt", "w")
#file.write("Steigung = {} Fehler: {}".format(Steigung1, np.sqrt(np.diag(pcov)) ))
#file.close()

#Make plots for data
#a)
plt.figure(1)
plt.plot(x1lang*1e2, B1lang*1e3, "xr", label="Daten")
#plt.plot(x1, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plota1.pdf")

plt.figure(2)
plt.plot(x1kurz*1e2, B1kurz*1e3, "xr", label="Daten")
#plt.plot(x1, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plota2.pdf")

#b)
plt.figure(3)
plt.plot(x2r*1e2, B2r*1e3, "xr", label="Daten")
#plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotb1.pdf")

plt.figure(4)
plt.plot(x2d*1e2, B2d*1e3, "xr", label="Daten")
#plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotb2.pdf")

plt.figure(5)
plt.plot(x23*1e2, B23*1e3, "xr", label="Daten")
#plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotb3.pdf")

#c)
plt.figure(6)
plt.plot(I3, B3*1e3, "xr", label="Daten")
#plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$I/\si{\ampere}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotc.pdf")

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

