import sys

import pyqtgraph as pg
from PyQt5 import QtWidgets

from analytic_solution import AnalyticSolution
from colors import *
from eulers_method import EulersMethod
from graph_parameters import GraphParameters
from graphics_config import init
from improved_eulers_method import ImprovedEulersMethod
from main_window import Ui_MainWindow
from plot_drawer import draw_plot
from runge_kutta_method import RungeKuttaMethod


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        init()

        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.plots_enabled = dict()

        self.curve_analytic = self.ui.solution_plots.plot(pen=pg.mkPen(color=black, width=2))
        self.curve_eulers = self.ui.solution_plots.plot(pen=pg.mkPen(color=green, width=2))
        self.curve_improved_eulers = self.ui.solution_plots.plot(pen=pg.mkPen(color=red, width=2))
        self.curve_runge_kutta = self.ui.solution_plots.plot(pen=pg.mkPen(color=blue, width=2))

        self.curve_eulers_lte = self.ui.local_error_plot.plot(pen=pg.mkPen(color=green, width=2))
        self.curve_improved_eulers_lte = self.ui.local_error_plot.plot(pen=pg.mkPen(color=red, width=2))
        self.curve_runge_kutta_lte = self.ui.local_error_plot.plot(pen=pg.mkPen(color=blue, width=2))

        self.curve_eulers_gte = self.ui.global_error_plot.plot(pen=pg.mkPen(color=green, width=2))
        self.curve_improved_eulers_gte = self.ui.global_error_plot.plot(pen=pg.mkPen(color=red, width=2))
        self.curve_runge_kutta_gte = self.ui.global_error_plot.plot(pen=pg.mkPen(color=blue, width=2))

        self.check_boxes = [self.ui.analytic_check_box, self.ui.improved_euler_check_box, self.ui.euler_check_box,
                            self.ui.runge_kutta_check_box]
        self.ui.a_input.valueChanged.connect(self.plot)
        self.ui.b_input.valueChanged.connect(self.plot)
        self.ui.x0_input.valueChanged.connect(self.plot)
        self.ui.y0_input.valueChanged.connect(self.plot)
        self.ui.pts_number_input.valueChanged.connect(self.plot)
        self.init_check_boxes()
        self.plot()

    def init_check_boxes(self):
        for box in self.check_boxes:
            box.setChecked(True)
            box.stateChanged.connect(self.handle_check_box_state_changed)
        self.fetch_check_boxes_value()

    def fetch_check_boxes_value(self):
        for box in self.check_boxes:
            self.plots_enabled[box.text()] = box.isChecked()

    def handle_check_box_state_changed(self, state):
        self.fetch_check_boxes_value()
        self.plot()

    def plot(self):
        self.plot_solutions()
        self.plot_lte()

    def plot_solutions(self):
        gp = self.fetch_values()
        analytic_solution = AnalyticSolution(gp)
        eulers_method = EulersMethod(gp)
        improved_eulers_method = ImprovedEulersMethod(gp)
        runge_kutta_method = RungeKuttaMethod(gp)
        methods = [(analytic_solution, self.curve_analytic), (eulers_method, self.curve_eulers),
                   (improved_eulers_method, self.curve_improved_eulers), (runge_kutta_method, self.curve_runge_kutta)]
        for (method, curve) in methods:
            curve.clear()
            if self.plots_enabled[method.check_box_name]:
                draw_plot(curve, method.calculate_plot_points())

    def plot_lte(self):
        gp = self.fetch_values()
        eulers_method = EulersMethod(gp)
        improved_eulers_method = ImprovedEulersMethod(gp)
        runge_kutta_method = RungeKuttaMethod(gp)
        methods = [(eulers_method, self.curve_eulers_lte), (improved_eulers_method, self.curve_improved_eulers_lte),
                   (runge_kutta_method, self.curve_runge_kutta_lte)]
        for (method, curve) in methods:
            curve.clear()
            if self.plots_enabled[method.check_box_name]:
                draw_plot(curve, method.calculate_lte_points())

    def fetch_values(self) -> GraphParameters:
        x0 = float(self.ui.x0_input.value())
        y0 = float(self.ui.y0_input.value())
        a = float(self.ui.a_input.value())
        b = float(self.ui.b_input.value())
        n = int(self.ui.pts_number_input.value())
        return GraphParameters(x0, y0, a, b, n)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
