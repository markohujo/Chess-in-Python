import pygame
import os

GUI_DIR = "gui"
IMAGES_DIR = "images"


class ImageLoader:
    def __init__(self, filename: str):
        self.filename = filename
        self._image = None

    def load(self):
        self._image = pygame.image.load(os.path.join(GUI_DIR, IMAGES_DIR, self.filename))
        return self

    def scale(self, width: int, height: int):
        self._image = pygame.transform.scale(self._image, (width, height))
        return self

    @property
    def get(self):
        return self._image
