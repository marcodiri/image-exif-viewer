from PyQt5.QtCore import QSize, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from components import AboutDialog
from model import Image, ImageList

from .designer.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    resized = pyqtSignal(QSize)

    def __init__(
        self,
        images: ImageList,
        aboutDialog: AboutDialog,
        maxImgInitialSize: int = 512
    ):
        super().__init__()
        self.imgMarginRight = 20
        self._imgMarginBottom = 60
        self.maxImgInitialSize = maxImgInitialSize

        self._aspectRatio = None

        self._images = images
        self._images.idxChanged.connect(self.showImage)
        self._images.imagesChanged.connect(self.updateUi)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionAbout.triggered.connect(aboutDialog.exec_)
        self.ui.actionQuit.triggered.connect(QApplication.exit)
        self.ui.actionOpen.triggered.connect(self.getImageFiles)

        self.ui.buttonForward.hide()
        self.ui.buttonBackward.hide()
        self.ui.buttonForward.clicked.connect(self._images.next)
        self.ui.buttonBackward.clicked.connect(self._images.prev)

        self.ui.statusbar.showMessage("No image opened")

        self.resized.connect(self.onResize)
    
    @property
    def imgMarginBottom(self):
        if len(self._images) > 1:
            return self._imgMarginBottom + self.ui.navButtonsLayout.sizeHint().height() + 4
        return self._imgMarginBottom

    @imgMarginBottom.setter
    def imgMarginBottom(self, value):
        self._imgMarginBottom = value

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
            self._images.addImage(Image(file))
    
    def updateUi(self, numImages: int):
        if numImages > 0:
            self.ui.menuImage.setEnabled(True)
        if numImages > 1:
            self.ui.buttonForward.show()
            self.ui.buttonBackward.show()

    def showImage(self, idx: int):
        pixmap = QPixmap(self._images.getImage(idx).path)
        w, h = pixmap.width(), pixmap.height()
        self._aspectRatio = w / h

        # resize image to maxImgInitialSize
        if w >= h and w > self.maxImgInitialSize:
            self.ui.labelImage.resize(self.maxImgInitialSize, int(
                self.maxImgInitialSize/self._aspectRatio))
        elif w < h and h > self.maxImgInitialSize:
            self.ui.labelImage.resize(
                int(self.maxImgInitialSize*self._aspectRatio), self.maxImgInitialSize)
        else:
            self.ui.labelImage.resize(pixmap.size())

        self.ui.labelImage.setPixmap(pixmap)
        self.resize(self.ui.labelImage.width()+self.imgMarginRight,
                    self.ui.labelImage.height()+self.imgMarginBottom)

        self.ui.statusbar.showMessage(f"{idx+1}/{len(self._images)} - {self._images.getImage(idx).path}")
    