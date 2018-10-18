import numpy as np 
import uncertainties.unumpy as unp 

data_T1= np.genfromtxt("Puppe1.txt", unpack=True)
data_T2= np.genfromtxt("Puppe2.txt", unpack=True)

T1= unp.uarray(data_T1,0.5)/10
T2= unp.uarray(data_T2,0.5)/10

D= unp.uarray(0.014088, 0.000027)
Id=unp.uarray(0.0009762, 0.0000025)

Mittel_T1= sum(T1)/len(T1)
Mittel_T2= sum(T2)/len(T2) 

Ipos1=(((Mittel_T1)**2/(2*np.pi)**2)*D)-Id 
Ipos2= (((Mittel_T2)**2/(2*np.pi)**2)*D)-Id

file = open("ErgebnisPuppeExp.txt", "w")
file.write("Trägheitsmoment Position 1: {}\n  Trägheitsmoment Position 2:{}".format(Ipos1, Ipos2))
