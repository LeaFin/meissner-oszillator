import numpy as np

from PyQt4 import QtGui, QtCore
backend = 'pyqt4'

from decimal import Decimal

from euler import euler
from runge_kutta import runge_kutta
from runge_kutta_simple import runge_kutta_simple

import visvis as vv


app = vv.use(backend)


class MainWindow(QtGui.QWidget):
    def __init__(self, *args):
        self.points = [[],[]]
        QtGui.QWidget.__init__(self, *args)

        # Make a panel with a button
        self.panel = QtGui.QWidget(self)
        but_m = QtGui.QPushButton(text="Meissner Oszillator")
        but_s = QtGui.QPushButton(text="Schwingkreis")
        cap_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=200, maximum=400)

        # Make figure using "self" as a parent
        Figure = app.GetFigureClass()
        self.fig = Figure(self)

        # Make sizer and embed stuff
        self.sizer = QtGui.QHBoxLayout(self)
        self.sizer.addWidget(self.panel, 1)
        self.sizer.addWidget(self.fig._widget, 3)

        self.panelLayout = QtGui.QVBoxLayout(self.panel)
        self.panelLayout.addWidget(but_m)
        self.panelLayout.addWidget(but_s)
        self.panelLayout.addWidget(cap_slider)

        # Make callbacks
        # but_m.pressed.connect(self._start_euler)
        but_m.pressed.connect(self._start_runge_kutta)
        but_s.pressed.connect(self._start_runge_kutta_simple)
        cap_slider.valueChanged.connect(self._get_cap_val)

        # Apply sizers
        self.setLayout(self.sizer)
        self.panel.setLayout(self.panelLayout)

        # Finish
        self.resize(800, 420)
        self.setWindowTitle('Meissner Oszillator')
        self.show()
        self.raise_()

    def _start_euler(self):
        self.points = [[],[]]
        euler(300., 0, np.matrix('0;0'), 0.1, self)

    def _start_runge_kutta(self):
        self.points = [[],[]]
        runge_kutta(300., 0, np.matrix('0;0'), 0.1, self)

    def _start_runge_kutta_simple(self):
        self.points = [[],[]]
        runge_kutta_simple(300., 0, np.matrix('3;0'), 0.1, self)

    def _get_cap_val(self, val, *args, **kwargs):
        print Decimal(val) / 1000

    def plot(self, new_point):
        vv.clf()
        self.points[0].append(new_point[0])
        self.points[1].append(new_point[1])
        length = max(len(self.points[0]) - 90, 0)
        self.points[0] = self.points[0][length:]
        self.points[1] = self.points[1][length:]
        vv.plot(self.points[0], self.points[1], lw=0, mw=1, ms='.')
        self.fig.currentAxes.SetLimits((self.points[0][0], self.points[0][0]+10), (-5, 5))
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
