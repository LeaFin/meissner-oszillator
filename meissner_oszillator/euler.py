from differential import w


# Implementation of euler algorightm
def euler(t_end, t_start, y_start, h, figure):
    y = y_start
    t = t_start
    n = int((t_end - t_start) / h)  # number of steps in given time
    h = (t_end - t_start) / n  # duration of timestep

    for i in range(n):
        # calling differatial equation for time and inputarray y, and inputvalues
        k = w(t, y, r=figure.r, c=figure.c, u0=figure.u0, l1=figure.l1, l12=figure.l12)
        y = y + k * h
        t = t + h
        figure.plot([t, y.item(0), y.item(1)]) # plot new point
