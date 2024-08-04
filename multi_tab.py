# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multi_tab.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 771, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab0 = QtWidgets.QWidget()
        self.tab0.setObjectName("tab0")
        self.frame = QtWidgets.QFrame(self.tab0)
        self.frame.setGeometry(QtCore.QRect(0, 10, 771, 501))
        self.frame.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_file_distribution = QtWidgets.QLabel(self.frame)
        self.label_file_distribution.setGeometry(QtCore.QRect(20, 20, 101, 17))
        self.label_file_distribution.setObjectName("label_file_distribution")
        self.label_node_distribution = QtWidgets.QLabel(self.frame)
        self.label_node_distribution.setGeometry(QtCore.QRect(20, 60, 121, 17))
        self.label_node_distribution.setObjectName("label_node_distribution")
        self.input_file_distribution = QtWidgets.QTextEdit(self.frame)
        self.input_file_distribution.setGeometry(QtCore.QRect(160, 10, 161, 31))
        self.input_file_distribution.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.input_file_distribution.setObjectName("input_file_distribution")
        self.input_node_distribution = QtWidgets.QTextEdit(self.frame)
        self.input_node_distribution.setGeometry(QtCore.QRect(160, 50, 161, 31))
        self.input_node_distribution.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.input_node_distribution.setObjectName("input_node_distribution")
        self.print_info = QtWidgets.QPushButton(self.frame)
        self.print_info.setGeometry(QtCore.QRect(120, 100, 89, 25))
        self.print_info.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.print_info.setObjectName("print_info")
        self.output = QtWidgets.QTextBrowser(self.frame)
        self.output.setGeometry(QtCore.QRect(120, 200, 256, 192))
        self.output.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.output.setObjectName("output")
        self.tabWidget.addTab(self.tab0, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.frame_2 = QtWidgets.QFrame(self.tab1)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 771, 501))
        self.frame_2.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.frame_3 = QtWidgets.QFrame(self.tab2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 771, 501))
        self.frame_3.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tabWidget.addTab(self.tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_file_distribution.setText(_translate("MainWindow", "文件分布情况："))
        self.label_node_distribution.setText(_translate("MainWindow", "节点分布情况："))
        self.print_info.setText(_translate("MainWindow", "PrintInfo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab0), _translate("MainWindow", "标签0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "标签1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "标签2"))
