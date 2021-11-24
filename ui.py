# Form implementation generated from reading ui file 'converter.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(34, 34, 46);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 270))
        self.frame.setStyleSheet("background-color: rgb(251, 91, 93);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 0, 240, 50))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 50, 180, 180))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("exchanging.png"))
        self.label_2.setObjectName("label_2")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 300, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: rgb(34, 34, 46);\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(50, 390, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color: rgb(34, 34, 46);\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.input_amount.setText("")
        self.input_amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(50, 480, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: rgb(34, 34, 46);\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(50, 570, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: rgb(34, 34, 46);\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 660, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #fb5b5d;\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #fa4244;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Конвертер валют"))
        self.pushButton.setText(_translate("MainWindow", "Конвертируй"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
