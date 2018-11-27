import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
import scipy.constants as const 
#Generate data 

#from txt
#a)
x1, I1 = np.genfromtxt("data/dataa.txt", unpack=True)
taba = TexTable([x1,I1], [r"<++>", r"<++>"], label="tab<++>", caption="<++>", roundPrecision=<++>)
tab<++>.writeFile("build/tab<++>.tex")

#b)
d2, I2 = np.genfromtxt("data/datab.txt", unpack=True)
tab<++> = TexTable([<++>,<++>], [r"<++>", r"<++>"], label="tab<++>", caption="<++>", roundPrecision=<++>)
tab<++>.writeFile("build/tab<++>.tex")

#c)
H3, B3 = np.genfromtxt("data/datac.txt", unpack=True)
tab<++> = TexTable([<++>,<++>], [r"<++>", r"<++>"], label="tab<++>", caption="<++>", roundPrecision=<++>)
tab<++>.writeFile("build/tab<++>.tex")

#extra values 
#a)
n1=<++>
l1=<++>
mu_r1=<++>
mu_0=4*np.pi*e-7 

#b) 
R2=<++>
n2=<++>
x2= d2/2
#c)
R3=<++>
mu_r3=<++> 
n3= <++> 

#functions 

#a)
def getBlong(mu_r, mu_0, n, l, I):
    return mu_r*mu_0*(n/l)*I

#b)
def getBhelm(mu_0, I, n, R, x):
    return n*m_0*I*(R**2)/((R**2+x**2)**(3/2))

def getBhelmgrad(mu_0, I, n, R, x):
    return (-3*mu_0*I*R**2*x)/((R**2+x**2)**(5/2))

def getBtorus(mu_r, mu_0, n, R, I):
    return mu_r*mu_0*(n/(2*np.pi*R)*I)

def f(x, a, b, c, d):
     return a * np.sin(b * x + c) + d


#calculate 
#a)
B1= getBlong(mu_r1, mu_0, n1, l1, I1)

#b) 
B2= getBhelm(mu_0, I2, n2, R2, x2)
Bgrad2= getBhelmgrad(mu_0, I2, n2, R2, x2)

#c)
B3= getBtorus(mu_r3, mu_0, n3, R3, I3)

#allgemeine Rechnungen
Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(x,y)
 
parameters, pcov = curve_fit(f, x, y, sigma=err_x)

#save solution 

file = open("build/solution.txt", "w")
file.write("Steigung = {} Fehler: {}".format(Steigung1, np.sqrt(np.diag(pcov)) ))
file.close()

#Make plots for data
#a)
plt.figure(1)
plt.plot(x1, B1, "xr", label="Daten")
#plt.plot(x1, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlim(x[0], x[-1])
plt.xlabel(r"$s/\si{\meter}$")
plt.ylabel(r"$B/\si{\tesla}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

#b)
plt.figure(1)
plt.plot(d2, B2, "xr", label="Daten")
#plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlim(x[0], x[-1])
plt.xlabel(r"$s/\si{\meter}$")
plt.ylabel(r"$B/\si{\telsa}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot2.pdf")

#c)
plt.figure(1)
plt.plot(H3, B3, "xr", label="Daten")
#plt.plot(<++>, function(<++>), "r", label="Fit", linewidth=1.0)
plt.xlim(x[0], x[-1])
plt.xlabel(r"$H/\si{\tesla}$")
plt.ylabel(r"$B/\si{\tesla}$")
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

