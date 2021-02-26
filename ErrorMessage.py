from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(509, 204)
        Error.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton = QtWidgets.QPushButton(Error)
        self.pushButton.setGeometry(QtCore.QRect(220, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.ErrorMsg = QtWidgets.QLabel(Error)
        self.ErrorMsg.setGeometry(QtCore.QRect(40, 20, 441, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorMsg.setFont(font)
        self.ErrorMsg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ErrorMsg.setAutoFillBackground(True)
        self.ErrorMsg.setObjectName("ErrorMsg")
        self.pushButton.clicked.connect(Error.close)
        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Error!"))
        self.pushButton.setText(_translate("Error", "Close"))
        self.ErrorMsg.setText(_translate("Error", "Your\'e not the Owner of the contract.\n"
"You\'re not alowed to do that!"))
