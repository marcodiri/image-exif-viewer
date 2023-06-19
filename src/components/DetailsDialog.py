from PyQt5.QtWidgets import QDialog

from .designer.Ui_DetailsDialog import Ui_DetailsDialog


class DetailsDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)
