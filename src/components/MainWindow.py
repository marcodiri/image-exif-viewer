from typing import List

from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtGui import QKeySequence, QTransform
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QShortcut

from components import AboutDialog, DetailsDialog
from model import Image, ImageList

from .designer.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    resized = pyqtSignal(QSize)

    def __init__(
        self,
        images: ImageList,
        aboutDialog: AboutDialog,
        detailsDialog: DetailsDialog,
        maxImgInitialSize: int = 512
    ):
        super().__init__()
        self._aboutDialog = aboutDialog
        self._detailsDialog = detailsDialog

        self.imgMarginRight = 20
        self.imgMarginBottom = 60
        self.maxImgInitialSize = maxImgInitialSize

        self._aspectRatio = None

        self._images = images
        self._images.idxChanged.connect(self.showImage)
        self._images.imagesChanged.connect(self.updateUi)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionAbout.triggered.connect(aboutDialog.exec_)
        self.ui.actionDetails.triggered.connect(self.showImageDetails)
        self.ui.actionQuit.triggered.connect(QApplication.exit)
        self.ui.actionOpen.triggered.connect(self.getImageFiles)
        self.ui.actionRotate_90.triggered.connect(lambda: self.rotateImage(90))
        self.ui.actionRotate_m90.triggered.connect(
            lambda: self.rotateImage(-90))
        self.resized.connect(self.onResize)

        # command shortcuts
        self.ui.actionOpen.setShortcut(QKeySequence("Ctrl+O"))
        self.ui.actionRotate_90.setShortcut(QKeySequence("R"))
        self.ui.actionRotate_m90.setShortcut(QKeySequence("Ctrl+R"))
        QShortcut(QKeySequence("Right"), self).activated.connect(
            self._images.next)
        QShortcut(QKeySequence("Left"), self).activated.connect(
            self._images.prev)

        self.ui.statusbar.showMessage("No image opened")

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

    def addImages(self, paths: List[str]):
        images = []
        for path in paths:
            extension = path.split(".")[-1]
            if extension not in ["jpg", "jpeg", "png", "tiff", "webp"]:
                raise ValueError("File type not supported")
            images.append(Image(path))
        self._images.addImages(images)

    def getImageFiles(self):
        fileNames, _ = QFileDialog.getOpenFileNames(
            self, 'Open Images', r"",
            "Image files (*.jpg *.jpeg *.png *.tiff *.webp)"
        )
        self.addImages(fileNames)

    def updateUi(self, numImages: int):
        if numImages > 0:
            self.ui.menuImage.setEnabled(True)

    def showImage(self, idx: int):
        pixmap = self._images.getImage(idx).pixmap
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

        self.ui.statusbar.showMessage(
            f"{idx+1}/{len(self._images)} - {self._images.getImage(idx).path}")

    def showImageDetails(self):
        currentIdx = self._images.currentIdx
        self._detailsDialog.setDetails(
            self._images.getImage(currentIdx).metadata)
        self._detailsDialog.exec_()

    def rotateImage(self, angle: float):
        currentIdx = self._images.currentIdx
        if currentIdx is not None:
            currentImage = self._images.getImage(currentIdx)
            if currentImage.transform is None:
                currentImage.transform = QTransform().rotate(angle)
            else:
                currentImage.transform.rotate(angle)
            self.showImage(currentIdx)
