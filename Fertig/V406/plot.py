import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 


abstand = 1.113 
dunkelstrom = 1.6*1e-9 
#Generate data 
l1, I1 = some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="taba", caption_text=r"Die $x$-Koordinate und die Stromstärke." , precision=1)
l1 = (l1-25.5)*1e-3 #Meter
I1 = I1*1e-9 -dunkelstrom #Ampere
phi1 = np.arctan(l1/abstand)
l1a, I1a= some.neueWerte(file_name="data/dataaextra.txt", finished_file="build/taba2.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="taba2", caption_text=r"Die $x$-Koordinate und die Stromstärke." , precision=1)
l1a = (l1a-25.5)*1e-3 #Meter
I1a = I1a*1e-9 - dunkelstrom #Ampere 
phi1a = np.arctan(l1a/abstand)
l2, I2 = some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="tabb", caption_text=r"Die $x$-Koordinate und die Stromstärke." , precision=1)
l2= (l2-23.0)*1e-3 #Meter
I2= I2*1e-9 -dunkelstrom #Ampere  
phi2 = np.arctan(l2/abstand)
l3, I3= some.neueWerte(file_name="data/datac.txt", finished_file="build/tabc.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="tabc", caption_text=r"Die $x$-Koordinate und die Stromstärke." , precision=1)
l3= (l3-24.0)*1e-3 #Meter
I3= I3*1e-9 -dunkelstrom #Ampere
phi3 = np.arctan(l3/abstand)

#Generate table with calculated data
some.tabelle([phi1*1e3, I1*1e9], finished_file="build/tab1.tex", vars_name=[r"$\varphi / \si{\milli\radian}$", r"$I / \si{\nano\ampere}$"], label_text="tab1", caption_text=r"Der Winkel \varphi und die Stromstärke I.", precision=2) 

some.tabelle([phi1a*1e3, I1a*1e9], finished_file="build/tab1a.tex", vars_name=[r"$\varphi / \si{\milli\radian}$", r"$I / \si{\nano\ampere}$"], label_text="tab1", caption_text=r"Der Winkel \varphi und die Stromstärke I aufgetragen.", precision=2) 

some.tabelle([phi2*1e3, I2*1e9], finished_file="build/tab2.tex", vars_name=[r"$\varphi / \si{\milli\radian}$", r"$I / \si{\nano\ampere}$"], label_text="tab1", caption_text=r"Der Winkel \varphi und die Stromstärke I aufgetragen.", precision=2) 

some.tabelle([phi3*1e3, I3*1e9], finished_file="build/tab3.tex", vars_name=[r"$\varphi / \si{\milli\radian}$", r"$I / \si{\nano\ampere}$"], label_text="tab1", caption_text=r"Der Winkel \varphi und die Stromstärke I aufgetragen.", precision=2) 

#extra values
welle= 532*1e-9 
dunkelstrom = 1.6*1e-9
spaltmittel= 0.00015 
linkerspalt= 0.000075
doppelspalt= 5.5e-4
spaltbreite= 78e-7
c = 7.0e-5

#functions 

def func1(phi, b, a, d):
    return a * b *(welle / (np.pi * b * np.sin(phi))) * np.sin((np.pi * b * np.sin(phi))/welle) +d

def func2(phi, b, a, d, c):
    return 2* c* np.cos((np.pi* a*np.sin(phi))/(welle)) *(welle / (np.pi * b * np.sin(phi))) * np.sin((np.pi * b * np.sin(phi))/welle) +d

d = dunkelstrom
#Generate curve-fit-Plot 
#Meter and Ampere
#params1, err1 = some.curvefit(x=phi1, y=np.sqrt(I1), num=1, x_add= 0, function = func1, x_name=r"$\phi / \si{\radian}$", y_name=r"$I / \si{\ampere}$", file_name="build/plot1.pdf", p0=[spaltmittel, 4*1e-3, d])

#params2, err2 = some.curvefit(x=phi2, y=np.sqrt(I2), num=2, x_add=0, function= func1, x_name=r"$\varphi /\si{\radian}$", y_name=r"$I / \si{\ampere}$", file_name="build/plot2.pdf", p0=[linkerspalt, 4*1e-3, d])

#params3, err3 = some.curvefit(x= phi3, y=np.sqrt(I3), num=3, x_add=0, function= func2, x_name=r"$\varphi / \si{\radian}$", y_name=r"I / \si{\ampere}", file_name="build/plot3.pdf", p0=[spaltbreite, spaltbreite, d])

params4, pcov = curve_fit(func2, phi3, np.sqrt(I3), p0=[doppelspalt, spaltbreite, d, c])

newphi3= np.linspace(phi3[0], phi3[-1], 10000)

plt.figure(4)
plt.plot(phi3, I3, "xr", label=r"Daten")
plt.plot(newphi3, func2(newphi3, *params4)**2, "k", label="Fit", linewidth=1.0)
plt.plot(newphi3, func2(newphi3, 5.5e-5, 48e-5, d, 7.0e-5)**2, "g", label="Theoriekurve", linewidth=1.0)
plt.xlabel(r"$\varphi / \si{\radian}$")
plt.ylabel(r"$I / \si{\ampere}$")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plot4.pdf")

file = open("build/solution2.txt", "w")
file.write(f"\nDie Spaltbreite b_experimentell= 5.5e-5 m\nDie Dicke zwischen den Spalten  s_experimentell= 48e-5 m Parameter a(Amplitude)=7.0e-5\nDunkelstrom d=\n1.6e-9")
file.close()
#millimeter and nanoampere
#params1a, err1a = some.curvefit(x=phi1, y=np.sqrt(I1*1e9), num=4, x_add= 0, function = func1, x_name=r"$\varphi / \si{\radian}$", y_name=r"$I / \si{\nano\ampere}$", file_name="build/plot4.pdf", p0=[spaltmittel*1e3, 1e-6, d*1e9])

#params2a, err2a = some.curvefit(x=phi2, y=np.sqrt(I2*1e9), num=5, x_add=0, function= func1, x_name=r"$\varphi /\si{\radian}$", y_name=r"$I / \si{\nano\ampere}$", file_name="build/plot5.pdf", p0=[linkerspalt, 2, d])

#params3a, err3a = some.curvefit(x= phi3, y=np.sqrt(I3*1e9), num=6, x_add=0, function= func1, x_name=r"$\varphi / \si{\radian}$", y_name=r"I / \si{\nano\ampere}", file_name="build/plot6.pdf", p0=[doppelspalt, 2, d])
#d1 = ufloat(params1[2], err1[2])
#d2 = ufloat(params2[2], err2[2])
#d3 = ufloat(params3[2], err3[2])
#d1 = d1**2
#d2 = d2**2
#d3 = d3**2
##save solution
#file = open("build/solution.txt", "w")
#file.write(f"1.Messung\nDie Spaltbreite b_literatur= {spaltmittel}\nDie Spaltbreite b_experimentell={params1[0]} +- {err1[0]}\nParameter a(Amplitude)={params1[1]} +- {err1[1]}\nDunkelstrom d={d1}\n\n2.Messung\nDie Spaltbreite b_literatur= {linkerspalt}\nDie Spaltbreite b_experimentell={params2[0]}+-{err2[0]}\nParameter a(Amplitude)={params2[1]} +- {err2[1]}\nDunkelstrom d={d2}\n\n3.Messung Doppelspalt\nDie Spaltbreite b_literatur= {doppelspalt} und die Spaltbreite x= {spaltbreite} \nDie Spaltbreite b_experimentell={params3[0]}+-{err3[0]}\nParameter a(Amplitude)={params3[1]} +- {err3[1]}\nDunkelstrom d={d3}\n")
#file.close()
