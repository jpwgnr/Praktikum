import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 

#Generate data 
Uk1, Ik1= some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$U_\text{K} / \si{\volt}$", r"$I_\text{K} / \si{\nano\ampere}$"], label_text="taba", caption_text=r"Die Kathodenspannung und der Kathodenstrom bei einer Beschleunigungsspannung von $U_\text{B} = \SI{25}{\kilo\volt}$ und einem Anodenstrom von $I_\text{A} = \SI{1}{\milli\ampere}$ bei einem Blendenradius von $r_\text{B} = \SI{2}{\milli\meter}$." , precision=2)


some.plot(Uk1, Ik1, x_name=r"U_\text{k}/\si{\volt}", y_name=r"I_\text{k}/\si{\nano\ampere}", num=41, file_name="build/plota.pdf")
Ik1= Ik1*1e-9

Uk2, Ik2= some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$U_\text{K} / \si{\volt}$", r"$I_\text{K} / \si{\nano\ampere}$"], label_text="tabb", caption_text=r"Die Kathodenspannung und der Kathodenstrom bei einer Beschleunigungsspannung von $U_\text{B} = \SI{25}{\kilo\volt}$ und einem Anodenstrom von $I_\text{A} = \SI{1}{\milli\ampere}$ bei einem Blendenradius von $r_\text{B} = \SI{5}{\milli\meter}$." , precision=2)

some.plot(Uk2, Ik2, x_name=r"U_\text{k}/\si{\volt}", y_name=r"I_\text{k}/\si{\nano\ampere}", num=31, file_name="build/plotb.pdf")
Ik2= Ik2*1e-9

Ia3, Ik31, Ik32 = some.neueWerte(file_name="data/datac.txt", finished_file="build/tabc.tex",  vars_name=[r"$I_\text{K} / \si{\milli\ampere}$", r"$I_\text{K,1} / \si{\nano\ampere}$", r"$I_\text{K,2} / \si{\nano\ampere}$"], label_text="tabc", caption_text=r"Der Anodenstrom und der Kathodenstrom bei einer Beschleunigungsspannung von $U_\text{B} = \SI{25}{\kilo\volt}$ und einer Kathodenspannung $U_\text{K,1} = \SI{500}{\volt}$ und einer Kathodenspannung $U_\text{K,2} = \SI{300}{\volt}$ bei einem Blendenradius von $r_\text{B} = \SI{5}{\milli\meter}$." , precision=2)

Ia3 = Ia3 * 1e-6
Ik31 = Ik31 * 1e-9
Ik32 = Ik32 * 1e-9

Ub4, Ik41, Ik42 = some.neueWerte(file_name="data/datad.txt", finished_file="build/tabd.tex",  vars_name=[r"$U_\text{B} / \si{\milli\ampere}$", r"$I_\text{K,1} / \si{\nano\ampere}$", r"$I_\text{K,2} / \si{\nano\ampere}$"], label_text="tabd", caption_text=r"Die Beschleunigungsspannung und der Kathodenstrom bei einem Anodenstrom von $I_\text{A} = \SI{1}{\milli\ampere}$ und einer Kathodenspannung $U_\text{K,1} = \SI{500}{\volt}$ und einer Kathodenspannung $U_\text{K,2} = \SI{300}{\volt}$ bei einem Blendenradius von $r_\text{B} = \SI{5}{\milli\meter}$." , precision=2)

Ub4 = Ub4 * 1e3
Ik41 = Ik41 * 1e-9
Ik42 = Ik42 * 1e-9

#Generate table with calculated data

#extra values
Sat1 = 0.45*1e-9
Sat2 = 2.6*1e-9
V1 = 27.8*1e-6
V2 = 173.5*1e-6
#functions 
def quad(x, a, b):
    return a*x**2+b

#Generate linReg-Plot
steigung1, yabschnitt1, err1 = some.linReg(x=Ia3*1e9, y=Ik31*1e9, x_name=r"$I_\text{A} / \si{\nano\ampere}$", y_name=r"$I_\text{K,1} / \si{\nano\ampere}$", num=1,  x_add=-100, file_name="build/plot1.pdf")
steigung2, yabschnitt2, err2 = some.linReg(x=Ia3*1e9, y=Ik32*1e9, x_name=r"$I_\text{A} / \si{\nano\ampere}$", y_name=r"$I_\text{K,2} / \si{\nano\ampere}$", num=2,  x_add=-100, file_name="build/plot2.pdf")
#Generate curve-fit-Plot 
params3, err3 = some.curvefit(x=Ub4*1e-3, y=Ik41*1e9, num=3, x_add=-2, function=quad, x_name=r"$U_\text{B} / \si{\kilo\volt}$", y_name=r"$I_\text{K,2} / \si{\nano\ampere}$", file_name="build/plot3.pdf")
params4, err4 = some.curvefit(x=Ub4*1e-3, y=Ik42*1e9, num=4, x_add=-2, function=quad, x_name=r"$U_\text{B} / \si{\kilo\volt}$", y_name=r"$I_\text{K,2} / \si{\nano\ampere}$", file_name="build/plot4.pdf")

#Rechnung 
dichteluft= 1.2041 #kg/m^3
J1punkt = Sat1* 1/(V1*dichteluft) #A/kg
J2punkt = Sat2* 1/(V2*dichteluft) #A/kg
J = np.array([J1punkt, J2punkt])
mittelJ = ufloat(J.mean(), J.std())
n = mittelJ/1.6e-19
phi= 52.8e-19
P = n*phi 

#save solution
file = open("build/solution.txt", "w")
file.write(f"Ergebnisse\nSättigungsstrom 1: {Sat1} A\nSättigungsstrom 2: {Sat2} A\nIonendosisrate Jpunkt1: {J1punkt} A/kg\nIonendosisrate Jpunkt2: {J2punkt} A/kg\nIonendosisrate Jpunkt_Mittel= {mittelJ} A/kg\nAnzahl erzeugter Ionen pro kg und Sekunde: {n} kg^-1 s^-1\nIonisationsenergie(Literatur): {phi} J\nP_m: {P} J kg^-1 s^-1\n\nc)Parameter: \nSteigung1 = {steigung1}+-{err1}\nyAbschnitt1= {yabschnitt1}\nSteigung2 = {steigung2}+-{err2}\nyAbschnitt2= {yabschnitt2}\nd) Parameter:\nAmplitude3= {params3[0]}+-{err3[0]}\nyAbschnitt3 = {params3[1]}+-{err3[1]}\nAmplitude4= {params4[0]}+-{err4[0]}\nyAbschnitt4 = {params4[1]}+-{err4[1]}")
file.close()

