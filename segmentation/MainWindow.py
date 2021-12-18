import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Data import DataProcess
from Unet import Unet


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.unet = Unet()
        self.model = self.unet.get_unet()
        self.mydata = DataProcess(512, 512)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.mainLayout = QVBoxLayout()

        trainButton = QPushButton('Обучить нейронную сеть', self)
        trainButton.clicked.connect(self.trainNeuralNetwork)

        segmintationPredicatButton = QPushButton('Сегментировать изображение', self)
        segmintationPredicatButton.clicked.connect(self.segmentationImage)

        dataButton = QPushButton('Подготовить данные', self)
        dataButton.move(60, 60)
        dataButton.clicked.connect(self.dataPreparation)

        saveImg = QPushButton('Сохранить сегментированные изображения', self)
        saveImg.move(80, 80)
        saveImg.clicked.connect(self.saveImg)

        self.mainLayout.addWidget(trainButton)
        self.mainLayout.addWidget(dataButton)
        self.mainLayout.addWidget(trainButton)
        self.mainLayout.addWidget(segmintationPredicatButton)
        self.mainLayout.addWidget(saveImg)
        centralWidget.setLayout(self.mainLayout)

        self.resize(400, 200)
        self.setWindowTitle('Segmentation app')
        self.show()

    def trainNeuralNetwork(self):
        self.unet.train()

    def segmentationImage(self):
        self.unet.segmintationImage()
        self.unet.save_img()

    def dataPreparation(self):
        self.mydata.create_train_data()
        self.mydata.create_test_data()

    def saveImg(self):
        self.unet.save_img()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
