import os
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect

class SeriesSeasonSelection(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Вибір кількості сезонів')
        self.setGeometry(400, 300, 450, 180)

        layout = QVBoxLayout()

        self.label = QLabel('Оберіть кількість сезонів:')
        self.label.setFont(QFont("Arial", 15))
        layout.addWidget(self.label)

        self.label_value = QLabel('1')
        self.label_value.setFont(QFont("Arial", 15))
        layout.addWidget(self.label_value)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(16)  # Змінено максимальне значення на 16
        self.slider.setValue(1)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        layout.addWidget(self.slider)

        self.save_button = QPushButton('Зберегти')
        layout.addWidget(self.save_button)

        self.setLayout(layout)

        self.slider.valueChanged.connect(self.on_slider_value_changed)
        self.save_button.clicked.connect(self.save_to_file)

    def on_slider_value_changed(self, value):
        if value <= 15:
            self.label_value.setText(str(value))
        else:
            self.label_value.setText('15+')

        # Анімація для збільшення текстового напису при зміні значення слайдера
        animation = QPropertyAnimation(self.label, b"geometry")
        animation.setDuration(200)
        animation.setStartValue(QRect(10, 30, 400, 30))
        animation.setEndValue(QRect(10, 30, 450, 30))
        animation.start()

    def save_to_file(self):
        project_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        file_path = os.path.join(project_dir, "Series_QuantitySeason.txt")

        # Open the file for writing and save the text
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.label_value.text())
            self.close()
            # QMessageBox.information(self, 'Success', 'Text saved successfully!')

        except Exception as e:
            print(f"Error writing to the file: {e}")
            QMessageBox.critical(self, 'Error', f'Error saving text:\n{str(e)}')