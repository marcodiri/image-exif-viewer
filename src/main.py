import sys

from PyQt5.QtWidgets import QApplication

from components import MainWindow, AboutDialog


class ImageViewerApp(QApplication):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == '__main__':
    app = ImageViewerApp(sys.argv)
    aboutDialog = AboutDialog()
    window = MainWindow(aboutDialog)
    window.show()
    app.exec()
