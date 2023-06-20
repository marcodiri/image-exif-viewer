from typing import Optional

import exifread
from PyQt5.QtGui import QPixmap, QTransform


class Image:
    _metadata: Optional[dict] = None
    transform: Optional[QTransform] = None

    def __init__(self, path: str):
        self.path = path
        self._pixmap = QPixmap(path)

    @property
    def metadata(self):
        if self._metadata is None:
            self._metadata = {
                "Image Path": self.path,
                "Image Width": self.pixmap.width(),
                "Image Height": self.pixmap.height()
            }
            with open(self.path, 'rb') as f:
                self._metadata.update(exifread.process_file(f))
        return self._metadata

    @property
    def pixmap(self):
        if self.transform is not None:
            return self._pixmap.transformed(self.transform)
        return self._pixmap
