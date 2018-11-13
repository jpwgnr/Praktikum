from table import TexTable
import numpy as np 

D1,x=np.genfromtxt("mitD1.txt", unpack=True)
D2,x=np.genfromtxt("ohneD1.txt", unpack=True)

tabD1 = TexTable([D1,D2,x], [r'$D(x)/\si{\milli\meter}$ ohne Gewicht', r'$D(x)/\si{\milli\meter}$ mit Gewicht', r'$x/\si{\centi\meter}$'])

tabD1.writeFile('../tables/tableD1.tex')

