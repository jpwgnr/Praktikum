import numpy as np 
import uncertainties.unumpy as unp 

# Für Erklärungen dieses Dokuments bitte die Kommentare von puppe2.py anschauen
def vZyl(h, d):
    return h* ((d/2)**2)*np.pi 

def vKug(d):
    return (4/3)*np.pi*(d/3)**3

data_h, data_d= np.genfromtxt("Puppeeinfach.txt", unpack=True)
data_dk= np.array(["29"])

h= unp.uarray(data_h, 0.5)/1000
d= unp.uarray(data_d, 0.5)/1000
dk= unp.uarray(data_dk, 0.5)/1000

vgeszyl= vZyl(h,d)
vgeskug= vKug(dk)


Vges=sum(vgeszyl)+ sum(vgeskug)

m= unp.uarray(0.16223, 0)

def einzelmasse(m, vgeszyl, Vges):
    return (vgeszyl/Vges)*m 

mzyl= einzelmasse(m, vgeszyl, Vges)

mkug = einzelmasse(m, vgeskug, Vges)

def Izyl(mzyl,d):
    return 0.5*mzyl*(d/2)**2

Izyl= Izyl(mzyl,d)

def Ikug(mkug, dk):
    return (2/5)*mkug*(dk/2)**2

Ikug= Ikug(mkug, dk)

a_1= unp.uarray(0.0075, 0.00005)
a_2= unp.uarray(0.0246, 0.00005)


Iges= Ikug+ Izyl[2]+2*(Izyl[0]+mzyl[0]*(a_1**2))+2*(Izyl[3]+mzyl[3]*(a_2**2))

file = open("ErgebnisPuppeeinfach.txt", "w")
file.write("Volumen Gesamt: {} \n I Gesamt: {}".format(Vges, Iges))
