class GraphParameters:
    x0: float = 1
    y0: float = 1
    a: float = 0
    b: float = 5
    number_of_points: int = 15

    def __init__(self, x0, y0, a, b, number_of_points):
        self.x0 = x0
        self.y0 = y0
        self.a = a
        self.b = b
        self.number_of_points = number_of_points
