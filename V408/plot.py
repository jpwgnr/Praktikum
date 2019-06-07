import numpy as np 
import matplotlib.pyplot as plt 
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit

#S: Position des Schirms, L: Position der Linse, B: Bildgröße
#g: Gegenstandsweite, b: Bildweite
L1, S1, B1 = np.genfromtxt("data/tab1.txt", unpack=True)

#Erste Messung, neue Tabelle
g1 = 110.7 - L1
b1 = L1 - S1

tab1 = TexTable([g1, b1, B1], [r"$g / \si{\centi\meter}$", r"$b / \si{\centi\meter}$", r"$B / \si{\centi\meter}$"], label="tab1", caption="Es sind die Bildweite und die Bildgröße bei verschiedenen Gegenstandsweiten zu sehen.", roundPrecision=1)
tab1.writeFile("build/tab1.tex")

#Methode von Bessel (weiß), neue Tabelle
S2, L21, L22 = np.genfromtxt("data/Bessel_weiß.txt", unpack=True)

g21 = 110.7 - L21
g22 = 110.7 - L22 
b21 = L21 - S2
b22 = L22 - S2

tab2 = TexTable([g21, b21, g22, b22], [r"$g_1 / \si{\centi\meter}$", r"$b_1 / \si{\centi\meter}$", r"$g_2 / \si{\centi\meter}$", r"$b_2 / \si{\centi\meter}$"], label="bessel_weiß", caption="Die ersten Gegenstands- und Bildweiten und die zweiten Gegenstands- und Bildweiten, die mit der Methode von Bessel gemessen wurden, für weißes Licht.", roundPrecision=1)
tab2.writeFile("build/Bessel_weiß.tex")

#Methode von Bessel (blau), neue Tabelle
S3, L31, L32 = np.genfromtxt("data/Bessel_blau.txt", unpack=True)

g31 = 110.7 - L31
g32 = 110.7 - L32 
b31 = L31 - S3
b32 = L32 - S3

tab3 = TexTable([g31, b31, g32, b32], [r"$g_1 / \si{\centi\meter}$", r"$b_1 / \si{\centi\meter}$", r"$g_2 / \si{\centi\meter}$", r"$b_2 / \si{\centi\meter}$"], label="bessel_blau", caption="Die ersten Gegenstands- und Bildweiten und die zweiten Gegenstands- und Bildweiten, die mit der Methode von Bessel gemessen wurden, für blaues Licht.", roundPrecision=1)
tab3.writeFile("build/Bessel_blau.tex")

#Methode von Bessel (rot), neue Tabelle
S4, L41, L42 = np.genfromtxt("data/Bessel_rot.txt", unpack=True)

g41 = 110.7 - L41
g42 = 110.7 - L42 
b41 = L41 - S4
b42 = L42 - S4

tab4 = TexTable([g41, b41, g42, b42], [r"$g_1 / \si{\centi\meter}$", r"$b_1 / \si{\centi\meter}$", r"$g_2 / \si{\centi\meter}$", r"$b_2 / \si{\centi\meter}$"], label="bessel_rot", caption="Die ersten Gegenstands- und Bildweiten und die zweiten Gegenstands- und Bildweiten, die mit der Methode von Bessel gemessen wurden, für rotes Licht.", roundPrecision=1)
tab4.writeFile("build/Bessel_rot.tex")

#Methode von Abbe
#S: Position des Schirms, A=a+x (a: Position Referenzpunkt), B: Bildgröße
S5, A, B5 = np.genfromtxt("data/Abbe.txt", unpack=True)

a = A - 3
g5 = 110.7 - a 
b5 = a - S5 

tab5 = TexTable([g5, b5, B5], [r"$g' / \si{\centi\meter}$", r"$b' / \si{\centi\meter}$", r"$B / \si{\centi\meter}$"], label="abbe", caption="Die Gegenstands- und Bildweiten bezüglich des Referenzpunktes und die jeweiligen Bildgrößen, die mit der Methode von Abbe gemessen wurden.", roundPrecision=1)
tab5.writeFile("build/Abbe.tex")

#Linsengleichung und Abbildungsgesetz
def linsengleichung(b, g):
    return (b*g)/(b+g)

def abbildungsgesetz1(b, g):
    return b/g 

def abbildungsgesetz2(B):
    return B/3 #G = 3cm

#Aufgabe 1
f1 = linsengleichung(b1, g1)
f1 = ufloat(f1.mean(), f1.std())
V1 = abbildungsgesetz1(b1, g1)
V1 = ufloat(V1.mean(), V1.std())
V2 = abbildungsgesetz2(B1)
V2 = ufloat(V2.mean(), V2.std())

plt.figure(1)
for i in range(len(b1)-1):
    x = np.array([0, b1[i]])
    y = np.array([g1[i], 0])
    plt.plot(x, y, "b", linewidth=1.0, marker=".")
