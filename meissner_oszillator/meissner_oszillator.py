import numpy as np

from PyQt4 import QtGui, QtCore
backend = 'pyqt4'

from euler import euler
from runge_kutta import runge_kutta
from runge_kutta_simple import runge_kutta_simple

import visvis as vv


app = vv.use(backend)

c = 0.9
l = 0.2
l2 = 0.03
r = 5.0 # regler [1-2]
u0 = 20.


class MainWindow(QtGui.QWidget):
    def __init__(self, *args):
        self.points = [[],[]]
        self.points_i = [[],[]]
        QtGui.QWidget.__init__(self, *args)

        self.r = 5.0
        self.c = 0.9

        # Make a panel with a button
        self.panel = QtGui.QWidget(self)
        but_m = QtGui.QPushButton(text="Meissner Oszillator")
        but_s = QtGui.QPushButton(text="Schwingkreis")
        self.check_u = QtGui.QCheckBox(text="Kondensatorspannung")
        self.check_i = QtGui.QCheckBox(text="Strom durch Spule")
        self.check_u.nextCheckState()
        self.check_i.nextCheckState()
        resistor_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=10, maximum=100)
        resistor_slider.setSliderPosition(50)
        condensator_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=3, maximum=20)
        condensator_slider.setSliderPosition(9)

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
        self.panelLayout.addWidget(self.check_u)
        self.panelLayout.addWidget(self.check_i)
        self.panelLayout.addWidget(resistor_slider)
        self.panelLayout.addWidget(condensator_slider)

        # Make callbacks
        # but_m.pressed.connect(self._start_euler)
        but_m.pressed.connect(self._start_runge_kutta)
        but_s.pressed.connect(self._start_runge_kutta_simple)
        resistor_slider.valueChanged.connect(self._set_resistor_val)
        condensator_slider.valueChanged.connect(self._set_condensator_val)

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
        self.points_i = [[],[]]
        euler(300., 0, np.matrix('0;0'), 0.1, self)

    def _start_runge_kutta(self):
        self.points = [[],[]]
        self.points_i = [[],[]]
        runge_kutta(300., 0, np.matrix('0;0'), 0.1, self)

    def _start_runge_kutta_simple(self):
        self.points = [[],[]]
        self.points_i = [[],[]]
        runge_kutta_simple(300., 0, np.matrix('3;0'), 0.1, self)

    def _set_resistor_val(self, val, *args, **kwargs):
        self.r = float(val) / 10

    def _set_condensator_val(self, val, *args, **kwargs):
        self.c = float(val) / 10

    def plot(self, new_point):
        vv.clf()
        length = max(len(self.points[0]) - 90, len(self.points_i[0]) - 90, 0)
        if self.check_u.checkState():
            self.plot_point_set(new_point[:2], 'b', length)
        if self.check_i.checkState():
            self.plot_point_set([new_point[0], new_point[2]], 'r', length, i=True)
        first_point = self.points_i[0][0] if self.check_i.checkState() else self.points[0][0]
        self.fig.currentAxes.SetLimits((first_point, first_point+10), (-5, 5))
        self.fig.currentAxes.axis.showGrid = True
        self.fig.DrawNow()

    def plot_point_set(self, new_point, color, length, i=False):
        points = self.points_i if i else self.points
        points[0].append(new_point[0])
        points[1].append(new_point[1])
        points[0] = points[0][length:]
        points[1] = points[1][length:]
        vv.plot(points[0], points[1], lw=0, mw=1, ms='.', mc=color, mec=color)
        if i:
            self.points_i = points
        else:
            self.points = points


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
