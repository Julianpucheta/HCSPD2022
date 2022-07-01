import numpy as np
import scipy as sp
import scipy.signal
from matplotlib import pyplot as plt
from pylab import *
h=1e-4;t_simul=1e-1;R=2.2e2;L=100e-3;C=100e-6;
##h=1e-9;t_simul=1e-3;R=2.2e3;L=10e-6;C=100e-9;
##
A=np.array([[-R/L, -1/L],[1/C,0]])
B=np.array([[1/L],[0]])
x1=np.linspace(0,0,int(t_simul/h))
x2=np.linspace(0,0,int(t_simul/h))
u=np.linspace(0,0,int(t_simul/h))
t=np.linspace(0,0,int(t_simul/h))
Va=np.array([0])
x=np.array([[0],[0]])
xp=np.array([[0],[0]])
####x2=x1 ojo , porque queda igualado para todo el programa
for ii in range(int(t_simul/h)):
  xp=np.matmul(A, x)+B*Va
  x=x+xp*h
  u[ii] = Va
  Va = 12
  x1[ii] = x[0]
  x2[ii] = x[1]
  t[ii] = ii*h
##end
fig, axs = plt.subplots(3)
fig.suptitle('Circuito RLC')
axs[0].plot(t, x1, linewidth =1.0)
axs[0].grid( True )
axs[0].set_ylabel('$i_L$')
axs[1].plot(t, x2, linewidth =1.0)
axs[1].set_ylabel('$v_c$')
axs[1].grid( True )
##plot(t, x2, linewidth =1.0)
axs[2].plot(t, u, linewidth =1.0)
axs[2].grid( True )
axs[2].set_ylabel('$V_a$')
axs[2].set_xlabel('Tiempo (s)')
##title('Motor CC')
grid( True )
show()
