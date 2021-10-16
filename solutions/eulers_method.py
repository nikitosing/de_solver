from solutions.analytic_solution import AnalyticSolution
from helpers.graph_parameters import GraphParameters
from solutions.plot_calculator import PlotCalculator


class EulersMethod(PlotCalculator):
    check_box_name = "Euler's method (green)"

    def __init__(self, graph_parameters: GraphParameters):
        self.y_last = graph_parameters.y0
        self.first_calculating = True
        self.step = abs(graph_parameters.b - graph_parameters.a) / graph_parameters.number_of_points
        self.analytic_solution = AnalyticSolution(graph_parameters)
        super().__init__(graph_parameters)

    def calculate_plot_points(self) -> ([float], [float]):
        self.first_calculating = True
        gp = self.graph_parameters
        self.y_last = gp.y0
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
        if self.first_calculating:
            self.first_calculating = False
            return self.y_last
        to_return = self.y_last + self.step * (2 * x + self.y_last - 3)
        self.y_last = to_return
        return to_return

    def calculate_lte_points(self) -> ([float], [float]):
        self.first_calculating = True
        gp = self.graph_parameters
        self.y_last = gp.y0
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

    def calculate_gte(self, x) -> float:
        pass

    def calculate_gte_points(self) -> ([float], [float]):
        pass
