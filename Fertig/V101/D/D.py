import numpy as np 
import uncertainties.unumpy as unp
# Phi und F Daten aus der Textdatei holen
phi_data,F_data= np.genfromtxt("D.txt", unpack=True)

#Setze r auf gemessenen Wert, F und Phi sind ohne Fehler
r= unp.uarray(0.259,0.0005) 
F=unp.uarray(F_data, 0)
phi= unp.uarray(phi_data, 0) *2*np.pi/360 #rechne Phi von Grad in Bogenmaß um

#Erzeuge Array mit Werten von D
D=( F*r)/phi

# Bestimme Mittelwert von D, dank uncertainties ist Fehler direkt dabei
D_mittel=sum(D)/len(D)


file = open("ErgebnisD.txt", "w")
file.write("Einzelwerte von D: {} \n Mittelwert von D: {} ".format(D, D_mittel))
file.close()
