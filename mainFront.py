import json
import logging
import sys
import qasync
from PySide6 import QtWidgets

from htmlParser.divParser import StockObject
from mainWindow import Ui_MainWindow
import pyqtgraph as pg
from baseElements.baseTable import TableModel


def upload_data_from_file(path):
    try:
        file = open(path, "r", encoding="utf-8")
        file_data_loaded = json.load(file)
        file.close()
        logging.info(f'File {path} was opened.')
        return file_data_loaded
    except FileNotFoundError:
        logging.exception(f'File {path} not found')
        return []


def download_data_from_file(path):
    ...


def set_data_to_table(table_name, header, data):
    a = 0
    table_data = []

    for d in data['companies']:
        data_tmp = [d['company']]
        a += 1
        table_data.append(data_tmp)

    test = StockObject("Handlowy", "https://strefainwestorow.pl/notowania/gpw/handlowy-bhw/dywidendy")
    model = TableModel(test.get_history_div(), header)
    table_name.setModel(model)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Stock Helper")

        # Variable
        self.all_json_data = upload_data_from_file(r"config/config.json")

        # Setting for all_companies_table
        header = ["Lp", "Spółka", "Sdadasda", "dsadsa", "sdadasd"]
        set_data_to_table(self.all_companies_table, header, self.all_json_data)
        self.all_companies_table.resizeColumnsToContents()
        self.all_companies_table.doubleClicked.connect(self.all_companies_table_double_click)

    def all_companies_table_double_click(self, index):
        print(self.all_companies_table.model().index(index.row(), index.column()).data())
        self.mainContentStacked.setCurrentIndex(1)


def start_application():  # Start Application with qasync
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    logging.info("Starting gui from application stockHelper...")
    with loop:
        loop.run_forever()
