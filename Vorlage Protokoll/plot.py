import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats

#Generate data 

#from txt
x, y = np.genfromtxt("data/data.txt", unpack=True)
tab1 = TexTable([x,y], [r"xyz", r"xyz"], label="tab1", caption="xy", roundPrecision=3)
tab1.writeFile("build/tab1.tex")

#extra values 
a=0

#functions 

def func(x):
    return x+1

#calculate 

Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)

#save solution 

file = open("build/solution.txt", "w")
file.write("Steigung = {}".format(Steigung1))
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



