import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 
#Generate data 
p1, pulse1, max1= some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$p / \si{\milli\bar}$", r"$# \text{Pulse}$", r"$\text{Maximum Position}$"], label_text="taba", caption_text=r"Die Werte für den Druck in dem Glaszylinder, die Anzahl der Pulse und die Position des Maximums." , precision=1)
p2, pulse2, max2= some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$p / \si{\milli\bar}$", r"$# \text{Pulse}$", r"$\text{Maximum Position}$"], label_text="tabb", caption_text=r"Die Werte für den Druck in dem Glaszylinder, die Anzahl der Pulse und die Position des Maximums." , precision=1)
twelve, pulse3 = some.neueWerte(file_name="data/datac.txt", finished_file="build/tab100.tex",  vars_name=[r"$\text{Anzahl}$"], label_text="tab100", caption_text=r"Die Werte für den Druck in dem Glaszylinder, die Anzahl der Pulse und die Position des Maximums." , precision=1)
#Generate table with calculated data
some.tabelle([pulse3[0:19],pulse3[20:39],pulse3[40:59],pulse3[60:79],pulse3[80:99]], finished_file="tabc.tex", vars_name=[r"Pulse", r"Pulse", r"Pulse", r"Pulse", r"Pulse"], label_text="tabc", caption_text=r"Die Pulse wurden zur Analyse der Statistik des Radioaktiven Zerfalls bestimmt.", precision=1) 

#extra values
p0 = 1013 
x01 = 0.027
x02 = 0.02
#functions 

x1 =  x01* p1/p0
x2 =  x02* p2/p0

max1 = 1120/max1 * 4e6
max2 = 1099/max2 * 4e6

Steigung1, yAbschnitt1, err1 = some.linReg(x=x1, y=pulse1, p=x1[16:19], q=pulse1[16:19], x_name=r"$x_1 / \si{\meter}$", y_name=r"$\frac{N}{\SI{120}{\second}}$", num=1,  x_add=0.001, file_name="build/plota.pdf")
Steigung2, yAbschnitt2, err2 = some.linReg(x=x1, y=max1, p=x1[10:15], q=max1[10:15], x_name=r"$x_1 / \si{\meter}$", y_name=r"$E / \si{\electronvolt}$", num=2,  x_add=0, file_name="build/plotb.pdf")

mitReichw1 = (1/2 * pulse1[0] - yAbschnitt1)/Steigung1
EnergiemitReichw1 = 1234


some.tabelle([x1, pulse1, max1], finished_file="tab1.tex", vars_name=[r"$x_1 / \si{\meter}$", r"$# \text{Pulse}$", r"\text{Maximum Position}"], label_text="tab1", caption_text=r"Die Reichweite $x_1$, die Anzahl der Impulse und die Position des Maximums.", precision=2) 
some.tabelle([x2, pulse2, max2], finished_file="tab2.tex", vars_name=[r"$x_2 / \si{\meter}$", r"$# \text{Pulse}$", r"\text{Maximum Position}"], label_text="tab2", caption_text=r"Die Reichweite $x_2$, die Anzahl der Impulse und die Position des Maximums.", precision=2) 
#some.tabelle(, finished_file="tab<++>.tex", vars_name=[r"<++>", r"<++>"], label_text="tab<++>", caption_text=r"<++>", precision=2) 
#Generate linReg-Plot
#some.linReg(x=<++>, y=<++>, x_name=r"<++>", y_name=r"<++>", num=<++>,  x_add=<++>, file_name="build/plot<++>.pdf")
#Generate curve-fit-Plot 
#some.curvefit(x=<++>, y=<++>, num=<++>, x_add=<++>, function=<++>, x_name=r"<++>", y_name=r"<++>", file_name="build/plot<++>.pdf")

#def gauß(x, mean, std):
#    return 1/np.sqrt(4*np.pi*std**2) *np.exp(-(x-mean)**2/(2*std**2)) 

mean = pulse3.mean()
std = pulse3.std()
np.random.seed(42)
gauß = np.random.normal(mean, std, 10000)
poisson = np.random.poisson(mean, 10000)

plt.figure(3) 
plt.hist(pulse3, bins=20, label="Daten", density=True)
plt.hist(gauß, bins=20, label="Gauß", density= True, histtype='step')
plt.hist(poisson, bins=20, label="Poisson", density = True, histtype='step')
plt.ylabel("Anzahl")
plt.xlabel("Pulse")
plt.legend(loc="best")
plt.tight_layout()
plt.savefig("build/plotc.pdf") 



#save solution
#file = open("build/solution.txt", "w")
#file.write(f"Steigung = {Steigung1} Fehler: {Fehler}")
#file.close()

