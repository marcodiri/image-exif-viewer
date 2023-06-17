from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from components import AboutDialog
from model import ImagesList

from .designer.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, images: ImagesList, aboutDialog: AboutDialog):
        super().__init__()
        
        self._images = images
        self._images.idxChanged.connect(self.showImage)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.actionAbout.triggered.connect(aboutDialog.exec_)
        self.ui.actionQuit.triggered.connect(QApplication.exit)
        self.ui.actionOpen.triggered.connect(self.getImageFiles)
        
        self.ui.buttonForward.hide()
        self.ui.buttonBackward.hide()
        
        self.ui.statusbar.showMessage("No image opened")

    def getImageFiles(self):
        fileNames, _ = QFileDialog.getOpenFileNames(self, 'Open Images', r"", "Image files (*.jpg *.jpeg *.png *.gif)")
        for file in fileNames:
            self._images.addImage(QPixmap(file))
            
    def showImage(self, idx: int):
        image = self._images.getImage(idx)
        w, h = image.width(), image.height()
        if w > 512 or h > 512:
            image = image.scaled(512, 512, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.ui.labelImage.setPixmap(image)
        self.resize(self.layout().sizeHint())
    