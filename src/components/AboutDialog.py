from PyQt5.QtWidgets import QDialog

from .designer.Ui_AboutDialog import Ui_AboutDialog


class AboutDialog(QDialog):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
