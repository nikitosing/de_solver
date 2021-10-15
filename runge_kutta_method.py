from graph_parameters import GraphParameters
from plot_calculator import PlotCalculator


class RungeKuttaMethod(PlotCalculator):
    def __init__(self, graph_parameters: GraphParameters):
        self.y_last = graph_parameters.y0
        self.x_last = graph_parameters.y0
        self.first_calculating = True
        self.step = abs(graph_parameters.b - graph_parameters.a) / graph_parameters.number_of_points
        super().__init__(graph_parameters)

    def calculate_plot_points(self) -> ([float], [float]):
        gp = self.graph_parameters
        self.y_last = gp.y0
        self.x_last = gp.y0
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