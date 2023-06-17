from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from components import AboutDialog

from .designer.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, aboutDialog: AboutDialog):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionAbout.triggered.connect(aboutDialog.exec_)
        self.ui.actionQuit.triggered.connect(QApplication.exit)
        self.ui.actionOpen.triggered.connect(self.get_image_files)
        
        self.ui.buttonForward.hide()
        self.ui.buttonBackward.hide()
        
        self.ui.statusbar.showMessage("No image opened")
    
    def get_image_files(self):
        file_names, _ = QFileDialog.getOpenFileNames(self, 'Open Images', r"", "Image files (*.jpg *.jpeg *.png *.gif)")
        print(file_names)
