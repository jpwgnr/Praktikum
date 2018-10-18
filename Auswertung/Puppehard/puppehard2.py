import numpy as np 
import uncertainties.unumpy as unp 

def vZyl(h, d):
    return h* ((d/2)**2)*np.pi 

def vhZyl(h, d):
    return 0.5* h* ((d/2)**2)*np.pi 

def vKug(d):
    return (4/3)*np.pi*(d/3)**3

def vhKug(d):
    return 0.5* (4/3)*np.pi*(d/3)**3

data_h, data_d= np.genfromtxt("PuppeZyl.txt", unpack=True)
data_dk= np.genfromtxt("PuppeKug.txt", unpack=True)
data_hh, data_hd= np.genfromtxt("PuppehZyl.txt", unpack=True)
data_hdk= np.genfromtxt("PuppehKug.txt", unpack=True)

h= unp.uarray(data_h, 0.5)/100
d= unp.uarray(data_d, 0.5)/100
dk= unp.uarray(data_dk, 0.5)/100
hh= unp.uarray(data_hh, 0.5)/100
hd= unp.uarray(data_hd, 0.5)/100
hdk=unp.uarray(data_hdk, 0.5)/100

vgeszyl= vZyl(h, d)
vgeshzyl=vhZyl(hh, hd)
vgeskug= vKug(dk)
vgeshkug= vhKug(hdk) 

#Volumen der Puppe, einfach
Vges=sum(vgeszyl)+ sum(vgeshzyl)+ sum(vgeskug) + vgeshkug

m= unp.uarray(0.16223, 0)

def einzelmasse(m, vgeszyl, Vges):
    return (vgeszyl/Vges)*m 

mzyl= einzelmasse(m, vgeszyl, Vges)

mkug = einzelmasse(m, vgeskug, Vges)

mhzyl= einzelmasse(m, vgeshzyl, Vges)

mhkug= einzelmasse(m, vgeshkug, Vges)

def izyl1(mzyl, d, h):
    return mzyl*((((d/2)**2)/4)+((h**2)/12))

def izyl2(mzyl, d):
    return 0.5*mzyl*(d/2)**2

Izyl= izyl1(mzyl,d, h)
Ihzyl= izyl1(mhzyl, hd, hh)
Ihzyl2= izyl2(mhzyl, hd)
Izyl2= izyl2(mzyl, d)

def ikug(mkug, dk):
    return (2/5)*mkug*(dk/2)**2

Ikug= ikug(mkug, dk)
Ihkug= ikug(mhkug, hdk)


a_1= unp.uarray(0.0259, 0.0005)
a_2= unp.uarray(0.025275, 0.0005)
a_3= unp.uarray(0.023, 0.0005)
a_4= unp.uarray(0.0248, 0.0005)
a_5= unp.uarray(0.022775, 0.0005)
a_6= unp.uarray(0.00945, 0.0005)

Iges= Ikug[0]+ Ikug[4] + Izyl2[0]+ Izyl2[1]+ Izyl2[2] + Izyl2[7] + 2*(Ikug[2]+mkug[2]*a_1**2)+2*(Izyl2[3]+mzyl[3]*a_2**2)+2*(Ikug[1]+mkug[1]*a_3**2)+2*(Izyl[4]+mzyl[4]*a_4**2)+2*(Ikug[3]+ mkug[3]*a_5**2)+2*(Ikug[5]+mkug[5]*a_6**2)+2*(Izyl[5]+mzyl[5]*a_6**2)+2*(Ikug[6]+mkug[6]*a_6**2)+2*(Izyl[6]+mzyl[6]*a_6**2)+2*(Ikug[7]+mkug[7]*a_6**2)+2*(Ihzyl[1]+mhzyl[1]*a_6**2)+2*(Ihzyl[0]+mhzyl[0]*a_1**2)+Ihkug 

file = open("ErgebnisPuppe2.txt", "w")
file.write("Volumen Gesamt: {}\n I Gesamt Position 2: {}".format(Vges, Iges))
file.close()
