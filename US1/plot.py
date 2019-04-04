import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from scipy.optimize import curve_fit
from something import some 

#Generate data 
l1, U11, t11, U12, t12   = some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$l/ \si{\milli\meter}$", r"$U_1/ \si{\volt}$", r"$t_1/ \si{\micro\second}$", r"$U_2/ \si{\volt}$", r"$t_2/ \si{\micro\second}$"], label_text="taba", caption_text=r"Die Länge der Zylinder und die Spannung mit den jeweiligen Zeitenpunkten der Ausschläge." , precision=2)
#Einheiten
l1= l1*1e-3
t11= t11*1e-6
t12=t12*1e-6

#Generate data 
t21, t22 = some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$t_1/ \si{\micro\second}$", r"$t_2/ \si{\micro\second}$"], label_text="tabb", caption_text=r"Die Zeiten beim Impuls-Echo-Verfahren." , precision=2)
#Einheiten
t21=t21*1e-6
t22=t22*1e-6

#Generate data 
t31, t32 = some.neueWerte(file_name="data/datac.txt", finished_file="build/tabc.tex",  vars_name=[r"$t_1/ \si{\micro\second}$", r"$t2/ \si{\micro\second}$"], label_text="tabc", caption_text=r"Die Zeiten beim Durschallungsverfahren." , precision=2)
#Einheiten
t31=t31*1e-6
t32=t32*1e-6

#Generate data 
tA, UA = some.neueWerte(file_name="data/datad.txt", finished_file="build/tabd.tex",  vars_name=[r"$t_1/ \si{\micro\second}$", r"$U_1/ \si{\volt}$"], label_text="tabd", caption_text=r"Das Auge und seine Daten." , precision=2)
tA=tA*1e-6
#calculate
t13=t12-t11
c = 2*l1 /t13 
t23=t22-t21 
t33=t32-t31

some.tabelle([-np.log(U12/U11), l1*1e3], finished_file="build/tab1.tex", vars_name=[r"$- ln(U2/U1)$", r"$l/ \si{\milli\meter}$"], label_text="tab1", caption_text=r"Der negative Logarithmus des Verhältnisses der Amplituden aufgetragen gegen die Längen $l$ des Zylinder.", precision=2) 

#Generate linReg-Plot 1
alpha, y1= some.linReg(x=l1*1e3 , y=-np.log(U12/U11), x_name=r"$l/ \si{\milli\meter}$", y_name=r"$- ln(U2/U1)$", num=1,  x_add=-3, file_name="build/plot1.pdf")

some.tabelle([t23*1e6, l1*1e3], finished_file="build/tab2.tex", vars_name=[r"$t/ \si{\micro\second}$", r"$l/ \si{\milli\meter}$"], label_text="tab2", caption_text=r"Die Zeit des Durchschallungsverfahrens gegen die Länge der Zylinder.", precision=2) 

#Generate linReg-Plot 2
c2, y2=some.linReg(x=t23*1e6 , y=l1*1e3, x_name=r"$t/ \si{\micro\second}$", y_name=r"$l/ \si{\milli\meter}$", num=2,  x_add=-3, file_name="build/plot2.pdf")

some.tabelle([t33*1e6, l1*1e3], finished_file="build/tab3.tex", vars_name=[r"$t/ \si{\micro\second}$", r"$l/ \si{\milli\meter}$"], label_text="tab3", caption_text=r"Die Zeit des Durchschallungsverfahrens gegen die Länge der Zylinder.", precision=2) 

#Generate linReg-Plot 3
c3, y3=some.linReg(x=t33*1e6 , y=l1*1e3, x_name=r"$t/ \si{\micro\second}$", y_name=r"$l/ \si{\milli\meter}$", num=3,  x_add=-3, file_name="build/plot3.pdf")

#Augenmodell 
c_theo1 = 1480
sA1= 0.5*c_theo1*(tA[2]-tA[1])
c_theo2 = 2500
sA2= 0.5*c_theo2*(tA[3]-tA[2])
c_theo3 = 1410
sA3= 0.5*c_theo3*(tA[4]-tA[3])

file = open("build/solution.txt", "w")
file.write(f"Ultraschall\nGeschwindigkeiten 1-5 = {c}\nDämpfungsfaktor= {alpha}\nGeschwindigkeit c2={c2*2}\nGeschwindigkeit c3={c3*2}\nAugenweite:\nStrecke 1={sA1}\nStrecke 2={sA2}\nStrecke 3={sA3}")
file.close()

