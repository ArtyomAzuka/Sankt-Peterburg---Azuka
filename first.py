from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        if event == self.pushButton.clicked:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_flag(qp)
            # Завершаем рисование
            qp.end()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        x1 = randint(0, 799)
        y1 = randint(0, 599)
        coeff = randint(0, 600 - y1)
        qp.drawEllipse(x1, y1, x1 + coeff, y1 + coeff)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
