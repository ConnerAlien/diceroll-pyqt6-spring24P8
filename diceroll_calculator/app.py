import sys

from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QLabel,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rando")
        self.setContentsMargins(12, 40, 12, 12)
        self.resize(320, 240)

        #install fonts
        self.set_font("Comfortaa-Light.ttf")
        self.set_font("Comfortaa-Bold.ttf")

        layout = QVBoxLayout()
        title_label = QLabel("Rando - Dice Calculator")
        title_label.setFont(QFont("Comfortaa-Bold.ttf", 24, 8))

        Label_1 = QLabel("How many dice do you want to roll?")
        Label_1.setFont(QFont("Comfortaa-Light.ttf", 12))

        Input_1 = QSpinBox()
        Input_1.setFont(QFont("Comfortaa-Light.ttf", 12))

        roll_button = QPushButton("Roll")
        roll_button.setFont(QFont("Comfortaa-Light.ttf", 12, 4))

        layout.addWidget(title_label)
        layout.addWidget(Label_1)
        layout.addWidget(Input_1)
        layout.addWidget(roll_button)
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def set_font(self, font_name: str) -> None:
        font_dir = "resources/fonts/"
        font_path = font_dir + font_name
        success = QFontDatabase.addApplicationFont(font_path)
        #If it failed to add the font
        if success == -1:
            print(f"{font_name} not loaded. \nTried path '{font_path}'")

app = QApplication(sys.argv)

stylesheet = None
styles_path = "resources/styles.qss.txt"
#Get the cpde from the stylesheet
with open(styles_path, "r") as f:
    stylesheet = f.read()
app.setStyleSheet(stylesheet)

window = MainWindow()
window.show()

app.exec()
