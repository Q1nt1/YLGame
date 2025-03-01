import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QLabel, QDialog, QDialogButtonBox)
from PyQt6.QtGui import QFont
from main import Main
from PyQt6.QtCore import Qt
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Шахматы - Главное меню")
        self.setGeometry(100, 100, 400, 300) #x, y, width, height

        layout = QVBoxLayout()

        title_label = QLabel("Шахматы")
        title_label.setFont(QFont("Arial", 32))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)

        # Создание кнопок
        self.start_button = QPushButton("Играть")
        self.settings_button = QPushButton("Настройки")
        self.quit_button = QPushButton("Выход")

        # Подключение кнопок к функциям
        self.start_button.clicked.connect(self.start_game)
        self.settings_button.clicked.connect(self.show_settings)
        self.quit_button.clicked.connect(self.quit_game)

        # Добавление кнопок в layout
        layout.addWidget(self.start_button)
        layout.addWidget(self.settings_button)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)

    def start_game(self):
        main = Main()
        main.mainloop()


    def show_settings(self):
        """Открывает настройки (заглушка)"""
        print("Открытие настроек...")
        #Здесь можно добавить код для отображения окна настроек
        dialog = QDialog(self)
        dialog.setWindowTitle("Настройки")
        dialog_layout = QVBoxLayout()
        label = QLabel("Здесь будут настройки (заглушка)")
        dialog_layout.addWidget(label)
        dialog.setLayout(dialog_layout)
        dialog.exec()


    def quit_game(self):
        QApplication.instance().quit() #выход из приложения

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())