import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 

#Generate data 
Uk1, Ik1= some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$U_\text{K} / \si{\volt}$", r"$I_\text{K} / \si{\nano\ampere}$"], label_text="taba", caption_text=r"Die Kathodenspannung und der Kathodenstrom bei einer Beschleunigungsspannung von $U_\text{B} = \SI{25}{\kilo\volt}$ und einem Anodenstrom von $I_\text{A} = \SI{1}{\milli\ampere}$ bei einem Blendenradius von $r_\text{B} = \SI{2}{\milli\meter}$." , precision=2)

Ik1= Ik1*1e-9

Uk2, Ik2= some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$U_\text{K} / \si{\volt}$", r"$I_\text{K} / \si{\nano\ampere}$"], label_text="taba", caption_text=r"Die Kathodenspannung und der Kathodenstrom bei einer Beschleunigungsspannung von $U_\text{B} = \SI{25}{\kilo\volt}$ und einem Anodenstrom von $I_\text{A} = \SI{1}{\milli\ampere}$ bei einem Blendenradius von $r_\text{B} = \SI{5}{\milli\meter}$." , precision=2)

Ik2= Ik2*1e-9

Ia3, Ik31, Ik32 = some.neueWerte(file_name="data/datac.txt", finished_file="build/tabc.tex",  vars_name=[r"$I_\text{K} / \si{\milli\ampere}$", r"$I_\text{K,1} / \si{\nano\ampere}$", r"$I_\text{K,2} / \si{\nano\ampere}$"], label_text="tabc", caption_text=r"Der Anodenstrom und der Kathodenstrom bei einer Beschleunigungsspannung von $U_\text{B} = \SI{25}{\kilo\volt}$ und einer Kathodenspannung $U_\text{K,1} = \SI{500}{\volt}$ und einer Kathodenspannung $U_\text{K,1} = \SI{300}{\volt}$ bei einem Blendenradius von $r_\text{B} = \SI{5}{\milli\meter}$." , precision=2)

Ia3 = Ia3 * 1e-6
Ik31 = Ik31 * 1e-9
Ik32 = Ik32 * 1e-9

Ub4, Ik41, Ik42 = some.neueWerte(file_name="data/datad.txt", finished_file="build/tabd.tex",  vars_name=[r"$U_\text{B} / \si{\milli\ampere}$", r"$I_\text{K,1} / \si{\nano\ampere}$", r"$I_\text{K,2} / \si{\nano\ampere}$"], label_text="tabc", caption_text=r"Die Beschleunigungsspannung und der Kathodenstrom bei einer Beschleunigungsspannung von $U_\text{B} = \SI{25}{\kilo\volt}$ und einer Kathodenspannung $U_\text{K,1} = \SI{500}{\volt}$ und einer Kathodenspannung $U_\text{K,1} = \SI{300}{\volt}$ bei einem Blendenradius von $r_\text{B} = \SI{5}{\milli\meter}$." , precision=2)

Ub4 = Ub4 * 1e3
Ik41 = Ik41 * 1e-9
Ik42 = Ik42 * 1e-9

#Generate table with calculated data

#extra values
Sat1 = 0.45*1e-9
Sat2 = 2.6*1e-9
V1 = 0.278*1e-4
V2 = 1.735*1e-4
#functions 
def quad(x, a, b):
    return a*x**2+b

#Generate linReg-Plot
some.linReg(x=Ia3, y=Ik31, x_name=r"I_\text{A} / \si{\ampere}", y_name=r"I_\text{K,1}", num=1,  x_add=0, file_name="build/plot1.pdf")
some.linReg(x=Ia3, y=Ik32, x_name=r"I_\text{A} / \si{\ampere}", y_name=r"I_\text{K,2}", num=2,  x_add=0, file_name="build/plot2.pdf")
some.linReg(x=Ub4, y=Ik41, x_name=r"U_\text{B} / \si{\volt}", y_name=r"I_\text{K,1}", num=3,  x_add=0, file_name="build/plot3.pdf")
some.linReg(x=Ub4, y=Ik42, x_name=r"U_\text{B} / \si{\volt}", y_name=r"I_\text{K,2}", num=4,  x_add=0, file_name="build/plot4.pdf")
#Generate curve-fit-Plot 
some.curvefit(x=Ub4, y=Ik41, num=5, x_add=0, function=quad, x_name=r"U_\text{B} / \si{\volt}", y_name=r"I_\text{K,2}", file_name="build/plot5.pdf")
some.curvefit(x=Ub4, y=Ik41, num=6, x_add=0, function=quad, x_name=r"U_\text{B} / \si{\volt}", y_name=r"I_\text{K,2}", file_name="build/plot6.pdf")

#Rechnung 
dichteluft= 1.2041 #kg/m^3
J1punkt = Sat1* 1/(V1*dichteluft) #A/kg
J2punkt = Sat2* 1/(V2*dichteluft) #A/kg
n = 1
ionenergie = 35 
D = 1 
Dpunkt = 1 

#save solution
file = open("build/solution.txt", "w")
file.write(f"Ergebnisse\na) Sättigungsstrom 1: {Sat1} A, Sättigungsstrom 2: {Sat2} A\nIonendosisrate Jpunkt1: {J1punkt} A/kg\n Ionendosisrate Jpunkt2: {J2punkt} A/kg\nAnzahl erzeugter Ionen: {n} Ionisationsenergie(Literatur): {ionenergie} Gy/(C/kg), Energiedosis D: {D}, Energiedosisrate: {Dpunkt}\n")
file.close()

