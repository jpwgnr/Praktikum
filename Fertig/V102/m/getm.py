import numpy as np 
import uncertainties.unumpy as unp 
from uncertainties import ufloat

def newB(I):
    return (((4*np.pi)*1e-7)*8*I*390)/(np.sqrt(125)*78*(1e-1))

def T(data_T):
    return np.mean(data_T), np.std(data_T)

#variables

# T in s 
data_T1, data_T2, data_T3, data_T4, data_T5=np.genfromtxt("T.txt", unpack= True)
# L in cm transform to m
data_I=np.genfromtxt("I.txt", unpack= True)

I=unp.uarray(data_I, 0.021)
B= newB(I)
meanT1, stdT1= T(data_T1) 
T1= 1/(unp.uarray(meanT1, stdT1)**2)
meanT2, stdT2= T(data_T2)
T2=1/(unp.uarray(meanT2, stdT2)**2)
meanT3, stdT3= T(data_T3)
T3= 1/(unp.uarray(meanT3, stdT3)**2)
meanT4, stdT4= T(data_T4)
T4=1/(unp.uarray(meanT4, stdT4)**2)
meanT5, stdT5= T(data_T5)
T5= 1/(unp.uarray(meanT5, stdT5)**2)

T= np.array([T1, T2, T3, T4, T5])
file = open("ErgebnisB.txt", "w")
file.write("B: {}".format(B))
file.close()

file = open("ErgebnisT.txt", "w")
file.write("T: {}".format(T))
file.close()

x= np.zeros(5)
y= np.zeros(5)
for i in 0,1,2,3,4:
    x[i], y[i]= B[i].nominal_value, T[i].nominal_value
np.savetxt("xy.txt", np.column_stack([x,y]), header= "B in T, 1/T² in 1/s²")




