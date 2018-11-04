import sys
from PySide2.QtWidgets import QApplication
from calculator import MyWidget

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Pyside2 Calculator")

    widget = MyWidget()
    widget.show()
    app.exec_()


main()