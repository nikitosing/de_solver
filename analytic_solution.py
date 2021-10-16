from graph_parameters import GraphParameters
from plot_calculator import PlotCalculator
import math


class AnalyticSolution(PlotCalculator):
    check_box_name = "Analytic solution"

    def __init__(self, graph_parameters: GraphParameters):
        super().__init__(graph_parameters)
        self.c = (self.graph_parameters.y0 + 2 * self.graph_parameters.x0 - 1) / math.exp(self.graph_parameters.x0)

    def calculate_function(self, x) -> float:
        return self.c * math.exp(x) - 2 * x + 1

    def calculate_plot_points(self) -> ([float], [float]):
        gp = self.graph_parameters
        current_x = gp.a
        x = []
        y = []
        step = abs(gp.b - gp.a) / gp.number_of_points
        if step == 0:
            return [], []
        while current_x <= gp.b:
            x.append(current_x)
            y.append(self.calculate_function(current_x))
            current_x += step
        return x, y

    def calculate_lte_points(self, x) -> ([float], [float]):
        pass

    def calculate_gte(self, x) -> float:
        pass

    def calculate_gte_points(self, x) -> ([float], [float]):
        pass
