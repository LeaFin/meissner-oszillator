import numpy as np

c=0.9
l=0.2
l2=0.03
r=5.0 # regler [1-2]
u0 = 20.


def w(t, y):
    u=y.item(0)
    i=y.item(1)
    dI_dt = u/l
    u2=l2*dI_dt
    u3=u0*(u2/3+1.0/2)

    dU_dt = (u3-u)/(r*c)-i/c

    return np.matrix([[dU_dt],[dI_dt]])
