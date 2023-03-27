import numpy as np
import matplotlib.pyplot as plt

plt.axes(projection='polar')
r=2
radians=np.arange(0,(2*np.pi),0.01)
for theta in radians:
    plt.polar(theta,r,linewidth=2)
rs=np.arange(0,2,0.1)
ts=np.arange(0,(2*np.pi),np.pi/8)
for theta in ts:
    for rho in rs:
        plt.polar(theta,rho,'.g',linewidth=2,mfc='b')

plt.show()