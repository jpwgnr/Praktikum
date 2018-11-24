import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
<++>, <++> = np.genfromtxt("data/data<++>.txt", unpack=True)
tab<++> = TexTable([<++>,<++>], [r"<++>", r"<++>"], label="tab<++>", caption="<++>", roundPrecision=<++>)
tab<++>.writeFile("build/tab<++>.tex")

#extra values 
a=0

#functions 

def func(x):
    return x+1

def f(x, a, b, c, d):
     return a * np.sin(b * x + c) + d
#calculate 

Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
 
parameters, pcov = curve_fit(f, x, y, sigma=err_x)

#save solution 

file = open("build/solution.txt", "w")
file.write("Steigung = {} Fehler: {}".format(Steigung1, np.sqrt(np.diag(pcov)) ))
file.close()

#Make plots for data
plt.figure(1)
plt.plot(x, y, "xr", label="Daten")
plt.plot(x, function(x), "r", label="Fit", linewidth=1.0)
plt.xlim(x[0], x[-1])
plt.xlabel(r"$t/\si{\second}$")
plt.ylabel(r"$y(x)$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

#curvefit plot

plt.errorbar(x, y, yerr=err_y, fmt='rx', label='Daten')
t = np.linspace(-0.5, 2 * np.pi + 0.5)
plt.plot(t, f(t, *parameters), 'b-', label='Fit')
plt.plot(t, np.sin(t), 'g--', label='Original')
plt.xlim(t[0], t[-1])
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot1b.pdf")

