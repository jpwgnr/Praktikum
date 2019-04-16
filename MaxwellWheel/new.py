import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from scipy.optimize import curve_fit
from something import some 
from uncertainties import ufloat
#Generate data 
h, t= some.neueWerte(file_name="data/dataa.txt", finished_file="tabnewa.tex",  vars_name=[r"$h / \si{\meter}$", r"$t / \si{\second}$"], label_text="taba", caption_text=r"Die Höhe gegen die Zeit aufgetragen." , precision=2)

#some changes in data 
for i in range(1,len(t)): 
    t[i]=t[i]+t[i-1]


#Generate table with calculated data
some.tabelle([-np.log(h), t], finished_file="tabnew1.tex", vars_name=[r"$h / \si{\meter}$", r"$t / \si{\second}$"], label_text="tabnew", caption_text=r"Die Höhe gegen die Zeit aufgetragen.", precision=2) 
#extra values

#functions 
def func(x, a, b):
    return a*np.exp(x/b)
#Generate linReg-Plot
steigung1, yWert1, err1 = some.linReg(x=t, y=-np.log(h), x_name=r"$t / \si{\second} $", y_name=r"-log(h/a)", num=1,  x_add=0, file_name="plotnew1.pdf")
#Generate curve-fit-Plot 
some.plotten(x=t, y=h, num=2, x_add=0, x_name=r"$t / \si{\second}$", y_name=r"h / \si{\meter}", file_name="plotnew2.pdf")

#save solution
Steigung1 = ufloat(steigung1, err1) 
file = open("solutionnew.txt", "w")
file.write(f"Steigung = {1/Steigung1}\n")
file.close()

