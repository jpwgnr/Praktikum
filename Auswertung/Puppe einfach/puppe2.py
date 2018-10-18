import numpy as np 
import uncertainties.unumpy as unp 

#Volumenformel für Zylinder, h Höhe in m, d hier Durchmesser in m 
def vZyl(h, d):
    return h* ((d/2)**2)*np.pi 

#Volumenformel für Kugel, d auch hier Durchmesser in m 
def vKug(d):
    return (4/3)*np.pi*(d/3)**3

#Daten der fünf Zylinder (drei verschiedene) und Durchmesser der einen Kugelin mm
data_h, data_d= np.genfromtxt("Puppeeinfach.txt", unpack=True)
data_dk= np.array(["29"])

# umrechnen von Höhe h, Durchmesser d des Zylinders und Durchmesser dk der Kugel in m 
h= unp.uarray(data_h, 0.5)/1000
d= unp.uarray(data_d, 0.5)/1000
dk= unp.uarray(data_dk, 0.5)/1000

#Volumen gesamt Zylinder mit Funktion Z.5 und Volumen gesamt Kugel Z.9
vgeszyl= vZyl(h,d)
vgeskug= vKug(dk)
# Gesamtvolumen der einfachen Puppe als Summe aus Zylindern und Kugel
Vges=sum(vgeszyl)+ sum(vgeskug)

# m in kg Gesamtmasse der Puppe
m= unp.uarray(0.16223, 0)

#Funktion um die Gesamtmasse der Einzelnen Körperteile zu berechnen
def einzelmasse(m, vgeszyl, Vges):
    return (vgeszyl/Vges)*m 

#Vektor mit den Einzelmassen in kg für Zylinder
mzyl= einzelmasse(m, vgeszyl, Vges)

#Einzelmasse der Kugel
mkug = einzelmasse(m, vgeskug, Vges)

#Trägheitsmomente der einzelnen Zylinderteile durch ihre Drehachse, Zylinder waagerecht
def izyl1(mzyl, d, h):
    return mzyl*((((d/2)**2)/4)+((h**2)/12))
#Trägheitsmomente Zylinder senkrecht
def izyl2(mzyl, d):
    return 0.5*mzyl*(d/2)**2

#Berechnen der Trägheitsmomente und in Vektoren schreiben
Izyl= izyl1(mzyl,d, h)
Izyl2= izyl2(mzyl, d)

#Trägheitsmomente für Kugel
def Ikug(mkug, dk):
    return (2/5)*mkug*(dk/2)**2

#berechnen des Trägheitsmoments
Ikug= Ikug(mkug, dk)

#Liste der Abstände von der Gesamtdrehachse der Puppe in m
a_1= unp.uarray(0.076, 0.00005)
a_2= unp.uarray(0.0873, 0.00005)

#Satz von Steiner mit I Kugel, und den fünf Zylindern
Iges= Ikug+ Izyl2[2]+2*(Izyl[0]+mzyl[0]*(a_1**2))+2*(Izyl[3]+mzyl[3]*(a_2**2))

file = open("ErgebnisPuppe2.txt", "w")
file.write("Volumen Gesamt: {}\n I Zylinder: {}\n I Kugel: {}\n I Gesamt Position 2: {}".format(Vges, Izyl, Ikug, Iges))
