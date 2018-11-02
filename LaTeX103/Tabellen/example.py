from table import TexTable
import numpy as np 
D1,x=np.genfromtxt("mitD1.txt", unpack=True)
D2,x=np.genfromtxt("ohneD1.txt", unpack=True)

tabD1 = TexTable([D1,D2,x], ['D(x)ohne', 'D(x)mit', 'x'])

tabD1.writeFile('../tables/tableD1.tex')

x2, D2a,D2b=np.genfromtxt("D2.txt", unpack=True)

tabD2 = TexTable([D2a,D2b,x2], ['D(x)ohne', 'D(x)mit', 'x'])

tabD2.writeFile('../tables/tableD2.tex')

x3a, D3aa,D3ab=np.genfromtxt("D3a.txt", unpack=True)

tabD3a = TexTable([D3aa,D3ab,x3a], ['D(x)ohne', 'D(x)mit', 'x'])

tabD3a.writeFile('../tables/tableD3a.tex')


x3b,D3ba,D3bb=np.genfromtxt("D3b.txt", unpack=True)

tabD3b = TexTable([D3ba,D3bb,x3b], ['D(x)ohne', 'D(x)mit', 'x'])

tabD3b.writeFile('../tables/tableD3b.tex')


newD1, newx1=np.genfromtxt("newDnewX1.txt", unpack=True)

tabnew1 = TexTable([newD1,newx1], ['D(x) in m', 'x in m³'])

tabnew1.writeFile('../tables/tablenew1.tex')


newD2, newx2=np.genfromtxt("newDnewX2.txt", unpack=True)

tabnew2 = TexTable([newD2,newx2], ['D(x) in m', 'x in m³'])

tabnew2.writeFile('../tables/tablenew2.tex')

newD3a, newx3a=np.genfromtxt("newDnewX3a.txt", unpack=True)

tabnew3a = TexTable([newD3a,newx3a], ['D(x) in m', 'x in m³'])

tabnew3a.writeFile('../tables/tablenew3a.tex')

newD3b, newx3b=np.genfromtxt("newDnewX3b.txt", unpack=True)

tabnew3b = TexTable([newD3b,newx3b], ['D(x) in m', 'x in m³'])

tabnew3b.writeFile('../tables/tablenew3b.tex')
