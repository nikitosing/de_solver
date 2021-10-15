from graph_parameters import GraphParameters
from plot_calculator import PlotCalculator


class ImprovedEulersMethod(PlotCalculator):
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
        to_return = self.y_last + 0.5 * self.step * (self.f(self.x_last, self.y_last) + self.f(x,
                                                                                               self.y_last + self.f(
                                                                                                   self.x_last,
                                                                                                   self.y_last)))
        self.y_last = to_return
        self.x_last = x
        return to_return

    def f(self, x, y):
        return 2 * x + y - 3
