from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont, QPainterPath


class MyButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

        # Встановлюємо стилі кнопки
        self.setStyleSheet(
            '''
            QPushButton {
                color: #FFFF00;
                background-color: #800080;
                border: 2px solid #FF0000;
                border-radius: 10px;
                padding: 10px;
            }

            QPushButton:pressed {
                background-color: #808080;
            }
            '''
        )

        # Ініціалізуємо анімаційні властивості
        self.current_color = QColor(255, 0, 0)
        self.animation = QPropertyAnimation(self, b"color")
        self.animation.setDuration(2000)
        self.animation.setLoopCount(-1)
        self.animation.setStartValue(QColor(255, 0, 0))
        self.animation.setEndValue(QColor(0, 255, 0))
        self.animation.valueChanged.connect(self.update)

        # Запускаємо анімацію через 3 секунди
        self.timer = QTimer()
        self.timer.timeout.connect(self.start_animation)
        self.timer.start(100)



    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Малюємо заокруглену форму з рамкою
        rect = self.rect()
        painter.setBrush(Qt.NoBrush)
        # Встановлюємо розмір та розташування тексту

        painter.setFont(QFont("Arial", 16, QFont.Bold))
        text_rect = rect.adjusted(15, 15, -15, -15)
        painter.drawText(text_rect, Qt.AlignCenter, self.text())


        if self.isDown():
            painter.setPen(QPen(QColor(0, 255, 0), 2))
        else:
            painter.setPen(QPen(self.current_color, 2))

        painter.drawRoundedRect(rect.adjusted(1, 1, -1, -1), 10, 10)

        # Встановлюємо фон тексту
        painter.setPen(QColor(255, 255, 0))
        painter.setBrush(QBrush(QColor(47, 47, 47)))
        painter.drawRect(rect.adjusted(10, 10, -10, -10))

        super().paintEvent(event)

    def start_animation(self):
        self.animation.start()

    def setColor(self, color):
        self.current_color = color
        self.update()

    def getColor(self):
        return self.current_color

    color = property(getColor, setColor)
