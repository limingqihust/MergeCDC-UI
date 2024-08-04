import multi_tab    # 需要运行的.py文件名
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = multi_tab.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.terasort.clicked.connect(self.TeraSort)
        self.ui.coded_terasort.clicked.connect(self.CodedTeraSort)
        self.ui.tab_0_button.clicked.connect(self.Tab0PushButton)
        

    def Tab0PushButton(self):
        self.ui.tab_0_output.clear()
        msg = self.ui.tab_0_input.toPlainText()
        self.ui.tab_0_output.setText(msg)


    def TeraSort(self):
        self.ui.output.clear()
        msg = self.ui.input_file_distribution.toPlainText() + self.ui.input_node_distribution.toPlainText()
        self.ui.output.setText(msg)

    def CodedTeraSort(self):
        self.ui.output.clear()
        msg = self.ui.input_file_distribution.toPlainText() + self.ui.input_node_distribution.toPlainText()
        self.ui.output.setText(msg)


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



