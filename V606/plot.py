import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
import scipy.constants as const
from scipy.optimize import curve_fit
from something import some 
#Generate data 
f1, U1= some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"f / \si{\kilo\hertz}", r"U_A / \si{\milli\volt}"], label_text="taba", caption_text=r"Die Frequenz und die Ausgangsspannung bei einer Eingangsspannung $U_\text{E}= \SI{100}{\milli\volt}$." , precision=2)

def func(x, a, s, t):
    return a/np.pi * (s/(s**2 + (x- t)**2))

params, err = some.curvefit(f1, U1, function= func, x_name=r"f / \si{\kilo\hertz}", y_name=r"U_A / \si{\milli\volt}", num=1, file_name="build/plota2.pdf")

Q = 35.1/(35.3-34.95) 

U11, U21, R11, R21 = some.neueWerte(file_name="data/datab1.txt", finished_file="build/tabb1.tex",  vars_name=[r"U_\text{Br,1} / \si{\milli\volt}",r"U_\text{Br,2} / \si{\milli\volt}",r"5 \cdot R_\text{1} / \si{\milli\ohm}", r"5 \cdot R_\text{2} / \si{\milli\ohm}"], label_text="tabb1", caption_text=r"Die Brückenspannungen vor und nach dem Einlegen der Probe und die Widerstände vor- und nachher.", precision=2)
U11, U21, R11, R21 = U11*1e-3, U21*1e-3, 5*R11*1e-3, 5*R21*1e-3
U12, U22, R12, R22 = some.neueWerte(file_name="data/datab2.txt", finished_file="build/tabb2.tex",  vars_name=[r"U_\text{Br,1} / \si{\milli\volt}",r"U_\text{Br,2} / \si{\milli\volt}",r"5 \cdot R_\text{1} / \si{\milli\ohm}", r"5 \cdot R_\text{2} / \si{\milli\ohm}"], label_text="tabb2", caption_text=r"Die Brückenspannungen vor und nach dem Einlegen der Probe und die Widerstände vor- und nachher.", precision=2)
U12, U22, R12, R22 = U12*1e-3, U22*1e-3, 5*R12*1e-3, 5*R22*1e-3
U13, U23, R13, R23 = some.neueWerte(file_name="data/datab3.txt", finished_file="build/tabb3.tex",  vars_name=[r"U_\text{Br,1} / \si{\milli\volt}",r"U_\text{Br,2} / \si{\milli\volt}",r"5 \cdot R_\text{1} / \si{\milli\ohm}", r"5 \cdot R_\text{2} / \si{\milli\ohm}"], label_text="tabb3", caption_text=r"Die Brückenspannungen vor und nach dem Einlegen der Probe und die Widerstände vor- und nachher.", precision=2)
U13, U23, R13, R23 = U13*1e-3, U23*1e-3, 5*R13*1e-3, 5*R23*1e-3
U14, U24, R14, R24 = some.neueWerte(file_name="data/datab4.txt", finished_file="build/tabb4.tex",  vars_name=[r"U_\text{Br,1} / \si{\milli\volt}",r"U_\text{Br,2} / \si{\milli\volt}",r"5 \cdot R_\text{1} / \si{\milli\ohm}", r"5 \cdot R_\text{2} / \si{\milli\ohm}"], label_text="tabb4", caption_text=r"Die Brückenspannungen vor und nach dem Einlegen der Probe und die Widerstände vor- und nachher.", precision=2)
U14, U24, R14, R24 = U14*1e-3, U24*1e-3, 5*R14*1e-3, 5*R24*1e-3

dU1, dU2, dU3, dU4 = np.abs(U21-U11), np.abs(U22-U12), np.abs(U23-U13), np.abs(U24-U14)
dU = unp.uarray([dU1.mean(), dU2.mean(), dU3.mean(), dU4.mean()], [dU1.std(), dU2.std(), dU3.std(), dU4.std()])
dR1, dR2, dR3, dR4 = np.abs(R21-R11), np.abs(R22-R12), np.abs(R23-R13), np.abs(R24-R14)
dR = unp.uarray([dR1.mean(), dR2.mean(), dR3.mean(), dR4.mean()], [dR1.std(), dR2.std(), dR3.std(), dR4.std()])

#Generate table with calculated data
#some.tabelle(vars, finished_file="tab<++>.tex", vars_name=[r"<++>", r"<++>"], label_text="tab<++>", caption_text=r"<++>", precision=2) 

