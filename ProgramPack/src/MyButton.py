from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont, QPainterPath
from PyQt5.QtWidgets import QPushButton

class _MyButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Встановлюємо стилі кнопки
        self.setStyleSheet(
            '''
            QPushButton {
                background-color: #6C3483;  /* Пурпурно-червоний */
                color: #FFFFFF;
                border-style: outset;
                padding: 2px;
                font: bold 15px;
                border-width: 6px;
                border-radius: 10px;
                border-color: #512E5F;  /* Темний пурпурно-червоний */
            }
            QPushButton:hover {
                background-color: #F39C12;  /* Помаранчевий */
            }
            QPushButton:pressed {
                background-color: #117A65;  /* Темний зелений */
            }
            '''
        )

        # Ініціалізуємо анімаційні властивості
        self.current_color = QColor(255, 0, 0)
        """self.animation = QPropertyAnimation(self, b"color")
        self.animation.setDuration(2000)
        self.animation.setLoopCount(-1)
        self.animation.setStartValue(QColor(255, 0, 0))
        self.animation.setEndValue(QColor(0, 255, 0))
        self.animation.valueChanged.connect(self.update)

        # Запускаємо анімацію через 3 секунди
        self.timer = QTimer()
        self.timer.timeout.connect(self.start_animation)
        self.timer.start(1000)
        """


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
            painter.setPen(QPen(self.current_color, 3))

        painter.drawRoundedRect(rect.adjusted(2, 2, -2, -2), 15, 15)

        # Встановлюємо фон тексту
        painter.setPen(QColor(255, 255, 0))
        painter.setBrush(QBrush(QColor(47, 47, 47)))
        painter.drawRect(rect.adjusted(20, 20, -20, -20))

        super().paintEvent(event)

    #def start_animation(self):
    #    self.animation.start()

    def setColor(self, color):
        self.current_color = color
        self.update()

    def getColor(self):
        return self.current_color

    color = property(getColor, setColor)
