import webbrowser
from typing import Optional

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from .designer.Ui_DetailsDialog import Ui_DetailsDialog


class DetailsDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)

        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(5)
        self.ui.tableWidget.itemClicked.connect(self.itemClicked)

    def itemClicked(self, event: QTableWidgetItem):
        clickedTag = self.ui.tableWidget.item(event.row(), 0).text().strip()
        if clickedTag == "GPSString":
            webbrowser.open(
                f"https://www.google.com/maps/place/{event.text()}", new=2)

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

    def addDetail(
        self,
        key: str,
        value: str,
        valueTooltip: Optional[str] = None,
        valueFont: Optional[QFont] = None,
        valueColor: Optional[QColor] = None
    ):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(rowCount+1)
        tag = QTableWidgetItem(" "*4+key)
        tag.setToolTip(key)
        tag.setFlags(tag.flags() & ~Qt.ItemIsEditable)
        val = QTableWidgetItem(value)
        if valueTooltip is not None:
            val.setToolTip(valueTooltip)
        if valueFont is not None:
            val.setFont(valueFont)
        if valueColor is not None:
            val.setForeground(valueColor)
        val.setFlags(val.flags() & ~Qt.ItemIsEditable)
        self.ui.tableWidget.setItem(rowCount, 0, tag)
        self.ui.tableWidget.setItem(rowCount, 1, val)

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
                        linkFont = QFont("Sans Serif")
                        linkFont.setUnderline(True)
                        self.addDetail("GPSString", gpsString,
                                       "Open in Google Maps",
                                       linkFont,
                                       QColor(6, 69, 173))

            self.formatted[cat][newTag] = v
            self.addDetail(newTag, str(v), str(v))

    def clearDetails(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
