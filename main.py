import sys

import pyqtgraph as pg
from PyQt5 import QtWidgets

from analytic_solution import AnalyticSolution
from colors import *
from eulers_method import EulersSolution
from graph_parameters import GraphParameters
from graphics_config import init
from main_window import Ui_MainWindow
from plot_drawer import draw_plot


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        init()

        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curve_analytic = self.ui.graphicsView.plot(pen=pg.mkPen(color=black, width=2))
        self.curve_eulers = self.ui.graphicsView.plot(pen=pg.mkPen(color=green, width=2))
        self.ui.plotButton.clicked.connect(self.plot)
        self.plot()

    def plot(self):
        gp = self.fetch_values()
        analytic_solution = AnalyticSolution(gp)
        eulers_method = EulersSolution(gp)
        draw_plot(self.curve_analytic, analytic_solution.calculate_plot_points())
        draw_plot(self.curve_eulers, eulers_method.calculate_plot_points())

    def fetch_values(self) -> GraphParameters:
        x0 = float(self.ui.x0_input.value())
        y0 = float(self.ui.y0_input.value())
        a = float(self.ui.a_input.value())
        b = float(self.ui.b_input.value())
        n = float(self.ui.pts_number_input.value())
        return GraphParameters(x0, y0, a, b, n)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
