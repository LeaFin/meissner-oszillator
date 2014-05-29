from differential import w


def runge_kutta(t_end, t_start, y_start, h, figure):
    y = y_start
    t = t_start

    n = int((t_end - t_start) / h)
    h = float((t_end - t_start) / n)

    for i in range(n):
        ka = w(t, y)
        ya = y + h/2 * ka
        ta = t + h/2

        kb = w(ta, ya)
        yb = y + h/2*kb
        tb = t + h/2

        kc = w(tb,yb)
        yc = y + h * kc
        tc = t + h

        kd = w(tc , yc)

        k = (1. / 6) * ((ka + 2 * kb + 2 * kc + kd))

        y = y + k * h
        t = t + h
        figure.plot([t, y.item(0), y.item(1)])
