import faulthandler
import json
import logging
import os
import sys

import qasync
from PySide6 import QtWidgets
from PySide6.QtWidgets import QAbstractItemView, QHeaderView, QAbstractScrollArea

from baseElements.baseThreading import BaseThread
from baseElements.historyDivTable import HistoryDivCompanyTable
from htmlParser.stockObject import StockObject
from mainWindow import Ui_MainWindow
import pyqtgraph as pg
from baseElements.companyTable import CompanyTable


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


def set_data_to_table(table_model, table_name, header, table_data):
    model = table_model(table_data, header)
    table_name.setModel(model)


def get_table_data_from_json(json_data):
    table_data = []
    try:
        for d in json_data['companies']:
            data_tmp = [d['company'], d['divLink']]
            table_data.append(data_tmp)

        return table_data
    except:
        return [["BRAK DANYCH"]]


def get_div_link_for_json(json_data, name):
    try:
        for d in json_data['companies']:
            if name == d['company']:
                return d['divLink']
        return 'NONE'
    except:
        return 'NONE'


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Stock Helper")
        self.mainContentStacked.setCurrentIndex(0)

        # Push button
        self.pushButton.clicked.connect(self.pushbutton_clicked)

        # Variable
        self.all_json_data = upload_data_from_file(r"config/config.json")

        # Setting for all_companies_table
        header = ["Lp"]
        data = get_table_data_from_json(self.all_json_data)
        set_data_to_table(CompanyTable, self.all_companies_table, header, data)
        self.all_companies_table.resizeColumnsToContents()
        self.all_companies_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.all_companies_table.doubleClicked.connect(self.all_companies_table_double_click)

    def all_companies_table_double_click(self, index):
        company_name = self.all_companies_table.model().index(index.row(), index.column()).data()

        header = ["Lp", "Spółka", "Sdadasda", "dsadsa", "sdadasd"]
        url_div = get_div_link_for_json(self.all_json_data, company_name)

        if url_div == 'NONE':
            table_data = [['BRAK', 'BRAK', 'BRAK', 'BRAK', 'BRAK']]
        else:
            stock_object = StockObject(company_name, url_div)
            table_data = stock_object.get_history_div()

        set_data_to_table(HistoryDivCompanyTable, self.divInfoTableView, header, table_data)
        self.divInfoTableView.resizeColumnsToContents()
        # self.divInfoTableView.setSelectionBehavior(QAbstractItemView.NoSelection)
        self.divInfoTableView.setSelectionMode(QAbstractItemView.NoSelection)
        self.divInfoTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.divInfoTableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        print(self.divInfoTableView.model().rowCount())
        #self.divInfoTableView.horizontalHeader().setStretchLastSection(True)
        self.mainContentStacked.setCurrentIndex(1)

    def pushbutton_clicked(self):
        thread = BaseThread(
            target=self.analize_all_companies
        )
        thread.start()

    def analize_all_companies(self):
        data = get_table_data_from_json(self.all_json_data)
        data_len = len(data)

        counter_progress_bar = 0
        for com, div_link in data:
            counter_progress_bar += 1
            self.label.setText(com)
            self.label_2.setText(f'{counter_progress_bar} / {data_len}')
            if div_link == 'NONE':
                table_data = 'NONE'
            else:
                stock_object = StockObject(com, div_link)
                table_data = stock_object.get_history_div()

            print(f'For company {com} div history is {table_data}')

    def closeEvent(self, event):  # Action to click right top exit button (os# _exit->closing all threads)
        print("Aplication was closed !!!")
        os._exit(0)
        event.accept()


def start_application():  # Start Application with qasync
    faulthandler.enable()
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    logging.info("Starting gui from application stockHelper...")
    with loop:
        loop.run_forever()
