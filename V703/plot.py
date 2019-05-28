import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from uncertainties import ufloat
from scipy.optimize import curve_fit
from something import some 
#Generate data 
U, N = some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"U / \si{\volt}", r"N"], label_text="taba", caption_text=r"Die angelegte Spannung des  Geiger-Müller-Zählrohrs ." , precision=<++>)
#Generate table with calculated data
some.tabelle(vars, finished_file="tab<++>.tex", vars_name=[r"<++>", r"<++>"], label_text="tab<++>", caption_text=r"<++>", precision=2) 
#extra values

#functions 

#Generate linReg-Plot
some.linReg(x=<++>, y=<++>, x_name=r"<++>", y_name=r"<++>", num=<++>,  x_add=<++>, file_name="build/plot<++>.pdf")
#Generate curve-fit-Plot 
some.curvefit(x=<++>, y=<++>, num=<++>, x_add=<++>, function=<++>, x_name=r"<++>", y_name=r"<++>", file_name="build/plot<++>.pdf")

#save solution
Steigung1 = <++> 
Fehler = <++>
file = open("build/solution.txt", "w")
file.write(f"Steigung = {Steigung1} Fehler: {Fehler}")
file.close()

