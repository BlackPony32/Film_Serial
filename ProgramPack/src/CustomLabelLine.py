from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QLabel
from PyQt5.QtGui import QFont
class CustomLabelLineEdit(QWidget):
    def __init__(self, label_text, placeholder_text, parent=None):
        super().__init__(parent)

        self.label = QLabel(label_text)
        self.label.setFont(QFont("Arial", 12, QFont.Bold))
        self.label.setStyleSheet("color: blue")

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder_text)
        self.line_edit.setFont(QFont("Arial", 12))
        self.line_edit.setStyleSheet("background-color: #F0F0F0")

        layout = QFormLayout()
        layout.addRow(self.label, self.line_edit)
        layout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(layout)

    def text(self):
        return self.line_edit.text()

    def set_text(self, text):
        self.line_edit.setText(text)