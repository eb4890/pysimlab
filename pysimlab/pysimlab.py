
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex

from PyQt5.QtGui import QColor


import numpy as np


class NdaArrayTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.nda_data = data
        shape = data.shape
        if len(shape) == 2:
            x,y = shape
            self.column_count = x
            self.row_count =  y
        if len(shape) ==1 :
            x, = shape
            self.column_count =  x
            self.row_count =  1

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            return "{}".format(self.nda_data[row][column])
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None




class PySimLab (QApplication):
    def __init__(self, argv):
        super().__init__(argv)


class NdarrayGrid(QTableView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

if __name__== "__main__":
    app = PySimLab(sys.argv)
    model = NdaArrayTableModel(np.zeros((10,10)))
    window = NdarrayGrid()
    window.setModel(model)
    window.setWindowTitle("PySimLab")
    window.setGeometry(100,100,280, 80)
    window.move(60,15)
    window.show()
    sys.exit(app.exec_())
