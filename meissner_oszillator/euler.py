import numpy as np

c=0.9
l=0.2
l2=0.02
r=23 # regler [1-2]


def euler(t_end, t_start, y_start, h, figure):
    y = y_start
    t = t_start
    n = int((t_end - t_start) / h)
    h = (t_end - t_start) / n

    for i in range(n):
        k = w(t, y, figure)
        y = y + k * h
        t = t + h


def w(t, y, figure):
    u0 = 20 #+50*sin(2*3.141*0*t)
    u=y.item(0)
    i=y.item(1)
    dI_dt = u/l
    u2=l2*dI_dt
    if u2 == 0:
        u2 = 1
    u3=u0*u2

    dU_dt = (u3-u)/(r*c)-i/c

    return np.matrix([[dU_dt],[dI_dt]])
