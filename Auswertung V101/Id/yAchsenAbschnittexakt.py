import numpy as np 
from scipy import stats

data_x, data_y= np.genfromtxt("Id.txt", unpack=True)

x= (data_x/100)**2
y= (data_y/10)**2

slope, intercept, r_value, p_value, std_err= stats.linregress(x,y)

print( intercept )
