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

tab1 = TexTable([g1, b1, B1], [r"$g / \si{\centi\meter}$", r"$b / \si{\centi\meter}$", r"$B / \si{\centi\meter}$"], label="tab1", caption="Erste Messung.", roundPrecision=1)
tab1.writeFile("build/tab1.tex")

#Methode von Bessel (weiß), neue Tabelle
S2, L21, L22 = np.genfromtxt("data/Bessel_weiß.txt", unpack=True)

g21 = 110.7 - L21
g22 = 110.7 - L22 
b21 = L21 - S2
b22 = L22 - S2

tab2 = TexTable([g21, b21, g22, b22], [r"$g_1 / \si{\centi\meter}$", r"$b_1 / \si{\centi\meter}$", r"$g_2 / \si{\centi\meter}$", r"$b_2 / \si{\centi\meter}$"], label="bessel_weiß", caption="Bessel 1", roundPrecision=1)
tab2.writeFile("build/Bessel_weiß.tex")

#Methode von Bessel (blau), neue Tabelle
S3, L31, L32 = np.genfromtxt("data/Bessel_blau.txt", unpack=True)

g31 = 110.7 - L31
g32 = 110.7 - L32 
b31 = L31 - S3
b32 = L32 - S3

tab3 = TexTable([g31, b31, g32, b32], [r"$g_1 / \si{\centi\meter}$", r"$b_1 / \si{\centi\meter}$", r"$g_2 / \si{\centi\meter}$", r"$b_2 / \si{\centi\meter}$"], label="bessel_blau", caption="Bessel 2", roundPrecision=1)
tab3.writeFile("build/Bessel_blau.tex")

#Methode von Bessel (rot), neue Tabelle
S4, L41, L42 = np.genfromtxt("data/Bessel_rot.txt", unpack=True)

g41 = 110.7 - L41
g42 = 110.7 - L42 
b41 = L41 - S4
b42 = L42 - S4

tab4 = TexTable([g31, b31, g32, b32], [r"$g_1 / \si{\centi\meter}$", r"$b_1 / \si{\centi\meter}$", r"$g_2 / \si{\centi\meter}$", r"$b_2 / \si{\centi\meter}$"], label="bessel_rot", caption="Bessel 3", roundPrecision=1)
tab4.writeFile("build/Bessel_rot.tex")

#Methode von Abbe
#S: Position des Schirms, A=a+x (a: Position Referenzpunkt), B: Bildgröße
S5, A, B5 = np.genfromtxt("data/Abbe.txt", unpack=True)

a = A - 3
g5 = 110.7 - a 
b5 = a - S5 

tab5 = TexTable([g5, b5, B5], [r"$g' / \si{\centi\meter}$", r"$b' / \si{\centi\meter}$", r"$B / \si{\centi\meter}$"], label="abbe", caption="Abbe", roundPrecision=1)
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

#Plot
plt.figure(1)
plt.plot(b1, g1, "g-")
plt.xlim(0, b1[-1])
plt.ylim(0, g1[-1])
plt.xlabel(r"$b / \si{\centi\meter}$")
plt.ylabel(r"$g / \si{\centi\meter}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

#in der solution.txt saven
file = open("build/solution.txt", "w")
file.write(f"V408\nBrennweite_1 = {f1} \nAbbildungsmaßstab(mitbundg): {V1}\nAbbildungsmaßstab(mitBundG) = {V2}")
file.close()