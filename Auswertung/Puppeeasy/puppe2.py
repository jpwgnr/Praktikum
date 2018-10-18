import numpy as np 
import uncertainties.unumpy as unp 

def vZyl(h, d):
    return h* ((d/2)**2)*np.pi 

def vKug(d):
    return (4/3)*np.pi*(d/3)**3

data_h, data_d= np.genfromtxt("Puppeeasy.txt", unpack=True)
data_dk= np.array(["29"])

h= unp.uarray(data_h, 0.5)/100
d= unp.uarray(data_d, 0.5)/100
dk= unp.uarray(data_dk, 0.5)/100

vgeszyl= vZyl(h,d)
vgeskug= vKug(dk)
#Volumen der Puppe, einfach
Vges=sum(vgeszyl)+ sum(vgeskug)

m= unp.uarray(0.16223, 0)

def einzelmasse(m, vgeszyl, Vges):
    return (vgeszyl/Vges)*m 

mzyl= einzelmasse(m, vgeszyl, Vges)

mkug = einzelmasse(m, vgeskug, Vges)

def Izyl1(mzyl, d, h):
    return mzyl*((((d/2)**2)/4)+((h**2)/12))

def Izyl2(mzyl, d):
    return 0.5*mzyl*(d/2)**2

Izyl= Izyl1(mzyl,d, h)
Izyl2= Izyl2(mzyl, d)
def Ikug(mkug, dk):
    return (2/5)*mkug*(dk/2)**2

Ikug= Ikug(mkug, dk)

a_1= unp.uarray(0.076, 0.0005)
a_2= unp.uarray(0.0873, 0.0005)
Iges= Ikug+ Izyl2[2]+2*(Izyl[0]+mzyl[0]*(a_1**2))+2*(Izyl[3]+mzyl[3]*(a_2**2))

file = open("ErgebnisPuppe2.txt", "w")
file.write("Volumen Gesamt: {}\n I Zylinder: {}\n I Kugel: {}\n I Gesamt Position 2: {}".format(Vges, Izyl, Ikug, Iges))
