# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1164, 837)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(310, 160, 841, 621))
        self.graphicsView.setObjectName("graphicsView")
        self.plotButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotButton.setGeometry(QtCore.QRect(100, 320, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plotButton.setFont(font)
        self.plotButton.setObjectName("plotButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 410, 144, 88))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.euler_check_box = QtWidgets.QCheckBox(self.widget)
        self.euler_check_box.setObjectName("euler_check_box")
        self.gridLayout_5.addWidget(self.euler_check_box, 1, 0, 1, 1)
        self.improved_euler_check_box = QtWidgets.QCheckBox(self.widget)
        self.improved_euler_check_box.setObjectName("improved_euler_check_box")
        self.gridLayout_5.addWidget(self.improved_euler_check_box, 2, 0, 1, 1)
        self.runge_kutta_check_box = QtWidgets.QCheckBox(self.widget)
        self.runge_kutta_check_box.setObjectName("runge_kutta_check_box")
        self.gridLayout_5.addWidget(self.runge_kutta_check_box, 3, 0, 1, 1)
        self.analytic_check_box = QtWidgets.QCheckBox(self.widget)
        self.analytic_check_box.setObjectName("analytic_check_box")
        self.gridLayout_5.addWidget(self.analytic_check_box, 0, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(13, 22, 253, 154))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.y0_input = QtWidgets.QDoubleSpinBox(self.widget1)
        self.y0_input.setDecimals(5)
        self.y0_input.setMinimum(-1000000.0)
        self.y0_input.setSingleStep(1e-05)
        self.y0_input.setProperty("value", 1.0)
        self.y0_input.setObjectName("y0_input")
        self.gridLayout.addWidget(self.y0_input, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.x0_input = QtWidgets.QDoubleSpinBox(self.widget1)
        self.x0_input.setDecimals(5)
        self.x0_input.setMinimum(-1000000.0)
        self.x0_input.setMaximum(1000000.0)
        self.x0_input.setSingleStep(1e-05)
        self.x0_input.setProperty("value", 1.0)
        self.x0_input.setObjectName("x0_input")
        self.gridLayout.addWidget(self.x0_input, 1, 1, 1, 1)
        self.a_input = QtWidgets.QDoubleSpinBox(self.widget1)
        self.a_input.setMinimum(-1000.0)
        self.a_input.setMaximum(999.0)
        self.a_input.setSingleStep(0.1)
        self.a_input.setProperty("value", -3.5)
        self.a_input.setObjectName("a_input")
        self.gridLayout.addWidget(self.a_input, 2, 1, 1, 1)
        self.b_input = QtWidgets.QDoubleSpinBox(self.widget1)
        self.b_input.setMinimum(-999.0)
        self.b_input.setMaximum(1000.0)
        self.b_input.setSingleStep(0.1)
        self.b_input.setProperty("value", 3.5)
        self.b_input.setObjectName("b_input")
        self.gridLayout.addWidget(self.b_input, 3, 1, 2, 1)
        self.pts_number_input = QtWidgets.QSpinBox(self.widget1)
        self.pts_number_input.setMaximum(100000)
        self.pts_number_input.setProperty("value", 100)
        self.pts_number_input.setObjectName("pts_number_input")
        self.gridLayout.addWidget(self.pts_number_input, 5, 1, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 2, 1)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1164, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
        self.euler_check_box.setText(_translate("MainWindow", "Euler\'s method"))
        self.improved_euler_check_box.setText(_translate("MainWindow", "Improved Euler\'s method"))
        self.runge_kutta_check_box.setText(_translate("MainWindow", "Runge-Kutta method"))
        self.analytic_check_box.setText(_translate("MainWindow", "Analytic solution"))
        self.label_2.setText(_translate("MainWindow", "Y₀"))
        self.label.setText(_translate("MainWindow", "X₀"))
        self.label_3.setText(_translate("MainWindow", "a"))
        self.label_5.setText(_translate("MainWindow", "number of points"))
        self.label_4.setText(_translate("MainWindow", "b"))
from pyqtgraph import PlotWidget
