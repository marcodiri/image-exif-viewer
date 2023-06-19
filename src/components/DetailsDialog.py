from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtCore import Qt

from .designer.Ui_DetailsDialog import Ui_DetailsDialog


class DetailsDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)

    def setDetails(self, details: dict):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(len(details))

        for i, (k, v) in enumerate(details.items()):
            tag = QTableWidgetItem(str(k))
            tag.setFlags(tag.flags() & ~Qt.ItemIsEditable)
            value = QTableWidgetItem(str(v))
            value.setFlags(value.flags() & ~Qt.ItemIsEditable)
            self.ui.tableWidget.setItem(i, 0, tag)
            self.ui.tableWidget.setItem(i, 1, value)
