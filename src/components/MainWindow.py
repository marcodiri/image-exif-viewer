from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QSizePolicy

from components import AboutDialog
from model import ImagesList

from .designer.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    resized = pyqtSignal(QSize)

    def __init__(
        self,
        images: ImagesList,
        aboutDialog: AboutDialog,
        maxImgInitialSize: int = 512
    ):
        super().__init__()
        self.imgMarginRight = 40
        self.imgMarginBottom = 105
        self.maxImgInitialSize = maxImgInitialSize

        self._aspectRatio = None

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

        self.resized.connect(self.onResize)

    def resizeEvent(self, event):
        self.resized.emit(self.size())
        return super().resizeEvent(event)

    def onResize(self, newSize: QSize):
        if self._aspectRatio is not None:
            w, h = newSize.width(), newSize.height()
            
            # resize image with window maintaining aspect ratio
            newImgHeight = int((h-self.imgMarginBottom)*self._aspectRatio)
            newImgWidth = int((w-self.imgMarginRight)/self._aspectRatio)
            if w >= h:
                if newImgHeight < w-self.imgMarginRight:
                    self.ui.labelImage.resize(
                        newImgHeight, h-self.imgMarginBottom)
                else:
                    self.ui.labelImage.resize(
                        w-self.imgMarginRight, newImgWidth)
            else:
                if newImgWidth < h-self.imgMarginBottom:
                    self.ui.labelImage.resize(
                        w-self.imgMarginRight, newImgWidth)
                else:
                    self.ui.labelImage.resize(
                        newImgHeight, h-self.imgMarginBottom)

    def getImageFiles(self):
        fileNames, _ = QFileDialog.getOpenFileNames(
            self, 'Open Images', r"", "Image files (*.jpg *.jpeg *.png *.gif)")
        for file in fileNames:
            self._images.addImage(QPixmap(file))

    def showImage(self, idx: int):
        image = self._images.getImage(idx)
        w, h = image.width(), image.height()
        self._aspectRatio = w / h
        
        # resize image to maxImgInitialSize
        if w >= h and w > self.maxImgInitialSize:
            self.ui.labelImage.resize(self.maxImgInitialSize, int(
                self.maxImgInitialSize/self._aspectRatio))
        elif w < h and h > self.maxImgInitialSize:
            self.ui.labelImage.resize(
                int(self.maxImgInitialSize*self._aspectRatio), self.maxImgInitialSize)
        else:
            self.ui.labelImage.resize(image.size())

        self.ui.labelImage.setPixmap(image)
        self.resize(self.ui.labelImage.width()+self.imgMarginRight,
                    self.ui.labelImage.height()+self.imgMarginBottom)
        
        self.ui.statusbar.showMessage(f"{idx+1}/{len(self._images)}")
