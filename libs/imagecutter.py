import os.path
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except ImportError:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
    from PyQt4.QtCore import QString



class ImageCutter(QObject):
    def __init__(self,image,parent = None):
        super(ImageCutter,self).__init__(parent)
        self.imagename = image
        self.img = QImage()
        self.img.load(image)
        self.area=self.pix = self.img

    def cut(self,rect):
        if type(rect) == list and len(rect) == 4:
            self.area = self.pix.copy(rect[0],rect[1],rect[2],rect[3])
        else:
            print("invalid rects!\n")

    def saveas(self,name):
        if self.imagename:
            self.area.save(name)

# if __name__ == '__main__':
#     argv = []
#     app = QApplication(argv)
#     cutter = ImageCutter("/home/hhit/PycharmProjects/test.JPG")
#     rect = [1000,1000,5500,2000]
#     cutter.cut(rect)
#     dg = CuttingDialog()
#     if dg.exec():
#         print(rect)
#         cutter.saveas("/home/hhit/PycharmProjects/test_ 1.jpg")
#     else:
#         print("canceled")
#     dg.close()
#     app.exec_()
