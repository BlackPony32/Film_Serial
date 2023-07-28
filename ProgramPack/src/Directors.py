import os
import sys
import json

from PyQt5.QtCore import QTextStream, QFile, QIODevice
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLabel, QCheckBox, QPushButton, \
    QPlainTextEdit, QMessageBox, QFileDialog, QLineEdit


class DirectorsApp(QWidget):
    def __init__(self, genres):
        super().__init__()
        self.genres = genres
        self.selected_genres = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Вибір режисерів")
        self.setGeometry(100, 100, 400, 400)
        layout = QVBoxLayout()

        label = QLabel("Оберіть режисера:")
        layout.addWidget(label)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Пошук режисера")
        self.search_input.textChanged.connect(self.filter_directors)
        layout.addWidget(self.search_input)

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
        #file_name = "../my_data/data.txt"
        #self.file_path = os.path.join(os.getcwd(), file_name)
        text_to_save = self.selected_genres_text_edit.toPlainText()
        #self.file_name = ":/txt/data.txt"

        # Get the absolute path to the project's directory
        project_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        file_path = os.path.join(project_dir, "dataDirectors.txt")

        # Open the file for writing and save the text
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_to_save)
            self.close()
            #QMessageBox.information(self, 'Success', 'Text saved successfully!')

        except Exception as e:
            print(f"Error writing to the file: {e}")
            QMessageBox.critical(self, 'Error', f'Error saving text:\n{str(e)}')

    def filter_directors(self):
        search_text = self.search_input.text().strip()
        for checkbox in self.checkboxes:
            director = checkbox.text()
            if search_text.lower() in director.lower():
                checkbox.setVisible(True)
            else:
                checkbox.setVisible(False)
