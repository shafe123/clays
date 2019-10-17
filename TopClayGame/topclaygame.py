# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtGui import QPalette, QColor


class TopClayGame(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

if __name__ == "__main__":
    app = QApplication([])

    dark_palette = QPalette()

    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)

    app.setStyle('Fusion')
    app.setPalette(dark_palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window = QWidget()

    layout = QVBoxLayout()

    btn_login = QPushButton('Login')
    btn_play_without = QPushButton('Play wihtout Login')

    layout.addWidget(btn_login)
    layout.addWidget(btn_play_without)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())
