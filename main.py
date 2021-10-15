from PyQt5 import QtWidgets

from analytic_solution import AnalyticSolution
from graph_parameters import GraphParameters
from main_window import Ui_MainWindow
import sys
import numpy as np
import pyqtgraph as pg
from colors import *
from graphics_config import init
from plot_drawer import draw_plot


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        init()

        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curve = self.ui.graphicsView.plot(name="Line", pen=pg.mkPen(color=black, width=2))

        # self.random_plot()
        self.solution = AnalyticSolution(GraphParameters(1, 1, -10, 10, 1000))
        draw_plot(self.curve, self.solution.calculate_plot_points())

    def random_plot(self):
        random_array = np.random.random_sample(20)
        self.curve.setData([0, 2, 3.5, 5], [0.07348005, 0.80929058, 0.73979838, 0.64437829])


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
