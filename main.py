import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import random as rd

from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)
        self.x, self.y = self.get_cords()
        self.size = 0
        self.color = self.get_color()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def get_cords(self):
        # Возвращает координаты центра кнопки
        pb = self.pushButton
        x = pb.x() + pb.width() // 2
        y = pb.y() + pb.height() // 2
        return x, y

    def draw(self, qp: QtGui.QPainter):
        # Генерируем цвет
        qp.setBrush(self.color)

        qp.drawEllipse(QtCore.QPoint(self.x, self.y), self.size, self.size)

    def get_color(self):
        r = rd.randint(0, 255)
        g = rd.randint(0, 255)
        b = rd.randint(0, 255)
        color = QtGui.QColor(r, g, b)
        return color

    def run(self):
        # Генерируем размер и перепроверяем координаты кнопки. Меняем цвет.
        self.size = rd.randint(0, 200)
        self.x, self.y = self.get_cords()
        self.color = self.get_color()
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
