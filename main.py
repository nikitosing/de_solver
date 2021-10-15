from PyQt5 import QtWidgets
from main_window import Ui_MainWindow
import sys
import numpy as np
import pyqtgraph as pg
from colors import *
from graphics_config import init


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        init()

        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.curve = self.ui.graphicsView.plot(name="Line", pen=pg.mkPen(color=black, width=2))

        self.random_plot()

    def random_plot(self):
        random_array = np.random.random_sample(20)
        self.curve.setData([0.07348005, 0.80929058, 0.73979838, 0.64437829, 0.88681979,
                            0.39149684, 0.33953551, 0.89475804, 0.06234156, 0.4569001,
                            0.64637681, 0.70805449, 0.82971517, 0.16630447, 0.44577314,
                            0.08118012, 0.90280082, 0.0334852, 0.50733612, 0.65677828])


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
