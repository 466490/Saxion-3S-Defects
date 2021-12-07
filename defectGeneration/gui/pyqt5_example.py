from PyQt5 import QtWidgets
from PyQt5.QtGui import QWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Application():
    def __init__():
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setGeometry(0, 0, 1920, 1080)
        window.setWindowTitle("Defect Generation")

        label = QtWidgets.QLabel(window)
        label.setText("This is the first label")

        window.show()
        sys.exit(app.exec())


app = Application()