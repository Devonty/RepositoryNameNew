import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import random as rd

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.run)
        self.x, self.y = self.get_cords()
        self.size = 0

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def get_cords(self):
        pb = self.pushButton
        x = pb.x() + pb.width() // 2
        y = pb.y() + pb.height() // 2
        return x, y

    def draw(self, qp : QtGui.QPainter):

        qp.setBrush(QtGui.QColor(255,255,0))
        qp.drawEllipse(QtCore.QPoint(self.x, self.y), self.size, self.size)


    def run(self):
        self.size = rd.randint(0, 200)
        self.x, self.y = self.get_cords()
        self.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

