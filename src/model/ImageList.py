from typing import List

from PyQt5.QtCore import QObject, pyqtSignal

from model import Image


class ImageList(QObject):
    _images: List[Image] = []
    _idx: int = -1

    imagesChanged = pyqtSignal(int)
    idxChanged = pyqtSignal(int)

    def __len__(self):
        return len(self._images)

    @property
    def currentIdx(self):
        """Returns the index of the current image.
        """
        return self._idx if len(self) else None

    @currentIdx.setter
    def currentIdx(self, newIdx):
        if newIdx > len(self)-1 or newIdx < 0:
            raise ValueError("New index is out of range")
        self._idx = newIdx
        self.idxChanged.emit(self._idx)

    def getImage(self, idx: int):
        """Get image at the specified index.

        Args:
            idx (int): index of the image in the list.

        Returns:
            Image: image at idx.
        """
        if idx > len(self)-1 or idx < 0:
            raise ValueError("Index is out of range")
        return self._images[idx]

    def addImage(self, img: Image):
        """Add an image to the list.

        Args:
            img (Image)
        """
        self._images.append(img)
        self.currentIdx = len(self)-1
        self.imagesChanged.emit(len(self))

    def clear(self):
        self._images.clear()
        self.currentIdx = -1
        self.imagesChanged.emit(len(self))

    def next(self):
        """Advance to next image or loops to first
        if currently on the last image.
        """
        currentIdx = self.currentIdx
        if currentIdx is None:
            return None
        currentIdx = (currentIdx+1) % len(self)
        self.currentIdx = currentIdx
        return currentIdx

    def prev(self):
        """Goes back to previous image or loops to last
        if currently on the first image.
        """
        currentIdx = self.currentIdx
        if currentIdx is None:
            return None
        currentIdx -= 1
        if currentIdx < 0:
            currentIdx = len(self)-1
        self.currentIdx = currentIdx
        return currentIdx
