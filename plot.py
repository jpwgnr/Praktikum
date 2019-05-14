import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 
#Generate data 
anz1, ds1, de1 = some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"Anzahl", r"$d_\text{Start} / \si{\milli\meter}$", r"$d_\text{Start} / \si{\milli\meter}$"], label_text="taba", caption_text=r"Die Anzahl der Impulse, der Startwert auf der Millimeterschraube und der Endwert auf der Millimeterschraube." , precision=2)
anz2 = some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"Anzahl"], label_text="taba", caption_text=r"Die Anzahl der Impulse die innerhalb des Intervalls von $\Delta p= \SI{0.6}{\bar}$ erzeugt wurden." , precision=2)

ds1, de1, ds2, de2 = ds1/1e3, de1/1e3, ds2/1e3, de2/1e3

deltad1 = np.abs(ds1-de1)/5.017
deltad2 = np.abs(ds2-de2)/5.017

deltad1 = ufloat(deltad1.mean, deltad1.std)
deltad2 = ufloat(deltad2.mean, deltad2.std)

anz1 = ufloat(anz1.mean, anz1.std) 
anz2 = ufloat(anz2.mean, anz2.std)

b = 0.5 #m
lambda1 = 2*deltad1/anz1
deltan = anz2*lambda1/2 /b
#Generate table with calculated data
#some.tabelle(vars, finished_file="tab<++>.tex", vars_name=[r"<++>", r"<++>"], label_text="tab<++>", caption_text=r"<++>", precision=2) 
#extra values

#functions 

#Generate linReg-Plot
#some.linReg(x=<++>, y=<++>, x_name=r"<++>", y_name=r"<++>", num=<++>,  x_add=<++>, file_name="build/plot<++>.pdf")
#Generate curve-fit-Plot 
#some.curvefit(x=<++>, y=<++>, num=<++>, x_add=<++>, function=<++>, x_name=r"<++>", y_name=r"<++>", file_name="build/plot<++>.pdf")

#save solution
file = open("build/solution.txt", "w")
file.write(f"delta d 1 = {deltad1} m\nLambda = {lambda1} m delta d 2 = {deltad2} m\n delta n = {delta n}")
file.close()

