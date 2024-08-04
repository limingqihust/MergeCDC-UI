import multi_tab    # 需要运行的.py文件名
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import config
import exec
TOTAL_NDOE_NUM = 32

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
        file_distribution = self.ui.input_file_distribution.toPlainText()
        node_distribution = self.ui.input_node_distribution.toPlainText()
        config_status = config.CheckConfig(TOTAL_NDOE_NUM, file_distribution, node_distribution)
        if config_status == config.ConfigStatus.FileDistributionError or config_status == config.ConfigStatus.NodeDistributionError:
            msg = f'文件分布/节点分布输入应当为{TOTAL_NDOE_NUM - 2}行'
            self.ui.output.setText(msg)
            return 
        if config_status == config.ConfigStatus.Success:
            config.UpdateConfig(TOTAL_NDOE_NUM, file_distribution, node_distribution)
        msg = exec.Exec(exec.JobType.TeraSort)
        data = config.ParseData(msg)
        self.SetTable(data)
        self.ui.output.setText(msg)

    def CodedTeraSort(self):
        self.ui.output.clear()
        file_distribution = self.ui.input_file_distribution.toPlainText()
        node_distribution = self.ui.input_node_distribution.toPlainText()
        config_status = config.CheckConfig(TOTAL_NDOE_NUM, file_distribution, node_distribution)
        if config_status == config.ConfigStatus.FileDistributionError or config_status == config.ConfigStatus.NodeDistributionError:
            msg = f'文件分布/节点分布输入应当为{TOTAL_NDOE_NUM - 2}行'
            self.ui.output.setText(msg)
            return 
        if config_status == config.ConfigStatus.Success:
            config.UpdateConfig(TOTAL_NDOE_NUM, file_distribution, node_distribution)
        msg = exec.Exec(exec.JobType.CodedTeraSort)
        data = config.ParseData(msg)
        self.SetTable(data)
        self.ui.output.setText(msg)

    def SetTable(self, data):
        self.ui.table.setColumnCount(2)
        self.ui.table.setHorizontalHeaderLabels(['Avg', 'Max'])
        if len(data) == 4:
            self.ui.table.setRowCount(4)
            self.ui.table.setVerticalHeaderLabels(['MAP', 'SHUFFLE', 'UNPACK', 'REDUCE'])
            for i in range(len(data)):
                for j in range(2):
                    self.ui.table.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j + 1]))
        else:
            self.ui.table.setRowCount(9)
            self.ui.table.setVerticalHeaderLabels(['CODEGEN', 'MAP', 'INNERTRANS', 'ENCODE', 'SHUFFLE', 'SHUFFLE(P2P)', 'SHUFFLE(MULTI)', 'DECODE', 'REDUCE'])
            for i in range(len(data)):
                for j in range(2):
                    self.ui.table.setItem(i, j, QtWidgets.QTableWidgetItem(data[i][j + 1]))
        self.ui.table.update()


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



