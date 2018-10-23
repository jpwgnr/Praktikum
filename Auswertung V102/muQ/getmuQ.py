import numpy as np 
import uncertainties.unumpy as unp 
from uncertainties import ufloat
def functionmu(E, G): 
    return (E/(2*G))-1

def functionQ(E, mu):
    return E/(3*(1-2*mu))

E= ufloat(210e11, 0) 
G= unp.uarray(9.5e22,0.5e22)

mu= functionmu(E, G)
Q= functionQ(E, mu)

file = open("Ergebnisse1.txt", "w")
file.write("Value E: {} \nValue G: {} \nValue mu: {} \nValue Q: {}".format(E, G, mu, Q))
file.close()
