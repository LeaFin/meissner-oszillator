import numpy as np

c=10
l=0.2
l2=0.02
r=1 # regler [1-2]


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
    u0 = 50 #+50*sin(2*3.141*0*t)
    if t > 2:
        u0 = 0
    figure.plot([t, y.item(0)])
    u=y.item(0)
    i=y.item(1)
    dI_dt = u/l
    u2=l2*dI_dt
    u3=7.5*u2

    dU_dt = (u0+u3-u)/(r*c)-i/c
    return np.matrix([[dU_dt],[dI_dt]])
