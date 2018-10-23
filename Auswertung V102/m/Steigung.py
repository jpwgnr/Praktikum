import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt 
from uncertainties import ufloat
x,y= np.genfromtxt("xy.txt", unpack=True)

slope, intercept, r_value, p_value, std_err= stats.linregress(x,y)

y2= slope*x+intercept

plt.plot(x,y)
plt.plot(x, y2)
plt.savefig("Steigung.pdf")

Steigung= slope

mk= ufloat(512.2e-3, 512.2e-3*0.04e-2) #kg
Rk= ufloat(25.38e-3, 50.76e-3*0.007e-2) #m
theta= ufloat(22.5e-7,0)

m= Steigung*4*(np.pi**2)*((2/5)*mk*(Rk**2)+theta)

file = open("Ergebnism.txt", "w")
file.write("Steigung der Funktion: {}\ny-Abschnitt: {}\nErgebnis m: {}".format(Steigung, intercept, m))
file.close()
