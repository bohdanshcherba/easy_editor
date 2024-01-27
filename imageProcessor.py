import os 
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ImageProcessor:
    def __init__(self, label):
        self.original = None
        self.filename =  None
        self.dir = None
        self.save_dir = "edited/"
        self.label = label

    def loadImage(self, filname, dir):
        self.filename = filname
        self.dir = dir

        path = os.path.join(self.dir, self.filename)
        self.original = Image.open(path)

    def showImage(self, path):
        self.label.hide()
        pixmap = QPixmap(path)

        w = self.label.width()
        h = self.label.height()

        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio )
        self.label.setPixmap(pixmap)
        self.label.show()

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)

        if not os.path.exists(path) or not os.path.isdir(path):
            os.mkdir(path)

        image_path = os.path.join(path, self.filename)

        self.original.save(image_path)
        self.showImage(image_path)



    def do_bw(self):
        self.original = self.original.convert("L")

    def left(self):
        pass

    def blur(self):
        pass
