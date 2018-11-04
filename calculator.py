import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        designer_file = QFile("calculator.ui")
        designer_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.ui = loader.load(designer_file, self)

        designer_file.close()


        self.ui.pushButton_clear.clicked.connect(self.clear_text)
        self.ui.pushButton_one.clicked.connect(self.show_text)

        self.setWindowTitle("Qt for Python : PySide2")


    def clear_text(self):
        self.ui.lineEdit.clear()


    def show_text(self):
        one = self.ui.pushButton_one.text()
        print(str(one))
        self.ui.lineEdit.setText(one)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
