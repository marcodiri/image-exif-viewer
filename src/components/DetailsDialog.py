from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from .designer.Ui_DetailsDialog import Ui_DetailsDialog


class DetailsDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)
        
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(5)

    def addCategory(self, value):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(rowCount+1)
        value = QTableWidgetItem(str(value))
        value.setFont(QFont("Sans Serif", 10, QFont.Bold))
        value.setFlags(value.flags() & ~Qt.ItemIsEditable &
                       ~Qt.ItemIsSelectable)
        empty = QTableWidgetItem()
        empty.setFlags(value.flags() & ~Qt.ItemIsEditable &
                       ~Qt.ItemIsSelectable)
        self.ui.tableWidget.setItem(rowCount, 0, value)
        self.ui.tableWidget.setItem(rowCount, 1, empty)

    def addDetail(self, key, val):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(rowCount+1)
        tag = QTableWidgetItem(" "*4+str(key))
        tag.setToolTip(str(key))
        tag.setFlags(tag.flags() & ~Qt.ItemIsEditable)
        value = QTableWidgetItem(str(val))
        value.setToolTip(str(val))
        value.setFlags(value.flags() & ~Qt.ItemIsEditable)
        self.ui.tableWidget.setItem(rowCount, 0, tag)
        self.ui.tableWidget.setItem(rowCount, 1, value)

    def setDetails(self, details: dict):
        self.clearDetails()

        self.formatted = {}

        for k, v in details.items():
            if k in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                continue
            cat, newTag = str(k).split(" ", 1)
            if cat not in self.formatted:
                self.formatted[cat] = {}
                self.addCategory(cat)
                if cat == "GPS":
                    # format GPS records
                    if 'GPS GPSLatitude' in details and 'GPS GPSLongitude' in details:
                        latD, latM, latS = details['GPS GPSLatitude'].values
                        latRef = details['GPS GPSLatitudeRef'].values
                        lonD, lonM, lonS = details['GPS GPSLongitude'].values
                        lonRef = details['GPS GPSLongitudeRef'].values
                        gpsString = f"{latD}°{latM}'{float(latS)}\"{latRef}+{lonD}°{lonM}'{float(lonS)}\"{lonRef}"
                        self.addDetail("GPSString", gpsString)

            self.formatted[cat][newTag] = v
            self.addDetail(newTag, v)

    def clearDetails(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
