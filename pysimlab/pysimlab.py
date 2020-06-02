
import sys

from typing import Any

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex

from PyQt5.QtGui import QColor


import numpy as np


class NdArrayTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        shape = data.shape
        if len(shape) ==1 :
            x, = shape
            data = data.reshape((x,1))
        x,y = data.shape
        self.nda_data = data
        self.column_count =  y
        self.row_count =  x

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        else:
            return "{}".format(section)

    def data(self, index: QModelIndex, role: Qt.ItemDataRole =Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            return "{}".format(self.nda_data[row][column])
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None

    def flags(self, index: QModelIndex):
        return QAbstractTableModel.flags(self, index) | Qt.ItemIsEditable

    def setData(self, index: QModelIndex, value: Any,
                role: Qt.ItemDataRole = Qt.DisplayRole) -> bool:
        if role==Qt.EditRole:
            self.nda_data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        else:
            return False


class PySimLab (QApplication):
    def __init__(self, argv):
        super().__init__(argv)


class NdArrayGrid(QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

if __name__== "__main__":
    app = PySimLab(sys.argv)
    model = NdArrayTableModel(np.zeros((10)))
    window = NdArrayGrid()
    window.setModel(model)
    window.setWindowTitle("PySimLab")
    window.setGeometry(100,100,280, 80)
    window.move(60,15)
    window.show()
    sys.exit(app.exec_())
