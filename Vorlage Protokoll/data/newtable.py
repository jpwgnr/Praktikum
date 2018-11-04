from table import TexTable
import numpy as np 

G1, L1,d1=np.genfromtxt("Stab1.txt", unpack=True)

Stab1 = TexTable([G1, L1, d1], [r'Gewicht$/\si{\gram}$', r'Länge$/\si{\centi\meter}$', 'Durchmesser$/\si{\milli\meter}$'])

Stab1.writeFile('../tables/Stab1.tex')

