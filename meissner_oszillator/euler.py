from differential import w


def euler(t_end, t_start, y_start, h, figure):
    y = y_start
    t = t_start
    n = int((t_end - t_start) / h)
    h = (t_end - t_start) / n

    for i in range(n):
        k = w(t, y)
        y = y + k * h
        t = t + h
        figure.plot([t, y.item(0)])
