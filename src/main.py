import sys

from PyQt5.QtWidgets import QApplication

from components import AboutDialog, DetailsDialog, MainWindow
from model import ImageList


class ImageViewerApp(QApplication):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == '__main__':
    app = ImageViewerApp(sys.argv)
    images = ImageList()
    aboutDialog = AboutDialog()
    detailsDialog = DetailsDialog()
    window = MainWindow(images, aboutDialog, detailsDialog)
    if __file__ in sys.argv:
        sys.argv.remove(__file__)
        if len(sys.argv) > 0:
            for arg in sys.argv:
                window.addImage(arg)
    window.show()
    app.exec()
