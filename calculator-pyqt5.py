import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
#Sınıf Oluşturuyoruz
class HesapMakinesi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        self.lineEdit = QLineEdit()
        self.setLayout(self.layout)
        self.layout.addWidget(self.lineEdit)
        self.layout.addLayout(self.gridLayout)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, button in zip(positions, buttons):
            button_object = QPushButton(button)
            button_object.clicked.connect(self.button_clicked)
            self.gridLayout.addWidget(button_object, *position)

        self.clear_button = QPushButton('C')
        self.clear_button.clicked.connect(self.clear)
        self.gridLayout.addWidget(self.clear_button, 4, 0, 1, 2)

        self.backspace_button = QPushButton('<-')
        self.backspace_button.clicked.connect(self.backspace)
        self.gridLayout.addWidget(self.backspace_button, 4, 2, 1, 2)

        self.equal_button = QPushButton('=')
        self.equal_button.clicked.connect(self.calculate)
        self.gridLayout.addWidget(self.equal_button, 4, 3)

    def button_clicked(self):
        button = self.sender()
        current_text = self.lineEdit.text()
        clicked_text = button.text()

        if clicked_text == '=':
            self.calculate()
        else:
            self.lineEdit.setText(current_text + clicked_text)

    def clear(self):
        self.lineEdit.clear()

    def backspace(self):
        current_text = self.lineEdit.text()
        self.lineEdit.setText(current_text[:-1])

    def calculate(self):
        try:
            current_text = self.lineEdit.text()
            result = eval(current_text)
            self.lineEdit.setText(str(result))
        except Exception as e:
            self.lineEdit.setText("Hata!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hesap_makinesi = HesapMakinesi()
    hesap_makinesi.show()
    sys.exit(app.exec_())
