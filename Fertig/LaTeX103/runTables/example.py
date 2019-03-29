from table import TexTable
import numpy as np 
D1,x=np.genfromtxt("mitD1.txt", unpack=True)
D2,x=np.genfromtxt("ohneD1.txt", unpack=True)

tabD1 = TexTable([D1,D2,x], [r'$D(x)/\si{\milli\meter}$ ohne Gewicht', r'$D(x)/\si{\milli\meter}$ mit Gewicht', r'$x/\si{\centi\meter}$'])

tabD1.writeFile('../tables/tableD1.tex')

x2, D2a,D2b=np.genfromtxt("D2.txt", unpack=True)

tabD2 = TexTable([D2a,D2b,x2], [r'$D(x)/\si{\milli\meter}$ ohne Gewicht', r'$D(x)/\si{\milli\meter}$ mit Gewicht', r'$x/\si{\centi\meter}$'])

tabD2.writeFile('../tables/tableD2.tex')

x3a, D3aa,D3ab=np.genfromtxt("D3a.txt", unpack=True)

tabD3a = TexTable([D3aa,D3ab,x3a], [r'$D(x)/\si{\milli\meter}$ ohne Gewicht', r'$D(x)/\si{\milli\meter}$ mit Gewicht', r'$x/\si{\centi\meter}$'])

tabD3a.writeFile('../tables/tableD3a.tex')


x3b,D3ba,D3bb=np.genfromtxt("D3b.txt", unpack=True)

tabD3b = TexTable([D3ba,D3bb,x3b], [r'$D(x)/\si{\milli\meter}$ ohne Gewicht', r'$D(x)/\si{\milli\meter}$ mit Gewicht', r'$x/\si{\centi\meter}$'])

tabD3b.writeFile('../tables/tableD3b.tex')


newD1, newx1=np.genfromtxt("newDnewX1.txt", unpack=True)

tabnew1 = TexTable([newD1,newx1], ['$D(x)/\si{\meter}$ Differenz', r'$Lx^2-x^3/3 /\si{\cubic\meter}$'])
tabnew1.setRowRounding(5, 3)
tabnew1.writeFile('../tables/tablenew1.tex')


newD2, newx2=np.genfromtxt("newDnewX2.txt", unpack=True)
tabnew2 = TexTable([newD2,newx2], [r'$D(x)/\si{\meter}$ Differenz', r'$Lx^2-x^3/3 /\si{\cubic\meter}$'])

tabnew2.setRowRounding(5, 3)
tabnew2.writeFile('../tables/tablenew2.tex')

newD3a, newx3a=np.genfromtxt("newDnewX3a.txt", unpack=True)

tabnew3a = TexTable([newD3a,newx3a], [r'$D(x)/\si{\meter}$ Differenz', r'$3L^2x-4x^3 /\si{\cubic\meter}$'])

tabnew3a.setRowRounding(5, 3)
tabnew3a.writeFile('../tables/tablenew3a.tex')

newD3b, newx3b=np.genfromtxt("newDnewX3b.txt", unpack=True)

tabnew3b = TexTable([newD3b,newx3b], [r'$D(x)/\si{\meter}$ Differenz', r'$4x^3-12Lx^2+9L^2x-L^3 /\si{\cubic\meter}$'])

tabnew3b.setRowRounding(5, 3)
tabnew3b.writeFile('../tables/tablenew3b.tex')

G1, L1,d1=np.genfromtxt("Stab1.txt", unpack=True)
G2, L2,d2=np.genfromtxt("Stab2.txt", unpack=True)
G3, L3,d3=np.genfromtxt("Stab3.txt", unpack=True)

Stab1 = TexTable([G1, L1, d1], [r'Gewicht$/\si{\gram}$', r'Länge$/\si{\centi\meter}$', 'Durchmesser$/\si{\milli\meter}$'])
Stab2 = TexTable([G2, L2, d2], [r'Gewicht$/\si{\gram}$', r'Länge$/\si{\centi\meter}$', 'Durchmesser$/\si{\milli\meter}$'])
Stab3 = TexTable([G3, L3, d3], [r'Gewicht$/\si{\gram}$', r'Länge$/\si{\centi\meter}$', 'Durchmesser$/\si{\milli\meter}$'])

Stab1.writeFile('../tables/Stab1.tex')
Stab2.writeFile('../tables/Stab2.tex')
Stab3.writeFile('../tables/Stab3.tex')
