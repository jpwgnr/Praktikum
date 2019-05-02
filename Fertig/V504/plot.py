import matplotlib.pyplot as plt
from uncertainties import ufloat
import numpy as np
from something import some
import uncertainties.unumpy as unp
from table import TexTable
from scipy import stats
from scipy.optimize import curve_fit
#Generate data 

#from txt
U1, I1= some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$U / \si{\volt}$", r"$I / \si{\micro\ampere}$"], label_text="taba", caption_text=r"Die Spannung und die Stromstärke bei einer Heizspannung von $\SI{3}{\volt}$ und die Heizspannung $\SI{2.0}{\ampere}$." , precision=1)

I1 =I1*1e-6

U2, I2= some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$U / \si{\volt}$", r"$I / \si{\micro\ampere}$"], label_text="tabb", caption_text=r"Die Spannung und die Stromstärke bei einer Heizspannung von $\SI{3.2}{\volt}$ und die Heizspannung $\SI{2.1}{\ampere}$." , precision=1)

I2 =I2*1e-6

U3, I3= some.neueWerte(file_name="data/datac.txt", finished_file="build/tabc.tex",  vars_name=[r"$U / \si{\volt}$", r"$I / \si{\micro\ampere}$"], label_text="tabc", caption_text=r"Die Spannung und die Stromstärke bei einer Heizspannung von $\SI{3.5}{\volt}$ und die Heizspannung $\SI{2.2}{\ampere}$." , precision=1)

I3 =I3*1e-6

U4, I4= some.neueWerte(file_name="data/datad.txt", finished_file="build/tabd.tex",  vars_name=[r"$U / \si{\volt}$", r"$I / \si{\micro\ampere}$"], label_text="taba", caption_text=r"Die Spannung und die Stromstärke bei einer Heizspannung von $\SI{4}{\volt}$ und die Heizspannung $\SI{2.3}{\ampere}$." , precision=1)

I4 =I4*1e-6

U5, I5= some.neueWerte(file_name="data/datae.txt", finished_file="build/tabe.tex",  vars_name=[r"$U / \si{\volt}$", r"$I / \si{\micro\ampere}$"], label_text="tabe", caption_text=r"Die Spannung und die Stromstärke bei einer Heizspannung von $\SI{4.1}{\volt}$ und die Heizspannung $\SI{2.4}{\ampere}$." , precision=1)

I5 =I5*1e-6

U6, I6= some.neueWerte(file_name="data/dataf.txt", finished_file="build/tabf.tex",  vars_name=[r"$U / \si{\milli\volt}$", r"$I / \si{\nano\ampere}$"], label_text="tabf", caption_text=r"Die Gegenspannung und die dazu gehörende Stromstärke." , precision=1)
U6= U6*1e-3
I6= I6*1e-9
U7, I7= some.neueWerte(file_name="data/datag.txt", finished_file="build/tabg.tex",  vars_name=[r"$U / \si{\milli\volt}$", r"$I / \si{\nano\ampere}$"], label_text="tabg", caption_text=r"Die Gegenspannung und die dazu gehörende Stromstärke." , precision=1)
U7= U7*1e-3
I7= I7*1e-9

U8, I8= some.neueWerte(file_name="data/datah.txt", finished_file="build/tabh.tex",  vars_name=[r"$U / \si{\milli\volt}$", r"$I / \si{\nano\ampere}$"], label_text="tabh", caption_text=r"Die Gegenspannung und die dazu gehörende Stromstärke." , precision=1)
U8= U8*1e-3
I8= I8*1e-9
#extra values 
def const(U1, const):
    return const* U1/U1

U9 = np.append(np.append(U6[:7], U7[:8]), U8[:])
I9 = np.append(np.append(I6[:7], I7[:8]), I8[:])

#functions 
some.tabelle([np.log(U5), np.log(I5)], finished_file="build/tab2.tex", vars_name=[r"$ln(U/U_0)$", r"$ln(I/I_0)$"], label_text="tab2", caption_text=r"Logarithmierte Spannungen und logarithmierte Stromstärken.", precision=2) 

steigung1, yabschnitt1, err1 = some.linReg(x=np.log(U5[0:3]), y=np.log(I5[0:3]), x_name=r"$log(U/U_0)$", y_name=r"$log(I/I_0)$", num=2,  x_add=0.3, file_name="build/plot2.pdf")