x = np.array([0, b1[-1]])
y = np.array([g1[-1], 0])
plt.plot(x, y, "b", linewidth=1.0, label="Geraden", marker=".")

xsp = 9.62
ysp = 9.62
x_sp1 = np.array([0, xsp])
y_sp1 = np.array([ysp , ysp])
x_sp2 = np. array([xsp, xsp])
y_sp2 = np.array([ysp, 0])
plt.plot(x_sp1, y_sp1, "c--", label="Brennweite")
plt.plot(x_sp2, y_sp2, "c--")
plt.plot(xsp, ysp, "c", marker="x")

plt.xlabel(r"$b / \si{\centi\meter}$")
plt.ylabel(r"$g / \si{\centi\meter}$")
plt.grid()
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")


#Methode von Bessel
def bessel(d, e):
    return (e**2 - d**2) / (4*e)

e1_weiss = g21 + b21 
e2_weiss = g22 + b22
d1_weiss = g21 - b21
d2_weiss = g22 - b22

e1_blau = g31 + b31 
e2_blau = g32 + b32
d1_blau = g31 - b31
d2_blau = g32 - b32

e1_rot = g41 + b41 
e2_rot = g42 + b42
d1_rot = g41 - b41
d2_rot = g42 - b42

f1_weiss = bessel(d1_weiss, e1_weiss)
f1_weiss = ufloat(f1_weiss.mean(), f1_weiss.std())
f2_weiss = bessel(d2_weiss, e2_weiss)
f2_weiss = ufloat(f2_weiss.mean(), f2_weiss.std())

f1_blau = bessel(d1_blau, e1_blau)
f1_blau = ufloat(f1_blau.mean(), f1_blau.std())
f2_blau = bessel(d2_blau, e2_blau)
f2_blau = ufloat(f2_blau.mean(), f2_blau.std())

f1_rot = bessel(d1_rot, e1_rot)
f1_rot = ufloat(f1_rot.mean(), f1_rot.std())
f2_rot = bessel(d2_rot, e2_rot)
f2_rot = ufloat(f2_rot.mean(), f2_rot.std())


#Methode von Abbe
V_abbe2 = abbildungsgesetz2(B5)
V_abbe1 = abbildungsgesetz1(b5, g5) #braucht man glaube ich gar nicht

#Plot mit g'
x1 = 1 + 1/V_abbe2 
x1_plot = np.linspace(x1[0]-0.5, x1[-1]+0.5)


#Plot mit b'
x2 = 1+ V_abbe2
x2_plot = np.linspace(x2[0]-0.5, x2[-1]+0.5)

#steigung, abschnitt = stats.linregress(m, n)

#Gerade
def gerade(x, m, n):
    return m*x+n

params, covariance = curve_fit(gerade, x1, g5)
params2, covariance2 = curve_fit(gerade, x2, b5)
err1 = np.sqrt(np.diag(covariance))
err2 = np.sqrt(np.diag(covariance2))


plt.figure(2)
plt.plot(x1, g5, "xb", label="Daten")
plt.plot(x1_plot, gerade(x1_plot, *params), "k", linewidth=1.0, label="Fit")
plt.xlabel(r"$1 + \frac{1}{V}$")
plt.ylabel(r"$g' / \si{\centi\meter}$")
plt.grid()
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/abbe_g.pdf")

plt.figure(3)
plt.plot(x2, b5, "xb", label="Daten")
plt.plot(x2_plot, gerade(x2_plot, *params2), "k", linewidth=1.0, label="Fit")
plt.xlabel(r"$1 + V$")
plt.ylabel(r"$b' / \si{\centi\meter}$")
plt.grid()
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/abbe_b.pdf")


#in der solution.txt saven
file = open("build/solution.txt", "w")
file.write(f"V408 \nerste Messung: \nBrennweite = {f1} \nAbbildungsmaßstab(mit b und g): {V1} \nAbbildungsmaßstab(mit B und G) = {V2} \n \nMethode von Bessel: \n1 ist jeweils mit b_1 und g_1 berechnet, 2 mit b_2 und g_2 \nBrennweite_weiss,1 = {f1_weiss} \nBrennweite_weiss,2 = {f2_weiss} \nBrennweite_blau,1 = {f1_blau} \nBrennweite_blau,2 = {f2_blau} \nBrennweite_rot,1 = {f1_rot} \nBrennweite_rot,2 = {f2_rot} \n \nMethode von Abbe: \nPlot mit g': \nSteigung (Brennweite) = {params[0]} +/- {err1[0]} \ny-Achsenabschnitt (h) = {params[1]} +/- {err1[1]} \nPlot mit b': \nSteigung (Brennweite) = {params2[0]} +/- {err2[0]} \ny-Achsenabschnitt (h') = {params2[1]} +/- {err2[1]}")
file.close()