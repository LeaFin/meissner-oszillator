import numpy as np
import math
def euler(t_end, t_start, y_start, h):
    y = y_start
    t = t_start
    n = int((t_end - t_start) / h)
    h = (t_start - t_end) / n
    for i in range(n):
        k = w(t, y)
        y = y + k * h
        t = t + h
    return y


def w(t,z):
    res = []
    C = 0.00001
    L = 0.2
    R = 30
    u = U(t)
    Q = z[0]
    I = z[1]
    Q2 = u/L - Q/(C*L) - (R*I)/L
    res.append(I)
    res.append(Q2)
    return res


def U(t):
    u = 10
    a = 0
    f = 400
    return u + a * math.sin(2*3.14*f*t) 
