import multi_tab    # 需要运行的.py文件名
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets


def PrintInfo():
    print("hello world")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = multi_tab.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.print_info.clicked.connect(PrintInfo)


if __name__ == '__main__':
    app = QApplication(sys.argv)    # 创建应用程序
    # mainwindow = QMainWindow()      # 创建主窗口
    # ui = multi_tab.Ui_MainWindow()      # 调用中的主窗口
    # ui.setupUi(mainwindow)          # 向主窗口添加控件
    # ui.print_info.clicked.connect(PrintInfo)
    # mainwindow.show()               # 显示窗口

    mainwindow = MainWindow()       # 调用中的主窗口
    mainwindow.show()
    sys.exit(app.exec_())           # 程序执行循环



