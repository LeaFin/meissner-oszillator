import numpy as np

c=0.9
l=0.2
r=0.1


def runge_kutta_simple(t_end, t_start, y_start, h, figure):
    y = y_start
    t = t_start

    n = int((t_end - t_start) / h)
    h = float((t_end - t_start) / n)

    for i in range(n):
        ka = w_simple(t, y)
        ya = y + h/2 * ka
        ta = t + h/2

        kb = w_simple(ta, ya)
        yb = y + h/2*kb
        tb = t + h/2

        kc = w_simple(tb,yb)
        yc = y + h * kc
        tc = t + h

        kd = w_simple(tc , yc)

        k = (1. / 6) * ((ka + 2 * kb + 2 * kc + kd))

        y = y + k * h
        t = t + h
        figure.plot([t, y.item(0), y.item(1)])



def w_simple(t, y):

    q=y.item(0)
    i=y.item(1)

    dI_dt = -q/(c*l)-(r*i)/l

    return np.matrix([[i],[dI_dt]])

