from PyQt5 import QtCore, QtGui, QtWidgets
from web3 import Web3
import json
import RenewL
import web3_interface
from AddLicense import Addlicense
from ErrorMessage import Ui_Error

class Ui_RenewLicense(object):
    def setupUiRL(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 257)
        self.fname = QtWidgets.QLabel(Form)
        self.fname.setGeometry(QtCore.QRect(80, 40, 131, 41))
        self.fname.setObjectName("fname")
        self.lname = QtWidgets.QLabel(Form)
        self.lname.setGeometry(QtCore.QRect(80, 100, 111, 61))
        self.lname.setObjectName("lname")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 210, 93, 28))
        self.pushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ErrorMsg)
        self.pushButton.clicked.connect(Form.close)
        self.picture = QtWidgets.QLabel(Form)
        self.picture.setGeometry(QtCore.QRect(260, 20, 291, 161))
        self.picture.setStyleSheet("image: url(:/RenewL/Renew.png);")
        self.picture.setText("")
        self.picture.setObjectName("picture")
        self.inputFname = QtWidgets.QLineEdit(Form)
        self.inputFname.setGeometry(QtCore.QRect(80, 80, 151, 31))
        self.inputFname.setObjectName("inputFname")
        self.inputLname = QtWidgets.QLineEdit(Form)
        self.inputLname.setGeometry(QtCore.QRect(80, 140, 151, 31))
        self.inputLname.setObjectName("inputLname")

        self.retranslateUiRL(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUiRL(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RenewLicense"))
        self.fname.setText(_translate("Form", "Enter First Name:"))
        self.lname.setText(_translate("Form", "Enter Last Name:"))
        self.pushButton.setText(_translate("Form", "Deploy"))

    def ErrorMsg(self):
        self.window = QtWidgets.QMainWindow()
        self.uiNew = Ui_Error()
        self.uiNew.setupUi(self.window)
        self.window.show()
