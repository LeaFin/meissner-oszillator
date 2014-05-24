import numpy as np

c=10
l=0.2
l2=0.02
r=1 # regler [1-2]


def runge_kutta(t_end, t_start, y_start, h, figure):
    y = y_start
    t = t_start

    n = int((t_end - t_start) / h)
    h = float((t_end - t_start) / n)

    for i in range(n):
        u0 = 50 #+50*sin(2*3.141*0*t)
        if t > 2:
            u0 = 0
        ka = w(t, y, u0)
        ya = y + h/2 * ka
        ta = t + h/2

        kb = w(ta, ya, u0)
        yb = y + h/2*kb
        tb = t + h/2

        kc = w(tb,yb, u0)
        yc = y + h * kc
        tc = t + h

        kd = w(tc , yc, u0)

        k = (1. / 6) * ((ka + 2 * kb + 2 * kc + kd))

        y = y + k * h
        t = t + h
        figure.plot([t, y.item(0)])



def w(t, y, u0):
    u=y.item(0)
    i=y.item(1)
    dI_dt = u/l
    u2=l2*dI_dt
    u3=10*u2

    dU_dt = (u0+u3-u)/(r*c)-i/c

    return np.matrix([[dU_dt],[dI_dt]])

