import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from scipy.optimize import curve_fit
from something import some 


abstand = 1.113 
dunkelstrom = 1.6*1e-9 
#Generate data 
l1, I1 = some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="taba", caption_text=r"Die x Koordinate gegen die Stromstärke aufgetragen." , precision=1)
l1 = (l1-25.5)*1e-3 #Meter
I1 = I1*1e-9 -dunkelstrom #Ampere
phi1 = np.arcsin(l1/abstand)
l1a, I1a= some.neueWerte(file_name="data/dataaextra.txt", finished_file="build/taba2.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="taba2", caption_text=r"Die x Koordinate gegen die Länge aufgetragen." , precision=1)
l1a = (l1a-25.5)*1e-3 #Meter
I1a = I1a*1e-9 - dunkelstrom #Ampere 
phi1a = np.arcsin(l1a/abstand)
l2, I2 = some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="tabb", caption_text=r"Die x Koordinate gegen die Stromstärke aufgetragen." , precision=1)
l2= (l2-25.5)*1e-3 #Meter
I2= I2*1e-9 -dunkelstrom #Ampere  
phi2 = np.arcsin(l2/abstand)
l3, I3= some.neueWerte(file_name="data/datac.txt", finished_file="build/tabc.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="tabc", caption_text=r"Die x Koordinate gegen die Länge aufgetragen." , precision=1)
l3= (l3-25.5)*1e-3 #Meter
I3= I3*1e-9 -dunkelstrom #Ampere
phi3 = np.arcsin(l3/abstand)

#Generate table with calculated data
some.tabelle([phi1, I1*1e9], finished_file="build/tab1.tex", vars_name=[r"$\varphi / \si{\radian}$", r"$I / \si{\nano\ampere}$"], label_text="tab1", caption_text=r"Der Winkel \varphi gegen die Stromstärke I aufgetragen.", precision=2) 

some.tabelle([phi1a, I1a*1e9], finished_file="build/tab1.tex", vars_name=[r"$\varphi / \si{\radian}$", r"$I / \si{\nano\ampere}$"], label_text="tab1", caption_text=r"Der Winkel \varphi gegen die Stromstärke I aufgetragen.", precision=2) 

some.tabelle([phi2, I2*1e9], finished_file="build/tab1.tex", vars_name=[r"$\varphi / \si{\radian}$", r"$I / \si{\nano\ampere}$"], label_text="tab1", caption_text=r"Der Winkel \varphi gegen die Stromstärke I aufgetragen.", precision=2) 

some.tabelle([phi3, I3*1e9], finished_file="build/tab1.tex", vars_name=[r"$\varphi / \si{\radian}$", r"$I / \si{\nano\ampere}$"], label_text="tab1", caption_text=r"Der Winkel \varphi gegen die Stromstärke I aufgetragen.", precision=2) 

#extra values
welle= 532*1e-9 
spaltmittel= 0.0015 
linkerspalt= 0.00075
doppelspalt= 0.001
spaltbreite= 0.002

#functions 

def func1(phi, b, a):
    return a**2 * b**2 *(welle / (np.pi * b * np.sin(phi)))**2 * np.sin((np.pi * b * np.sin(phi))/welle)**2

#def func2(phi, b, a):
    #return 2*a *(welle/(2*np.pi *np.sin(phi)))* np.exp( i* b*np.pi* np.sin(phi)/welle )

#Generate curve-fit-Plot 
#Meter and Ampere
params1, err1 = some.curvefit(x=phi1, y=I1, num=1, x_add= 0, function = func1, x_name=r"$\phi / \si{\radian}$", y_name=r"$I / \si{\ampere}$", file_name="build/plot4.pdf", p0=[spaltmittel, 0.15])

params2, err2 = some.curvefit(x=phi2, y=I2, num=2, x_add=0, function= func1, x_name=r"$\varphi /\si{\radian}$", y_name=r"$I / \si{\ampere}$", file_name="build/plot5.pdf", p0=[linkerspalt, 2])

params3, err3 = some.curvefit(x= phi3, y=I3, num=3, x_add=0, function= func1, x_name=r"$\varphi / \si{\radian}$", y_name=r"I / \si{\ampere}", file_name="build/plot6.pdf", p0=[doppelspalt, 2])

#millimeter and nanoampere
params1a, err1a = some.curvefit(x=phi1, y=I1*1e9, num=4, x_add= 0, function = func1, x_name=r"$\varphi / \si{\radian}$", y_name=r"$I / \si{\nano\ampere}$", file_name="build/plot1.pdf", p0=[3, 8])

params2a, err2a = some.curvefit(x=phi2, y=I2*1e9, num=5, x_add=0, function= func1, x_name=r"$\varphi /\si{\radian}$", y_name=r"$I / \si{\nano\ampere}$", file_name="build/plot2.pdf", p0=[doppelspalt, 2])

params3a, err3a = some.curvefit(x= phi3, y=I3*1e9, num=6, x_add=0, function= func1, x_name=r"$\varphi / \si{\radian}$", y_name=r"I / \si{\nano\ampere}", file_name="build/plot3.pdf", p0=[doppelspalt, 2])

#save solution
file = open("build/solution.txt", "w")
file.write(f"1.Messung\nDie Spaltbreite b_literatur= {spaltmittel}\nDie Spaltbreite b_experimentell={params1[0]} +- {err1[0]}\n\n2.Messung\nDie Spaltbreite b_literatur= {linkerspalt}\nDie Spaltbreite b_experimentell={params2[0]}+-{err2[0]}\n\n3.Messung Doppelspalt\nDie Spaltbreite b_literatur= {doppelspalt} und die Spaltbreite x= {spaltbreite} \nDie Spaltbreite b_experimentell={params3[0]}+-{err3[0]}")
file.close()
