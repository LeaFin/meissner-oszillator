"""
Entryfile for Meissner oscillator simulation
Run: python meissner_oszillator.py
"""

import numpy as np

from PyQt4 import QtGui, QtCore
backend = 'pyqt4'

from euler import euler
from runge_kutta import runge_kutta
from runge_kutta_simple import runge_kutta_simple

import visvis as vv


c = 0.9
l = 0.2
l2 = 0.03
r = 5.0 # regler [1-2]
u0 = 20.

app = vv.use(backend)


class MainWindow(QtGui.QWidget):

    # Setting up GUI with variables for simulation
    def __init__(self, *args):
        self.points = [[],[]]
        self.points_i = [[],[]]
        QtGui.QWidget.__init__(self, *args)

        self.r = 5.0
        self.c = 0.9
        self.u0 = 20
        self.l1 = 0.2
        self.l12 = 0.03

        # Make a panel
        self.panel = QtGui.QWidget(self)

        # Make all buttons, sliders for input
        but_m = QtGui.QPushButton(text="Meissner Oszillator")
        but_s = QtGui.QPushButton(text="Schwingkreis")
        self.check_u = QtGui.QCheckBox(text="Kondensatorspannung")
        self.check_i = QtGui.QCheckBox(text="Strom durch Spule")
        self.check_u.nextCheckState()
        self.check_i.nextCheckState()
        self.resistor_label = QtGui.QLabel(text="Widerstand: %.1f Ohm" % self.r)
        resistor_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=1, maximum=100)
        resistor_slider.setSliderPosition(50)
        self.condensator_label = QtGui.QLabel(text="Kondensator: %.1f F" % self.c)
        condensator_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=3, maximum=20)
        condensator_slider.setSliderPosition(9)
        self.source_label = QtGui.QLabel(text="Quelle: %.1f V" % self.u0)
        source_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=30, maximum=400)
        source_slider.setSliderPosition(200)
        self.inductor_label = QtGui.QLabel(text="Spule 1: %.2f H" % self.l1)
        inductor_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=10, maximum=200)
        inductor_slider.setSliderPosition(20)
        self.inductor2_label = QtGui.QLabel(text="Spule 2: %.3f H" % self.l12)
        inductor2_slider = QtGui.QSlider(QtCore.Qt.Horizontal, minimum=10, maximum=200)
        inductor2_slider.setSliderPosition(30)

        # Make figure using MainWindow as a parent
        Figure = app.GetFigureClass()
        self.fig = Figure(self)

        # Make sizer
        self.sizer = QtGui.QHBoxLayout(self)
        self.sizer.addWidget(self.panel, 1)
        self.sizer.addWidget(self.fig._widget, 3)

        # Set layout and embed everything
        self.panelLayout = QtGui.QVBoxLayout(self.panel)
        self.panelLayout.addWidget(but_m)
        self.panelLayout.addWidget(but_s)
        self.panelLayout.addWidget(self.check_u)
        self.panelLayout.addWidget(self.check_i)
        self.panelLayout.addWidget(self.resistor_label)
        self.panelLayout.addWidget(resistor_slider)
        self.panelLayout.addWidget(self.condensator_label)
        self.panelLayout.addWidget(condensator_slider)
        self.panelLayout.addWidget(self.source_label)
        self.panelLayout.addWidget(source_slider)
        self.panelLayout.addWidget(self.inductor_label)
        self.panelLayout.addWidget(inductor_slider)
        self.panelLayout.addWidget(self.inductor2_label)
        self.panelLayout.addWidget(inductor2_slider)

        # Make callbacks
        but_m.pressed.connect(self._start_runge_kutta)
        but_s.pressed.connect(self._start_runge_kutta_simple)
        resistor_slider.valueChanged.connect(self._set_resistor_val)
        condensator_slider.valueChanged.connect(self._set_condensator_val)
        source_slider.valueChanged.connect(self._set_source_val)
        inductor_slider.valueChanged.connect(self._set_inductor_val)
        inductor2_slider.valueChanged.connect(self._set_inductor2_val)

        # Apply sizers
        self.setLayout(self.sizer)
        self.panel.setLayout(self.panelLayout)

        # Finish
        self.resize(800, 420)
        self.setWindowTitle('Meissner Oszillator')
        self.show()
        self.raise_()

    # Starts simulation with euler algorithem
    def _start_euler(self):
        self.points = [[],[]]
        self.points_i = [[],[]]
        # Inputs: endtime, starttime, matrix with start voltage and start currency, timesteps, figure to plot
        euler(300., 0, np.matrix('0;0'), 0.1, self)

    # Starts simulation with runge_kutta algorithem
    def _start_runge_kutta(self):
        self.points = [[],[]]
        self.points_i = [[],[]]
        # Inputs: endtime, starttime, matrix with start voltage and start currency, timesteps, figure to plot
        runge_kutta(300., 0, np.matrix('0;0'), 0.1, self)

    # Starts simulation with runge_kutta algorithem for simple circuit
    def _start_runge_kutta_simple(self):
        self.points = [[],[]]
        self.points_i = [[],[]]
        # Inputs: endtime, starttime, matrix with start voltage and start currency, timesteps, figure to plot
        runge_kutta_simple(300., 0, np.matrix('%f;0' % self.u0), 0.1, self)

    # Setting input values on callbacks of sliders
    def _set_resistor_val(self, val, *args, **kwargs):
        self.r = float(val) / 10
        self.resistor_label.setText("Widerstand: %.1f Ohm" % self.r)

    def _set_condensator_val(self, val, *args, **kwargs):
        self.c = float(val) / 10
        self.condensator_label.setText("Kondensator: %.1f F" % self.c)

    def _set_source_val(self, val, *args, **kwargs):
        self.u0 = float(val) / 10
        self.source_label.setText("Quelle: %.1f V" % self.u0)

    def _set_inductor_val(self, val, *args, **kwargs):
        self.l1 = float(val) / 100
        self.inductor_label.setText("Spule 1: %.2f H" % self.l1)

    def _set_inductor2_val(self, val, *args, **kwargs):
        self.l12 = float(val) / 1000
        self.inductor2_label.setText("Spule 2: %.3f H" % self.l12)

    # Plotting new frame
    def plot(self, new_point):
        vv.clf()
        # checking amount of points
        length = max(len(self.points[0]) - 90, len(self.points_i[0]) - 90, 0)
        if self.check_u.checkState():
            # plots points for voltage if voltage is on
            self.plot_point_set(new_point[:2], 'b', length)
        if self.check_i.checkState():
            # plots points for currency if currency is on
            self.plot_point_set([new_point[0], new_point[2]], 'r', length, i=True)

        first_point = self.points_i[0][0] if self.check_i.checkState() else self.points[0][0]

        # set Axes limits on current time
        self.fig.currentAxes.SetLimits((first_point, first_point+10), (-5, 5))
        self.fig.currentAxes.axis.showGrid = True
        self.fig.DrawNow()

    def plot_point_set(self, new_point, color, length, i=False):
        points = self.points_i if i else self.points
        # appending new point and drop old if window is full
        points[0].append(new_point[0])
        points[1].append(new_point[1])
        points[0] = points[0][length:]
        points[1] = points[1][length:]
        vv.plot(points[0], points[1], lw=0, mw=1, ms='.', mc=color, mec=color)
        if i:
            self.points_i = points
        else:
            self.points = points

# Start programm
def main():
    app.Create()
    m = MainWindow()
    app.Run()

if  __name__ =='__main__':main()
