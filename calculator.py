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
        self.ui.pushButton_zero.clicked.connect(self.clickZero)
        self.ui.pushButton_one.clicked.connect(self.clickOne)
        self.ui.pushButton_two.clicked.connect(self.clickTwo)
        self.ui.pushButton_three.clicked.connect(self.clickThree)
        self.ui.pushButton_four.clicked.connect(self.clickFour)
        self.ui.pushButton_five.clicked.connect(self.clickFive)
        self.ui.pushButton_six.clicked.connect(self.clickSix)
        self.ui.pushButton_seven.clicked.connect(self.clickSeven)
        self.ui.pushButton_eight.clicked.connect(self.clickEight)
        self.ui.pushButton_nine.clicked.connect(self.clickNine)


        self.setWindowTitle("My Calculator")


    def clear_text(self):
        self.ui.lineEdit.clear()


    def clickZero(self):
        number = self.ui.pushButton_zero.text()
        self.ui.lineEdit.setText(number)

    def clickOne(self):
        number = self.ui.pushButton_one.text()
        self.ui.lineEdit.setText(number)

    def clickTwo(self):
        number = self.ui.pushButton_two.text()
        self.ui.lineEdit.setText(number)

    def clickThree(self):
        number = self.ui.pushButton_three.text()
        self.ui.lineEdit.setText(number)

    def clickFour(self):
        number = self.ui.pushButton_four.text()
        self.ui.lineEdit.setText(number)

    def clickFive(self):
        number = self.ui.pushButton_five.text()
        self.ui.lineEdit.setText(number)

    def clickSix(self):
        number = self.ui.pushButton_six.text()
        self.ui.lineEdit.setText(number)

    def clickSeven(self):
        number = self.ui.pushButton_seven.text()
        self.ui.lineEdit.setText(number)

    def clickEight(self):
        number = self.ui.pushButton_eight.text()
        self.ui.lineEdit.setText(number)

    def clickNine(self):
        number = self.ui.pushButton_nine.text()
        self.ui.lineEdit.setText(number)
