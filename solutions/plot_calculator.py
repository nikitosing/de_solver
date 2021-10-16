from abc import ABC, abstractmethod

from helpers.graph_parameters import GraphParameters


class PlotCalculator(ABC):
    def __init__(self, graph_parameters: GraphParameters):
        self.graph_parameters = graph_parameters

    @abstractmethod
    def calculate_plot_points(self) -> ([float], [float]):
        pass

    @abstractmethod
    def calculate_function(self, x) -> float:
        pass

    @abstractmethod
    def calculate_lte_points(self) -> ([float], [float]):
        pass

    @abstractmethod
    def calculate_lte(self, x) -> float:
        pass

    def calculate_gte_points(self) -> ([int], [float]):
        n_0 = self.graph_parameters.n_0
        n = self.graph_parameters.n

        n_list = []
        e = []
        for i in range(n_0, n + 1):
            n_list.append(i)
            self.graph_parameters.number_of_points = i
            e.append(max(self.calculate_lte_points()[1]))
        return n_list, e

    def f(self, x, y):
        return 2 * x + y - 3

    def calculate_step(self):
        self.step = abs(self.graph_parameters.b - self.graph_parameters.a) / self.graph_parameters.number_of_points
