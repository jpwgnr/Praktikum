import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats

#all functions I need
def xnew(xvalue, L):
    return 4*xvalue**3-12*L*xvalue**2+9*L**2*xvalue-L**3 

def Dnew(D1, D2):
    return np.abs(D1-D2)

def F(m):
    return m*9.81

def IKreis(radius):
    return (np.pi*(radius**4))/4 

def IQuadrat(a):
    return a**4/12

def getE(F, I, newx, newD):
   return (F/(48*I*newD))*newx

def getElinreg(F, I, slope):
    return F/(48*I*slope)

#get values from txt
L= 56.1/100
Iq= IKreis(0.004)
Fg= F(0.5411)
x1, ohneD, mitD = np.genfromtxt("D2.txt", unpack=True)

D= Dnew(ohneD,mitD)/1000
x= xnew(x1/100, L)

#output newD and newx
np.savetxt("newDnewX3b.txt", np.column_stack([D, x]), header="D in m, x in m")
Steigung, yAbschnitt, r_value, p_value, std_err= stats.linregress(x,D)

y= Steigung*x+yAbschnitt

plt.plot(x,D, "xr", label="Messwerte")
plt.plot(x,y, "r", label="Ausgleichsgerade")
plt.xlabel(r"$4x^{3}-12Lx^{2}+9L^{2}x-L^{3} /m³$")
plt.ylabel(r"$D(x)/m$")
plt.legend(loc="best")
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig("Stange3b.pdf")

# get E

E= getE(Fg, Iq, x, D)
Emean= np.mean(E)
Estd= np.std(E)

Elinreg=getElinreg(Fg, Iq, Steigung)

file = open("ErgebnisE3b.txt", "w")
file.write("Steigung der Funktion: {}\n linReg E= {}".format(Steigung, Elinreg))
file.close()
