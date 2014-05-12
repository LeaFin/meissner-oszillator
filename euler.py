import numpy as np

from PyQt4 import QtGui, QtCore
backend = 'pyqt4'

from decimal import Decimal

import visvis as vv


app = vv.use(backend)

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
    c=0.3
    l=0.1
    r=0.3
    u0=0.5
    figure.plot([t, y.item(0)])
    u=y.item(0)
    i=y.item(1)
    dI_dt = u/l
    dU_dt = (u0-u)/r/c-i/c
    return np.matrix([[dU_dt],[dI_dt]])


class MainWindow(QtGui.QWidget):
    def __init__(self, *args):
        self.points = [[],[]]
        QtGui.QWidget.__init__(self, *args)

        # Make a panel with a button
        self.panel = QtGui.QWidget(self)
        but = QtGui.QPushButton(text="Simulation starten")
        cap_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=200, maximum=400)

        # Make figure using "self" as a parent
        Figure = app.GetFigureClass()
        self.fig = Figure(self)

        # Make sizer and embed stuff
        self.sizer = QtGui.QHBoxLayout(self)
        self.sizer.addWidget(self.panel, 1)
        self.sizer.addWidget(self.fig._widget, 3)

        self.panelLayout = QtGui.QVBoxLayout(self.panel)
        self.panelLayout.addWidget(but)
        self.panelLayout.addWidget(cap_slider)

        # Make callbacks
        but.pressed.connect(self._start_euler)
        cap_slider.valueChanged.connect(self._get_cap_val)

        # Apply sizers
        self.setLayout(self.sizer)
        self.panel.setLayout(self.panelLayout)

        # Finish
        self.resize(800, 420)
        self.setWindowTitle('Meissner Oszillator')
        self.show()

    def _start_euler(self):
        euler(6., 0, np.matrix('0;0'), 0.01, self)

    def _get_cap_val(self, val, *args, **kwargs):
        print Decimal(val) / 1000

    def plot(self, new_point):
        vv.clf()
        self.points[0].append(new_point[0])
        self.points[1].append(new_point[1])
        length = max(len(self.points[0]) - 130, 0)
        self.points[0] = self.points[0][length:]
        self.points[1] = self.points[1][length:]
        vv.plot(self.points[0], self.points[1], lw=0, mw=1, ms='.')
        self.fig.currentAxes.SetLimits((self.points[0][0], self.points[0][0]+1.5), (0, 0.7))
        self.fig.currentAxes.axis.showGrid = True
        self.fig.DrawNow()

if True:
    # The visvis way. Will run in interactive mode when used in IEP or IPython.
    app.Create()
    m = MainWindow()
    app.Run()

else:
    # The native way.
    qtApp = QtGui.QApplication([''])
    m = MainWindow()
    qtApp.exec_()
