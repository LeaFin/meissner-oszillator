from differential import w


def runge_kutta(t_end, t_start, y_start, h, figure):
    y = y_start
    t = t_start

    n = int((t_end - t_start) / h)
    h = float((t_end - t_start) / n)

    for i in range(n):
        ka = w(t, y, r=figure.r, c=figure.c, u0=figure.u0, l1=figure.l1, l12=figure.l12)
        ya = y + h/2 * ka
        ta = t + h/2

        kb = w(ta, ya, r=figure.r, c=figure.c, u0=figure.u0, l1=figure.l1, l12=figure.l12)
        yb = y + h/2*kb
        tb = t + h/2

        kc = w(tb, yb, r=figure.r, c=figure.c, u0=figure.u0, l1=figure.l1, l12=figure.l12)
        yc = y + h * kc
        tc = t + h

        kd = w(tc , yc, r=figure.r, c=figure.c, u0=figure.u0, l1=figure.l1, l12=figure.l12)

        k = (1. / 6) * ((ka + 2 * kb + 2 * kc + kd))

        y = y + k * h
        t = t + h
        figure.plot([t, y.item(0), y.item(1)])
