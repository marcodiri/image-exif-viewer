from typing import Optional

import exifread
from PyQt5.QtGui import QPixmap


class Image:
    _metadata: Optional[dict] = None

    def __init__(self, path: str):
        self.path = path
        self.pixmap = QPixmap(path)

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
