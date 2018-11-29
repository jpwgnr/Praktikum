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
l1lang=<++>
mu_rlang=1
mu_0=4*np.pi*1e-7 
Ilang= 1
explangBmax= <++>

#kurz
n1kurz=<++>
l1kurz=<++>
mu_rkurz=1
Ikurz= 1
expkurzmax=<++>
expkurzBmax= <++>

#b) 
R2=<++>
n2=100
d21=3.125e-2
d22=6.5e-2 
I21=4
I23=3
exphelmB1=<++>
exphelmx1=<++>
exphelmB2=<++>
exphelmlinks=<++>
exphelmB3=<++>
exphelmrechts=<++>

#c)
Spalt= 3e-3 #mm
n3= 595 

#functions 

#a)
def allgB(x, mu_0, I, R, n, p):
    return ((mu_0*I)/2)*(R**2/((R**2+(x-p)**2)**(3/2)))*n

def allgB2(x, mu_0, I, R, n, p, q):
    return ((mu_0*I)/2)*(R**2/((R**2+(x-p)**2)**(3/2)))*n+((mu_0*I)/2)*(R**2/((R**2+(x-q)**2)**(3/2)))*n

def getBlong(mu_r, mu_0, n, l, I):
    return mu_r*mu_0*(n/l)*I

#b)
def getBhelm(mu_0, I, n, R, x):
    return 2*n*mu_0*I*(R**2)/((R**2+x**2)**(3/2))

def getBhelmgrad(mu_0, I, n, R, x):
    return (-3*mu_0*I*R**2*x)/((R**2+x**2)**(5/2))

def getBtorus(mu_r, mu_0, n, R, I):
    return mu_r*mu_0*(n/(2*np.pi*R)*I)

#def f(x, a, b, c, d):
#    return a * np.sin(b * x + c) + d


#calculate 
#a)
theoBlang= getBlong(1, mu_0, n1lang, l1lang, Ilang)

#parameterslang, pcovlang = curve_fit(getBlong, x1lang, B1lang)

theox1kurz= np.linspace(x1kurz[0], x1kurz[-1], 200)
theoBkurz= allgB(theox1kurz, mu_0, Ikurz, Rkurz, n1kurz, expkurzmax)

parameterskurz, pcovkurz = curve_fit(allgB, x1kurz*1e2, B1kurz*1e3)

#b) 

theoBhelmmitte1 = getBhelm(mu_0, I21,n2, R2,d21)
theoBhelmmitte2 = getBhelm(mu_0, I21,n2, R2,d22)
theoBhelmmitte3 = getBhelm(mu_0, I23,n2, R2,d22)

theohelmx2r=np.linspace(x2r[0], x2r[-1], 200)
theohelmx2d=np.linspace(x2d[0], x2d[-1], 200)
theohelmx23= np.linspace(x23[0],x23[-1], 200)

theoBhelm1= allgB(theohelmx2r, mu_0, I21, R2, n2, exphelm1)
theoBhelm2= allgB2(theohelmx2d, mu_0, I21, R2, n2, exphelmlinks, exphelmrechts)
theoBhelm3= allgB2(theohelmx23, mu_0, I23, R2, n2, exphelmlinks, exphelmrechts)

parametersHelm1, pcovHelm1 = curve_fit(allgB, x2r, B2r)

parametersHelm2, pcovHelm2 = curve_fit(allgB2, x2d*1e2, B2d*1e3)

parametersHelm3, pcovHelm3 = curve_fit(allgB2, x23*1e2, B23*1e3)

#c)
#parametersTorus, pcovTorus = curve_fit(getBtorus, I3, B3)
#abgelesene Ergebnisse: 

SaetMag= <++> 
Rema= <++>
Koerz= <++>

#allgemeine Rechnungen
#Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
 
#parameters, pcov = curve_fit(f, x, y, sigma=err_x)

#save solution 

file = open("build/solution.txt", "w")
file.write("a) \n\tExperimental:\n\t\tLange Spule B= {} T\n\t\tKurze Spule B max= {} T\n\n\tTheoretisch:\n\t\tLange Spule B= {} T\n\t\tKurze Spule B max= {} T\n\nb)\n\tExperimental:\n\t\tMittePaar r B= {} T\n\t\tMittePaar d B= {} T\n\t\tMitte Paar d2 B= {} T\n\n\t Theorie:\n\tTheorie:\n\t\tMitte Paar r B= {} T\n\t\t Mitte Paar d B= {} T\n\t\tMitte Paar d2 B= {} T\n\nc)\n\t Ergebnis aus Graph:\n\t\tSättigungsmagnetisierung= {} T\n\t\tRemanenz= {} T\n\t\tStromstärke bei Koerzitivkraft= {} A".format(explangBmax, expkurzBmax, theoBlang, theoBkurz, exphelmB1, exphelmB2, exphelmB3, theoBhelmmitte1, theoBhelmmitte2, theoBhelmmitte3, SaetMag, Rema, Koerz ))
file.close()

#Make plots for data
#a)
plt.figure(1)
plt.plot(x1lang*1e2, B1lang*1e3, "xr", label="Daten")
#plt.plot(t, f(t, *parameters), 'b-', label='Fit')
plt.plot(x1lang*1e2, theoBlang*1e3, "r", label="Fit", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plota1.pdf")

plt.figure(2)
plt.plot(x1kurz*1e2, B1kurz*1e3, "xr", label="Daten")
plt.plot(theox1kurz*1e2, allgB(theox1kurz*1e2, *parameterskurz), 'b-', label='Fit')
plt.plot(theox1kurz*1e2, theoBkurz*1e3, "r", label="Theoriekurve", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plota2.pdf")

#b)
plt.figure(3)
plt.plot(x2r*1e2, B2r*1e3, "xr", label="Daten")
plt.plot(theohelmx2r*1e2, allgB(x2r*1e2, *parametersHelm1), 'b-', label='Fit')
plt.plot(theohelmx2r*1e2, theoBhelm1, "r", label="Theoriekurve", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotb1.pdf")

plt.figure(4)
plt.plot(x2d*1e2, B2d*1e3, "xr", label="Daten")
plt.plot(theohelmx2d*1e2, allgB2(theohelmx2d*1e2, *parametersHelm2), 'b-', label='Fit')
plt.plot(theohelmx2d*1e2, theoBhelm2, "r", label="Theoriekurve", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotb2.pdf")

plt.figure(5)
plt.plot(x23*1e2, B23*1e3, "xr", label="Daten")
plt.plot(theohelmx23*1e2, allgB2(theohelmx23*1e2, *parametersHelm3), 'b-', label='Fit')
plt.plot(theohelmx23*1e2, theoBhelm3, "r", label="Theoriekurve", linewidth=1.0)
plt.xlabel(r"$x/\si{\centi\meter}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotb3.pdf")

#c)
plt.figure(6)
plt.plot(I3[11:-1], B3[11:-1]*1e3, "r-", label="Hysteresekurve")
plt.plot(I3[0:10], B3[0:10]*1e3, 'b-', label='Neukurve')
plt.xlabel(r"$I/\si{\ampere}$")
plt.ylabel(r"$B/\si{\milli\tesla}$")
plt.Axes.set_axis_on()
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotc.pdf")

