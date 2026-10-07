# image.py
from typing import Protocol

class Image(Protocol):
    def showImage(self) -> None:
        pass

class HighResolutionImage:
    def __init__(self, imageFilePath:str):
        self._data = len(imageFilePath)

    def showImage(self) -> None:
        print(f"Filename with length of {self._data} characters.")

class ProxyImage:
    def __init__(self, imageFilePath:str):
        self._imageFilePath = imageFilePath

    def showImage(self) -> None:
        # create the Image Object only when the image is required to be shown
        self._proxifiedImage = HighResolutionImage(self._imageFilePath)
        # now call showImage on realSubject
        self._proxifiedImage.showImage()


def render(obj:Image):
    obj.showImage()

proxyImage = ProxyImage("image.tiff")
render(proxyImage)
