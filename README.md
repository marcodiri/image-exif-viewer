# Image + EXIF Viewer
Image + EXIF Viewer developed with PyQt5.

The project demonstrates the use of the Model-View-Presenter pattern and signal/slot feature of PyQt. Components can alter the models, and changes are signaled back to the components to update the views.

## Features
- **Visualization of images**: the GUI can open one or multiple images and the user can navigate through the images with keyboard left/right arrows.
- **GUI rescaling**: the GUI is initially displayed with a maximum dimension of 512 pixels if the image is larger. Rescaling the GUI also rescales the image appropriately, maintaining proportions.
- **Image rotation**: displayed image can be rotated in 90° increments via action buttons or keyboard shortcuts.
- **EXIF viewer**: image EXIF tags can be visualized in a dialog window. If GPS coordinates are present in the image, a link is provided to open the location in Google Maps.

Keyboard shortcuts are listed next to the respective command.

## Install
Clone the repo
```shell
> git clone https://github.com/marcodiri/image-exif-viewer.git
```
Install inside a virtual environment
```shell
> cd image-exif-viewer
> pip install .
```
Run the program
```shell
> python src/main.py
```
Or to open images directly
```shell
> python src/main.py /path/to/image.jpg /path/to/other/image.png
```