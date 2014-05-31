import numpy as np


# differental equation for meissner oscillator
# evaluating one time step per call
def w(t, y, r, c, u0, l1, l12):
    u=y.item(0)
    i=y.item(1)
    dI_dt = u/l1
    u2=l12*dI_dt
    u3=u0*(u2/3+1.0/2)

    dU_dt = (u3-u)/(r*c)-i/c

    return np.matrix([[dU_dt],[dI_dt]])
