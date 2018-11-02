import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

#all functions I need
def xnew(xvalue, L):
    return L*(xvalue**2)-((xvalue**3)/3)

def Dnew(D1, D2):
    return np.abs(D1-D2)

def F(m):
    return m*9.81

def IKreis(radius):
    return (np.pi*(radius**4))/4 

def IQuadrat(a):
    return a**4/12

def getE(F, I, newx, newD):
   return (F/(2*I*newD))*newx

def getElinreg(F, I, slope):
    return F/(2*I*slope)

#get values from txt
L= 51.2/100
Iq= IKreis(0.0041)
Fg= F(0.5411)
x1, ohneD, mitD = np.genfromtxt("D.txt", unpack=True)

D= Dnew(ohneD,mitD)/1000
x= xnew(x1/100, L)

#output newD and newx
np.savetxt("newDnewX2.txt", np.column_stack([D, x]), header="D in m, x in m")
Steigung, yAbschnitt, r_value, p_value, std_err= stats.linregress(x,D)

y= Steigung*x+yAbschnitt
plt.plot(x,D)
plt.plot(x,y)
plt.savefig("Stange2.pdf")

# get E

E= getE(Fg, Iq, x, D)
Emean= np.mean(E)
Estd= np.std(E)

Elinreg=getElinreg(Fg, Iq, Steigung)

file = open("ErgebnisE2.txt", "w")
file.write("Steigung der Funktion: {}\n Durchschnitt E: {}\n Fehler E: {}\n linReg E= {}".format(Steigung, Emean, Estd, Elinreg))
file.close()