import numpy as np 
import uncertainties.unumpy as unp

#Kugel, Gewicht m in kg, Radius d in m 
m= unp.uarray(0.8119, 0)
d= unp.uarray(0.13295, 0.00005)

#Zylinder, Gewicht m2 in kg, Radius d2 m
m2=unp.uarray(1.00528, 0)
d2=unp.uarray(0.07795, 0.00005)

#Formeln für Trägheitsmoment Kugel, bzw. Zylinder Theorie 
ItheoKugel= 0.4*m*((d/2)**2)
ItheoZylinder= 0.5*m2*((d2/2)**2)

#Experimental Daten
data_T= np.genfromtxt("Kugel.txt", unpack=True)
data_T2= np.genfromtxt("Zylinder.txt", unpack=True)
T= unp.uarray(data_T, 0.5)/10 #in s und wieder /10  wegen der zehn Schwingungen
T2= unp.uarray(data_T2, 0.5)/10

#Den Mittelwert von T(Kugel) und T2(Zylinder) bilden
Mittel_T= sum(T)/len(T)
Mittel_T2=sum(T2)/len(T2)

# D[N*m] und Id[kg*m²] aus ErgebnisId.txt
D= unp.uarray(0.014088, 0.000027)
Id= unp.uarray(0.0009762, 0.0000025)

#Formel für beide aus Theorie Teil des Protokolls entnehmen 
IexpKugel= (((Mittel_T)**2/(2*np.pi)**2)*D)-Id 
IexpZylinder=  (((Mittel_T2)**2/(2*np.pi)**2)*D)-Id  
file = open("ErgebnisKugelundZylinder.txt", "w")
file.write("Theoretisches Trägheitsmoment Kugel: {}\n Theoretisches Trägheitsmoment Zylinder: {} \n Mittelwert T Kugel: {} \n Mittelwert T Zylinder: {} \n Winkelrichtgröße D= {}\n Trägheitsmoment Id: {} \n Trägheitsmoment Kugel exp.: {} \n Trägheitsmoment Zylinder exp.: {}".format(ItheoKugel, ItheoZylinder, Mittel_T, Mittel_T2, D, Id, IexpKugel, IexpZylinder))
file.close()



