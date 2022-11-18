import random
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_circles(qp)
            # Завершаем рисование
            qp.end()

    def run(self):
        self.do_paint = True
        self.repaint()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(random.randint(1, 20)):
            r = random.randint(10, 200)
            qp.drawEllipse(random.randint(0, self.size().width()), random.randint(0, self.size().height()),
                           r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())