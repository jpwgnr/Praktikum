import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 
import scipy.constants as const
#Generate data 
U1, N1 = some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$U / \si{\volt}$", r"$\frac{N}{\SI{130}{\second}}$"], label_text="taba", caption_text=r"Die angelegte Spannung des elektrischen Feldes innerhalb des Geiger-Müller-Zählrohrs  und die Anzahl der jeweils gemessenen Impulse." , precision=1)
U2 ,N2, I2 = some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$U / \si{\volt}$", r"$\frac{N}{\SI{130}{\second}}$", r"$I / \si{\ampere}$"], label_text="tabb", caption_text=r"Die angelegte Spannung des elektrischen Feldes innerhalb des Geiger-Müller-Zählrohrs, die Anzahl der jeweils gemessenen Impulse und der Strom innerhalb des Geiger-Müller-Zählrohrs." , precision=2)
#Generate table with calculated data

t = 130 

N = N1/t 

N2 = N2/t 
errN2 = np.sqrt(N2)/t
N2 = unp.uarray(N2, errN2)

errN = np.sqrt(N1)/t



some.tabelle([U1, N, errN], finished_file="build/tab1.tex", vars_name=[r"$U / \si{\volt}$", r"$\frac{N}{\si{\second}$"], label_text="tab1", caption_text=r"Die Spannung $U$ gegen die Anzahl der Impulse pro Sekunde mit den dazugehörenden Fehlerwerten.", precision=1) 

def gerade(x, m, n):
    return m*x+n

steigung1, yabschnitt1, err1 = some.linReg(x=U1, y=N, yerr=errN, p=U1[3:15], q=N[3:15], x_name=r"$U / \si{\volt}$", y_name=r"$N / \frac{1}{\si{\second}}$", num=1,  x_add=30, file_name="build/plot1.pdf")

y450 = gerade(450, steigung1, yabschnitt1)
y500 = gerade(500, steigung1, yabschnitt1)
y550 = gerade(550, steigung1, yabschnitt1)

SteigPlat = (y550 - y450)/y500 *100

#some.tabelle(vars, finished_file="tab<++>.tex", vars_name=[r"<++>", r"<++>"], label_text="tab<++>", caption_text=r"<++>", precision=2) 
#extra values

tot1 = 20e-6*2.7

N1a = 9730/60 
errN1a = np.sqrt(N1a)/t
N1a = ufloat(N1a, errN1a)
N2a = 11918/60
errN2a = np.sqrt(N2a)/t
N2a = ufloat(N2a, errN2a)
N12a = 21187/60
errN12a = np.sqrt(N12a)/t
N12a = ufloat(N12a, errN12a)
tot2 = (N1a+N2a - N12a)/(2*N1a*N2a)

#functions 
deltaQ2 = I2 * 60/(N2/130)

deltaQ2e = deltaQ2/const.elementary_charge

some.tabelle([U2, I2, N2, deltaQ2, deltaQ2e], finished_file="build/tab2.tex", vars_name=[r"U / \si{\volt}", r"I / \si{\ampere}", r"N/second", r"$\Delta Q$", r"$\frac{\Delta Q}{\si{electroncharge}}$"], label_text="tab1", caption_text=r"Die Spannung, die Stromstärke, die Anzahl der Impulse, die transportierte Ladungsmenge und die transporte Ladungsmenge in Einheiten der Elementarladung.", precision=2) 
some.plot(U2, I2, x_name=r"$U / \si{\volt}$", y_name=r"$I / \si{\ampere}$", num=2, file_name="build/plot2.pdf")

#Generate linReg-Plot
#some.linReg(x=<++>, y=<++>, x_name=r"<++>", y_name=r"<++>", num=<++>,  x_add=<++>, file_name="build/plot<++>.pdf")
#Generate curve-fit-Plot 
#some.curvefit(x=<++>, y=<++>, num=<++>, x_add=<++>, function=<++>, x_name=r"<++>", y_name=r"<++>", file_name="build/plot<++>.pdf")

#save solution
file = open("build/solution.txt", "w")
file.write(f"V703\nSteigung = {steigung1} \nyabschnitt1: {yabschnitt1}\nSteigung Plateau = {SteigPlat} %/100V\nTotzeit aus Plot = {tot1} s\nTotzeit aus Messung = {tot2}\nN1= {N1a}\nN2= {N2a}\nN12= {N12a}")
file.close()

