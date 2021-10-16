from solutions.analytic_solution import AnalyticSolution
from helpers.graph_parameters import GraphParameters
from solutions.plot_calculator import PlotCalculator


class RungeKuttaMethod(PlotCalculator):
    check_box_name = "Runge-Kutta method (blue)"

    def __init__(self, graph_parameters: GraphParameters):
        super().__init__(graph_parameters)
        self.y_last = graph_parameters.y0
        self.x_last = graph_parameters.y0
        self.first_calculating = True
        self.analytic_solution = AnalyticSolution(graph_parameters)
        self.calculate_step()

    def calculate_plot_points(self) -> ([float], [float]):
        gp = self.graph_parameters
        self.y_last = gp.y0
        self.x_last = gp.x0
        current_x = gp.x0
        x = []
        y = []

        if self.step == 0:
            return [], []
        while current_x <= gp.b:
            x.append(current_x)
            y.append(self.calculate_function(current_x))
            current_x += self.step
        return x, y

    def calculate_function(self, x) -> float:
        k1 = self.step * self.f(self.x_last, self.y_last)
        k2 = self.step * self.f(self.x_last + self.step * 0.5, self.y_last + 0.5 * k1)
        k3 = self.step * self.f(self.x_last + self.step * 0.5, self.y_last + 0.5 * k2)
        k4 = self.step * self.f(self.x_last + self.step, self.y_last + k3)
        to_return = self.y_last + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        self.y_last = to_return
        self.x_last = x
        return to_return

    def calculate_lte_points(self) -> ([float], [float]):
        self.calculate_step()
        self.first_calculating = True
        gp = self.graph_parameters
        self.y_last = gp.y0
        self.x_last = gp.x0
        current_x = gp.x0
        x = []
        e = []

        if self.step == 0:
            return [], []
        while current_x <= gp.b:
            x.append(current_x)
            e.append(self.calculate_lte(current_x))
            current_x += self.step
        return x, e

    def calculate_lte(self, x) -> float:
        return abs(self.calculate_function(x) - self.analytic_solution.calculate_function(x))
