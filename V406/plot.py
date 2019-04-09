import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy import stats
from scipy.optimize import curve_fit
from something import some 

#Generate data 
l1, I1 = some.neueWerte(file_name="data/dataa.txt", finished_file="build/taba.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="taba", caption_text=r"Die x Koordinate gegen die Stromstärke aufgetragen." , precision=1)
l1 = l1*1e-3 #Meter
I1 = I1*1e-9 #Ampere
l1a, I1a= some.neueWerte(file_name="data/dataaextra.txt", finished_file="build/taba2.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="taba2", caption_text=r"Die x Koordinate gegen die Länge aufgetragen." , precision=1)
l1a = l1a*1e-3 #Meter
I1a = I1a*1e-9 #Ampere 
l2, I2 = some.neueWerte(file_name="data/datab.txt", finished_file="build/tabb.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="tabb", caption_text=r"Die x Koordinate gegen die Stromstärke aufgetragen." , precision=1)
l2= l2*1e-3 #Meter
I2= I2*1e-9 #Ampere  
l3, I3= some.neueWerte(file_name="data/datac.txt", finished_file="build/tabc.tex",  vars_name=[r"$l / \si{\milli\meter}$", r"$I / \si{\nano\ampere}$"], label_text="tabc", caption_text=r"Die x Koordinate gegen die Länge aufgetragen." , precision=1)
l3= l3*1e-3 #Meter
I3= I3*1e-9 #Ampere

#Generate table with calculated data
some.tabelle(vars, finished_file="tab<++>.tex", vars_name=[r"<++>", r"<++>"], label_text="tab<++>", caption_text=r"<++>", precision=2) 

#extra values
abstand = 1.113 
dunkelstrom = 1.6*1e-9 
welle= 532*1e-9 
spaltmittel= 0.0015 
linkerspalt= 0.00075
doppelspalt= 0.001
spaltbreite= 0.002

#functions 

#Generate curve-fit-Plot 
#Meter and Ampere
params1, err1 = some.curvefit(x=l1, y=I1, num=1, x_add= 5, function = func1, x_name=r"l / \si{\meter}", y_name=r"$I / \si{\ampere}$", file_name="build/plot1.pdf")

params2, err2 = some.curvefit(x=l2, y=I2, num=2, x_add=5, function= func1, x_name=r"l /\si{\meter}", y_name=r"$I / \si{\ampere}$", file_name="build/plot2.pdf")

params3, err3 = some.curvefit(x= l3, y=I3, num=3, x_add=5, function= func3, x_name=r"l / \si{\meter}", y_name=r"I / \si{\ampere}", file_name="build/plot3.pdf")

#millimeter and nanoampere
params1a, err1a = some.curvefit(x=l1*1e3, y=I1*1e9, num=4, x_add= 5, function = func1, x_name=r"l / \si{\milli\meter}", y_name=r"$I / \si{\nano\ampere}$", file_name="build/plot1.pdf")

params2a, err2a = some.curvefit(x=l2*1e3, y=I2*1e9, num=5, x_add=5, function= func1, x_name=r"l /\si{\milli\meter}", y_name=r"$I / \si{\nano\ampere}$", file_name="build/plot2.pdf")

params3a, err3a = some.curvefit(x= l3*1e3, y=I3*1e9, num=6, x_add=5, function= func3, x_name=r"l / \si{\milli\meter}", y_name=r"I / \si{\nano\ampere}", file_name="build/plot3.pdf")

#save solution
file = open("build/solution.txt", "w")
file.write(f"1.Messung\nDie Spaltbreite b_literatur= {spaltmittel}\nDie Spaltbreite b_experimentell={params1[0]} +- {err1[0]}\n\n2.Messung\nDie Spaltbreite b_literatur= {linkerspalt}\nDie Spaltbreite b_experimentell={params2[0]}+-{err2[0]}\n\n3.Messung Doppelspalt\nDie Spaltbreite b_literatur= {doppelspalt} und die Spaltbreite x= {spaltbreite} \nDie Spaltbreite b_experimentell={params3[0]}+-{err3[0]}")
file.close()