steigung2, yabschnitt2, err2 = some.linReg(x=U9, y=np.log(I9), x_name=r"$U$", y_name=r"$log(I/I_0)$", num=3,  x_add=0.1, file_name="build/plot3.pdf")

#calculate 

#save solution 
newU1 = np.linspace(U1[7], 260, 1000)
newU2 = np.linspace(U2[7], 260, 1000)
newU3 = np.linspace(U3[10], 260, 1000)
newU4 = np.linspace(U4[11], 260, 1000)
newU5 = np.linspace(U5[19], 260, 1000)

#Make plots for data
plt.figure(1)
plt.plot(U1, I1, "xr", label=r"$\SI{2.0}{\ampere}$, $\SI{3.0}{\volt}$")
plt.plot(U2, I2, "xb", label=r"$\SI{2.1}{\ampere}$, $\SI{3.2}{\volt}$")
plt.plot(U3, I3, "xg", label=r"$\SI{2.2}{\ampere}$, $\SI{3.5}{\volt}$")
plt.plot(U4, I4, "xy", label=r"$\SI{2.3}{\ampere}$, $\SI{4.0}{\volt}$")
plt.plot(U5, I5, "xk", label=r"$\SI{2.4}{\ampere}$, $\SI{4.1}{\volt}$")
plt.plot(newU1, const(newU1, 8e-6), "r",  linewidth=1.0)
plt.plot(newU2, const(newU2, 20e-6), "b", linewidth=1.0)
plt.plot(newU3, const(newU3, 40e-6), "g", linewidth=1.0)
plt.plot(newU4, const(newU4, 82e-6), "y", linewidth=1.0)
plt.plot(newU5, const(newU5, 178e-6), "k", linewidth=1.0)
plt.xlabel(r"$U / \si{\volt}$")
plt.ylabel(r"$I / \si{\ampere}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot1.pdf")

#curvefit plot
#
#plt.errorbar(x, y, yerr=err_y, fmt='rx', label='Daten')
#t = np.linspace(-0.5, 2 * np.pi + 0.5)
#plt.plot(t, f(t, *parameters), 'b-', label='Fit')
#plt.plot(t, np.sin(t), 'g--', label='Original')
#plt.xlim(t[0], t[-1])
#plt.xlabel(r'$t$')
#plt.ylabel(r'$f(t)$')
#plt.legend(loc='best')
#plt.tight_layout()
#plt.savefig("build/plot1b.pdf")
e0=1.602*1e-19 
k= 1.380*1e-23
m0= 9.11e-31 
h = 6.626e-34
T=-1/ufloat(steigung2, err2)*e0/k

L1 = 2.0* 3.0  
L2 = 2.1* 3.2 
L3 = 2.2* 3.5 
L4 = 2.3* 4.0 
L5 = 2.4* 4.1
N_w= 1
f= 0.32e-4
nu= 0.28 
sigma= 5.7e-8
L = np.array([L1,L2,L3,L4,L5])
I_S= np.array([8e-6, 20e-6, 37e-6, 80e-6, 175e-6])
T_var= ((L - N_w)/(f*nu*sigma))**(1/4) 
A= 1e-4

e0phi = k*T_var*(np.log(4*np.pi*e0*m0* k**2 * T_var**2/h**3)-np.log(I_S/A))/e0
e0phimean = e0phi.mean()
e0phistd = e0phi.std()
file = open("build/solution.txt", "w")
file.write(f"a) Sättigungsstrom: \n1. 8e-6 A\n2. 20e-6 A\n3. 37e-6 A\n4. 80e-6 A\n5. 175e-6 AExponent von b) = {steigung1} Fehler: {err1}\nErwartet wird 1.5\nc) Temperatur aus Anlaufstromgebiet: T = {T}\nd) Leistungen: 1. {L1} W\n2. {L2} W\n3. {L3} W\n4. {L4} W\n5. {L5} W\n\nDie Temperaturen die sich aus den jeweiligen Leistungen ergeben: {T_var} K\n\ne0 phi = {e0phi} eV\nMittelwert: {[e0phimean]} eV\nFehler: {[e0phistd]} eV \nLiteraturwert Austrittsarbeit Wolfram (Wikipdia): 4,55 eV")
file.close()
