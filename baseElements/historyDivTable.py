from PySide6 import QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor


class HistoryDivCompanyTable(QtCore.QAbstractTableModel):
    def __init__(self, data, header):
        super(HistoryDivCompanyTable, self).__init__()
        self._display_data = data
        self._header = header

    def headerData(self, col, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._header[col]
        return None

    def data(self, index=0, role=None):
        if role == Qt.DisplayRole:
            return self._display_data[index.row()][index.column()]

        if role == Qt.BackgroundRole:
            return QColor(Qt.white)

        if role == Qt.ForegroundRole:
            return QColor(Qt.black)

    def rowCount(self, index=1):
        return len(self._display_data)

    def columnCount(self, index=1):
        return len(self._display_data[0])

