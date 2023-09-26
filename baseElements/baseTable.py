from typing import Any

import PySide6
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QBrush


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, header):
        super(TableModel, self).__init__()
        self._data = data
        self._header = header

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._header[col]
        return None

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

        if role == Qt.BackgroundRole:
            return QBrush(QColor(Qt.red))

        if role == Qt.ForegroundRole:
            return QColor(Qt.blue)

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
