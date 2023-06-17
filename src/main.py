import sys

from PyQt5.QtWidgets import QApplication

from components import AboutDialog, MainWindow
from model import ImagesList


class ImageViewerApp(QApplication):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == '__main__':
    app = ImageViewerApp(sys.argv)
    images = ImagesList()
    aboutDialog = AboutDialog()
    window = MainWindow(images, aboutDialog)
    window.show()
    app.exec()
