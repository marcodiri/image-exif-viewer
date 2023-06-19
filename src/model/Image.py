from typing import Optional

import exifread


class Image:
    _metadata: Optional[dict] = None

    def __init__(self, path: str):
        self.path = path

    @property
    def metadata(self):
        if self._metadata is None:
            with open(self.path, 'rb') as f:
                self._metadata = exifread.process_file(f)
        return self._metadata