#extra values
R3 = 998 
USp = 0.68 
#functions 

def getchitheo(J, S, L, N, T, mu_b):
    """ Berechne den Wert für chi""" 
    gj = (3*J*(J+1)+(S*(S+1) - L*(L+1)))/(2*J*(J+1))
    chi = (const.mu_0 * mu_b**2 * gj**2 * N * J * (J+1))/(3* const.k * T)
    return chi, gj

def getchi1(dU, F, Q):
    return 4*(F*dU)/(Q*USp)

def getchi2(dR, F, Q):
    return 2*(dR*F)/(R3*Q)

laenge = 16e-2
M = np.array([7.87e-3, 14.08e-3, 9.0e-3, 14.38e-3])
m = np.array([545.87e-3, 373e-3, 362.5e-3, 336.48e-3 ])
rhoanders= 7.87e-3/(np.pi*(4e-3)**2 *laenge) # Masse ist die angeblich die gleiche wie auf Behälter
rho= np.array([rhoanders, 6.4e3, 7.24e3, 7.8e3]) 
mu_b = 0.5* const.e/const.electron_mass *const.hbar
N = 2* const.Avogadro * rho / m   
T = 273.15+20
J = np.array([4.0, 3.5, 4.5, 7.5])
L = np.array([5.0, 0.0, 6.0, 5.0])
S = np.array([1.0, 3.5, 1.5, 2.5])

chi_theo, G= getchitheo(J, S, L, N, T, mu_b)

Qreal = M/(laenge*rho)
F = 86.6e-6

chi1 = getchi1(dU, F, Qreal)
chi2 = getchi2(dR, F, Qreal)


some.tabelle([L, S, J, G], finished_file="build/tab1.tex", vars_name=[r"Maximaler Drehimpuls $L$", r"Gesamtspin $S$", r"Gesamtdrehimpuls $J$", r"Landé-Faktor $g_\text{J}$"], label_text="tab1", caption_text=r"Der maximale Drehimpuls, der Gesamtspin und der Drehimpuls ergeben sich zum Landé-Faktor für die vier verschiedenen Elemente.", precision=2) 
some.tabelle([M*1e3, rho, m*1e3], finished_file="build/tab2.tex", vars_name=[r"Masse $m$ \si{\gram}", r"Dichte $\rho_\text{W}$ / \si{\kilo\gram\per\cubic\meter}",r"Masse $m$ \si{\gram\per\mol}" ], label_text="tab2", caption_text=r"Die Masse der Probe und die Dichte des Probenmaterials. Für den ersten Stoff wurde dabei angenommen, dass die Dichte näherungsweise dieselbe ist, wie die Dichte der Probe. Die Dichte wurde hierbei mit dem Volumen und der angegebenen Probenmasse bestimmt. Für die anderen Stoffe war die Dichte in der Anleitung gegeben.", precision=2) 

#Generate linReg-Plot
#some.linReg(x=<++>, y=<++>, x_name=r"<++>", y_name=r"<++>", num=<++>,  x_add=<++>, file_name="build/plot<++>.pdf")
#Generate curve-fit-Plot 
#some.curvefit(x=<++>, y=<++>, num=<++>, x_add=<++>, function=<++>, x_name=r"<++>", y_name=r"<++>", file_name="build/plot<++>.pdf")

#save solution
#Steigung1 = <++> 
#Fehler = <++>
file = open("build/solution.txt", "w")
file.write(f"V606\nParameter: Cauchy Verteilung \n\nAmplitude a = {params[0]}+-{err[0]}\ns = {params[1]}+-{err[1]}\nt = {params[2]}+-{err[2]}\nf0 bei 99mV mit 35.1 kHz\nf1 und f2 bei 70.004 mV, bei 34.95 ca. bei 35.3\nQ = {Q}\nVerwendete Werte:\nTemperatur T = {T} K\n N= 2*n_A * rho / Masse\n\nchi_theo\t\t\t\t\t\tchi_1\t\t\t\t\t\tchi_2\n\nC6012PR2:\n{chi_theo[0]}\t\t{chi1[0]}\t\t{chi2[0]}\n\nGd2O3:\n{chi_theo[1]}\t\t{chi1[1]}\t\t{chi2[1]}\n\nNd203:\n{chi_theo[2]}\t\t{chi1[2]}\t\t{chi2[2]}\n\nDy203:\n{chi_theo[3]}\t\t{chi1[3]}\t\t{chi2[3]}\n")
file.close()

