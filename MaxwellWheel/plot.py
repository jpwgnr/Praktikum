import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
h1, t1= np.genfromtxt("data/dataa.txt", unpack=True)
tab1 = TexTable([h1,t1], [r"$h1 \si{\centi\meter}$", r"$t \si{\second}$"], label="tab1", caption=r"Die Strecke $s$ aufgetragen gegen die Zeit $t$.", roundPrecision=2)
tab1.writeFile("build/tab1.tex")

h2, t2= np.genfromtxt("data/datab.txt", unpack=True)
tab2 = TexTable([h2,t2], [r"$h2 \si{\centi\meter}$", r"$t \si{\second}$"], label="tab1", caption=r"Die Strecke $s$ aufgetragen gegen die Zeit $t$.", roundPrecision=2)
tab2.writeFile("build/tab2.tex")

h3, t3= np.genfromtxt("data/datac.txt", unpack=True)
tab3 = TexTable([h3,t3], [r"$h3 \si{\centi\meter}$", r"$t \si{\second}$"], label="tab1", caption=r"Die Strecke $s$ aufgetragen gegen die Zeit $t$.", roundPrecision=2)
tab3.writeFile("build/tab3.tex")

#extra values 
R= 0.127/2
r= 0.006/2
m= 0.43564  
tiefe= 0.264

s=0.206
r_eff= s/(20*np.pi)

#functions 

def dist(t,x,p,q):
   return 0.5*(x-q)*t**2+p 

def line(m,x,n):
    return m*x+n

#calculate 

#a) 
newh1= np.empty(len(h1))
for i in range(1,16):
    newh1[0]= 0
    newh1[i]= h1[i-1]+h1[i]-2*tiefe

#b)
newh2= np.empty(len(h2))
for i in range(1,11):
    newh2[0]= 0
    newh2[i]= h2[i-1]+h2[i]-2*tiefe
#c)
newh3= np.empty(len(h3))
for i in range(1,11):
    newh3[0]= 0
    newh3[i]= h3[i-1]+h3[i]-2*tiefe

newh1= np.delete(newh1, 0)
newh2= np.delete(newh2, 0)
newh3= np.delete(newh3, 0)
t1= np.delete(t1, 0)
t2= np.delete(t2, 0)
t3= np.delete(t3, 0)

a_theo= (1/(1+(R**2)/2*r_eff**2))*9.81

Steigung1, yAbschnitt1, r_value1, p_value1, std_err1= stats.linregress(t1**2, newh1)
Steigung2, yAbschnitt2, r_value2, p_value2, std_err2= stats.linregress(t2**2, newh2)
Steigung3, yAbschnitt3, r_value3, p_value3, std_err3= stats.linregress(t3**2, newh3)
params1, pcov1 = curve_fit(dist, t1, newh1)
params2, pcov2 = curve_fit(dist, t2, newh2)
params3, pcov3 = curve_fit(dist, t3, newh3)

a_exp= np.array([Steigung1, Steigung2, Steigung3]) 
#save solution 

file = open("build/solution.txt", "w")
file.write("Maxwell'sches Rad\nTrägheitsmoment: I={}, ".format(a_exp.mean(), a_exp.std(), ))
file.close()

#curvefit plot
plt.figure(1)
plt.errorbar(t1, newh1, fmt='rx', label='Daten')
newt1= np.linspace(t1[0]+1, t1[-1]-1, 500)
plt.plot(newt1, dist(newt1, *params1), 'b-', label='Fit')
plt.ylabel(r'$s/ \si{\centi\meter}$')
plt.xlabel(r'$t / \si{\second}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot1a.pdf")

plt.figure(2)
plt.errorbar(t2, newh2, fmt='rx', label='Daten')
newt2= np.linspace(t2[0]+1, t2[-1]-1, 500)
plt.plot(newt2, dist(newt2, *params2), 'b-', label='Fit')
plt.ylabel(r'$s/ \si{\centi\meter}$')
plt.xlabel(r'$t / \si{\second}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot2a.pdf")

plt.figure(3)
plt.errorbar(t3, newh3, fmt='rx', label='Daten')
newt3= np.linspace(t3[0]+1, t3[-1]-1, 500)
plt.plot(newt3, dist(newt3, *params3), 'b-', label='Fit')
plt.ylabel(r'$s/ \si{\centi\meter}$')
plt.xlabel(r'$t / \si{\second}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot3a.pdf")

plt.figure(4)
plt.errorbar(t1**2, newh1, fmt='rx', label='Daten')
plt.plot(newt1**2, line(Steigung1,newt1**2,yAbschnitt1), 'b-', label='Fit')
plt.ylabel(r'$s/ \si{\centi\meter}$')
plt.xlabel(r'$t^{2} / \si{\square\second}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot1b.pdf")


plt.figure(5)
plt.errorbar(t2**2, newh2, fmt='rx', label='Daten')
plt.plot(newt2**2, line(Steigung2,newt2**2,yAbschnitt2), 'b-', label='Fit')
plt.ylabel(r'$s/ \si{\centi\meter}$')
plt.xlabel(r'$t^{2} / \si{\square\second}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot2b.pdf")

plt.figure(6)
plt.errorbar(t3**2, newh3, fmt='rx', label='Daten')
plt.plot(newt3**2, line(Steigung3, newt3**2, yAbschnitt3), 'b-', label='Fit')
plt.ylabel(r'$s/ \si{\centi\meter}$')
plt.xlabel(r'$t^{2} / \si{\square\second}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("build/plot3b.pdf")
