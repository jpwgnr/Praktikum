import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
s, t= np.genfromtxt("data/dataa.txt", unpack=True)
tab1 = TexTable([s,t], [r"$s \si{\meter}$", r"$t \si{\second}$"], label="tab1", caption=r"Die Strecke $s$ aufgetragen gegen die Zeit $t$.", roundPrecision=2)
tab1.writeFile("build/tab1.tex")

#extra values 
R= 0.127/2
r= 0.006/2
m= 0.43564  
tiefe= 0.264

s=20.6
r_eff= s/(20*np.pi)

#functions 

def func(x):
   <++> 

#calculate 

Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(s, t**2)
#params1, pcov1 = curve_fit(func, <++>, <++>, sigma=err_<++>)

#save solution 

file = open("build/solution.txt", "w")
file.write("Maxwell'sches Rad\nTrägheitsmoment: I={}, ".format(Steigung1, np.sqrt(np.diag(pcov)) ))
file.close()

#curvefit plot
plt.figure(1)
plt.errorbar(s, t, fmt='rx', label='Daten')
newt= np.linspace(t[0], t[-1], 500)
plt.plot(newt, func(newt, *params1), 'r-', label='Fit')
plt.xlabel(r'$<++>$')
plt.ylabel(r'$<++>$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot1a.pdf")

plt.figure(2)
plt.errorbar(<++>, <++>, yerr=err_<++>, fmt='rx', label='Daten')
newt= np.linspace(<++>[0], <++>[-1], 500)
plt.plot(newt, func(newt, *params1), 'r-', label='Fit')
plt.xlabel(r'$<++>$')
plt.ylabel(r'$<++>$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot1a.pdf")

plt.figure(3)
plt.errorbar(<++>, <++>, yerr=err_<++>, fmt='rx', label='Daten')
newt= np.linspace(<++>[0], <++>[-1], 500)
plt.plot(newt, func(newt, *params1), 'r-', label='Fit')
plt.xlabel(r'$<++>$')
plt.ylabel(r'$<++>$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot1a.pdf")
