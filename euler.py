def euler(t_end, t_start, y_start, h, w):
    y = y_start
    t = t_start
    n = int((t_end - t_start) / h)
    h = (t_start - t_end) / n
    for i in range(n):
        k = w(t, y)
        y = y + k * h
        t = t + h
    return y