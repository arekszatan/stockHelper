import json
import logging
import sys
import qasync
from PySide6 import QtWidgets
from mainWindow import Ui_MainWindow
import pyqtgraph as pg


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Stock Helper")
        #self.graphWidget = pg.PlotWidget()
        #self.setCentralWidget(self.graphWidget)
        #self.horizontalLayout_2.addWidget(self.graphWidget)

        #hour = [-2,-1,0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #temperature = [23,23,23,30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        f = open(r"config/config.json", "r", encoding="utf-8")
        self.data = json.load(f)
        f.close()
        data = []
        a = 0
        #print(self.data['companies'])
        for i in self.data['companies']:
            print(i['company'])
            data_tmp = []
            data_tmp.append(a)
            data_tmp.append(i['company'])
            a += 1
            data.append(data_tmp)
        # plot data: x, y values
        #self.graphWidget.plot(hour, temperature)
        # data = [
        #     [4, 9, 2],
        #     [1, 0, 0],
        #     [3, 5, 0],
        #     [3, 3, 2],
        #     [7, 8, 9],
        # ]
        header = ["dsadas", "Dsadasd", "Sdadasda"]
        from baseElements.baseTable import TableModel
        self.model = TableModel(data, header)
        self.tableView.setModel(self.model)


def start_application():  # Start Application with qasync
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    logging.info("Starting gui from application stockHelper...")
    with loop:
        loop.run_forever()
