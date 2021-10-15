from abc import ABC, abstractmethod

from graph_parameters import GraphParameters


class PlotCalculator(ABC):
    graph_parameters: GraphParameters = GraphParameters(1, 1, 0, 5, 5)

    def __init__(self, graph_parameters: GraphParameters):
        self.graph_parameters = graph_parameters

    @abstractmethod
    def calculate_plot_points(self) -> ([float], [float]):
        pass

    @abstractmethod
    def calculate_function(self, x) -> float:
        pass

    def f(self, x, y):
        return 2 * x + y - 3
