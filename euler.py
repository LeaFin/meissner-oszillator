import numpy as np

from PyQt4 import QtGui, QtCore
backend = 'pyqt4'

import visvis as vv

app = vv.use(backend)

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

def w(t, y):
    c=0.000001
    l=0.1
    r=30
    u=5
    q=y.item(0)
    i=y.item(1)
    dI_dt = u/l-q/(c*l)-(r*i)/l
    return np.matrix([[i],[dI_dt]])


class MainWindow(QtGui.QWidget):
    def __init__(self, *args):
        QtGui.QWidget.__init__(self, *args)
        
        # Make a panel with a button
        self.panel = QtGui.QWidget(self)
        but = QtGui.QPushButton(self.panel)
        but.setText('Push me')
        
        # Make figure using "self" as a parent
        Figure = app.GetFigureClass()
        self.fig = Figure(self)
        
        # Make sizer and embed stuff
        self.sizer = QtGui.QHBoxLayout(self)
        self.sizer.addWidget(self.panel, 1)
        self.sizer.addWidget(self.fig._widget, 2)
        
        # Make callback
        but.pressed.connect(self._start_euler)
        
        # Apply sizers        
        self.setLayout(self.sizer)
        
        # Finish
        self.resize(560, 420)
        self.setWindowTitle('Meissner Oszillator')
        self.show()

    def _start_euler(self):

        # Make sure our figure is the active one. 
        # If only one figure, this is not necessary.
        #vv.figure(self.fig.nr)

        euler(1.3, 0, np.matrix('0;0'), 0.01, self)

    def plot(self, points):
        vv.clf()
        vv.boxplot([1,2,3,1,6])
