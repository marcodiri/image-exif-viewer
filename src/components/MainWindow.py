from PyQt5.QtWidgets import QApplication, QMainWindow

from components import AboutDialog

from .designer.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, aboutDialog: AboutDialog):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionAbout.triggered.connect(aboutDialog.exec_)
        self.ui.actionQuit.triggered.connect(QApplication.exit)
