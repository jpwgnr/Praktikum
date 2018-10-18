import numpy as np
import uncertainties.unumpy as unp

#Erzeuge Daten T und A zum Quadrat
dist_data, T_data= np.genfromtxt("Id.txt", unpack=True)
a_2=(unp.uarray(dist_data,0.05)/100)**2 #Fehler von 0,05cm. /100 um auf m zu normieren und dann quadriert
T_2=(unp.uarray(T_data, 0.5)/10)**2 #Fehler von 0,5s /10 weil immer nach 10 Schwingungen gemessen wurde, anschließend quadriert.

np.savetxt("ErgebnisA.txt", a_2, fmt="%r")
np.savetxt("ErgebnisT.txt", T_2, fmt="%r")

#Id berechnen:

y_absch=unp.uarray(3.5,0) # gemessen in Graph, also durch lineare Regression bestimmt. Einheit ist s^2.

#Trägheitsmomente I1 und I2 der beiden Massen bestimmen:
m1=unp.uarray(0.22316,0) # gemessen, beide in kg
m2=unp.uarray(0.22224,0) 

d1=unp.uarray(0.035, 0.00005) # in m, d hier Radius des Gewichts


I1= 0.5* m1 *(d1**2) #Trägheitsmoment Gewicht 1
I2= 0.5* m2 *(d1**2) #Gewicht 2
#Mittelwert von D aus ErgebnisD.txt mit Fehler
D= unp.uarray(0.014088, 0.000027)

Id= y_absch*D/(4*np.pi**2) -I1 -I2 #Fehler nach Formel, siehe Theorie 
file= open("ErgebnisId.txt", "w")
file.write("Y-Abschnitt: {} \n Trägheitsmoment m1= {} \n Trägheitsmoment m2= {} \n Winkelrichtgröße D= {} \n Trägheitsmoment Id= {}".format(y_absch, I1, I2, D, Id))
file.close()
