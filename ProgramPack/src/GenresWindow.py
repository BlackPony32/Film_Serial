import os
import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QCheckBox, QPushButton, \
    QPlainTextEdit, QMessageBox, QFileDialog


class GenreSelectionApp(QWidget):
    def __init__(self, genres):
        super().__init__()
        self.genres = genres
        self.selected_genres = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Вибір жанрів")
        self.setGeometry(100, 100, 400, 400)
        layout = QVBoxLayout()

        label = QLabel("Виберіть жанри:")
        layout.addWidget(label)

        grid_layout = QGridLayout()
        self.checkboxes = []
        row = 0
        col = 0
        for genre in self.genres:
            checkbox = QCheckBox(genre)
            checkbox.stateChanged.connect(self.update_selected_genres)
            self.checkboxes.append(checkbox)
            grid_layout.addWidget(checkbox, row, col)
            col += 1
            if col == 5:
                col = 0
                row += 1

        layout.addLayout(grid_layout)

        button = QPushButton("Підтвердити")
        button.clicked.connect(self.show_selected_genres)
        layout.addWidget(button)

        self.selected_genres_text_edit = QPlainTextEdit()
        layout.addWidget(self.selected_genres_text_edit)

        self.add_button = QPushButton("Додати")
        self.add_button.clicked.connect(self.add_selected_genres)
        layout.addWidget(self.add_button)


        self.setLayout(layout)

    def update_selected_genres(self, state):
        checkbox = self.sender()
        genre = checkbox.text()

        if state == 2:
            if genre not in self.selected_genres:
                self.selected_genres.append(genre)
        else:
            if genre in self.selected_genres:
                self.selected_genres.remove(genre)

    def show_selected_genres(self):
        genres_str = ", ".join(self.selected_genres)
        self.selected_genres_text_edit.setPlainText(genres_str)

    def add_selected_genres(self):
        file_name = "data.txt"
        file_path = os.path.join(os.getcwd(), file_name)

        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.selected_genres_text_edit.toPlainText())
                self.close()
        except Exception as e:
            QMessageBox.critical(self, 'Помилка', f'Виникла помилка під час збереження файлу:\n{str(e)}')


