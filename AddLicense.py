from PyQt5 import QtCore, QtGui, QtWidgets
from web3 import Web3
import json
import LicenseBF
import web3_interface

infura_url = 'https://ropsten.infura.io/v3/a1b856fc34e24754bdf947bb1ca04432'


class Addlicense():

    def setupUiAL(self, AddDriverLicense):
        AddDriverLicense.setObjectName("AddDriverLicense")
        AddDriverLicense.resize(541, 414)
        self.License_Pic = QtWidgets.QLabel(AddDriverLicense)
        self.License_Pic.setGeometry(QtCore.QRect(-370, 0, 1281, 211))
        self.License_Pic.setStyleSheet("image: url(:/LBF/BACKFRONT_LICENSE.jpg);")
        self.License_Pic.setText("")
        self.License_Pic.setObjectName("License_Pic")

        self.fNameInput = QtWidgets.QLineEdit(AddDriverLicense)
        self.fNameInput.setGeometry(QtCore.QRect(200, 230, 113, 22))
        self.fNameInput.setObjectName("fNameInput")

        self.LNameInput = QtWidgets.QLineEdit(AddDriverLicense)
        self.LNameInput.setGeometry(QtCore.QRect(200, 260, 113, 22))
        self.LNameInput.setObjectName("LNameInput")

        self.IdInput = QtWidgets.QLineEdit(AddDriverLicense)
        self.IdInput.setGeometry(QtCore.QRect(200, 290, 113, 22))
        self.IdInput.setObjectName("IdInput")

        self.exprInput = QtWidgets.QLineEdit(AddDriverLicense)
        self.exprInput.setGeometry(QtCore.QRect(200, 350, 113, 22))
        self.exprInput.setObjectName("exprInput")

        self.FirstName = QtWidgets.QLabel(AddDriverLicense)
        self.FirstName.setGeometry(QtCore.QRect(90, 230, 101, 16))
        self.FirstName.setObjectName("FirstName")

        self.LastName = QtWidgets.QLabel(AddDriverLicense)
        self.LastName.setGeometry(QtCore.QRect(90, 260, 101, 16))
        # self.LastName.setGeometry(QtCore.QRect(90, 290, 101, 16))
        self.LastName.setObjectName("LastName")

        self.Id = QtWidgets.QLabel(AddDriverLicense)
        self.Id.setGeometry(QtCore.QRect(90, 290, 101, 16))
        self.Id.setObjectName("ID")

        self.ExprDate = QtWidgets.QLabel(AddDriverLicense)
        self.ExprDate.setGeometry(QtCore.QRect(90, 350, 101, 16))
        self.ExprDate = QtWidgets.QLabel(AddDriverLicense)
        self.ExprDate.setGeometry(QtCore.QRect(90, 350, 101, 16))
        self.ExprDate.setObjectName("ExprDate")

        self.DeployBttn = QtWidgets.QPushButton(AddDriverLicense)
        self.DeployBttn.setGeometry(QtCore.QRect(390, 260, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.DeployBttn.setFont(font)
        self.DeployBttn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DeployBttn.setObjectName("DeployBttn")
        self.retranslateUiAL(AddDriverLicense)
        QtCore.QMetaObject.connectSlotsByName(AddDriverLicense)

        self.DeployBttn.clicked.connect(self.addLicense)

    def retranslateUiAL(self, AddDriverLicense):
        _translate = QtCore.QCoreApplication.translate
        AddDriverLicense.setWindowTitle(_translate("AddDriverLicense", "Add License"))
        self.FirstName.setText(_translate("AddDriverLicense", "First Name:"))
        self.LastName.setText(_translate("AddDriverLicense", "Last Name:"))
        self.Id.setText(_translate("AddDriverLicense", "ID:"))
        self.ExprDate.setText(_translate("AddDriverLicense", "Expiration Date:"))
        self.DeployBttn.setText(_translate("AddDriverLicense", "Deploy"))


    def addLicense(self):
        fname = self.fNameInput.text()
        lname= self.LNameInput.text()
        Id= self.IdInput.text()
        exprDate = self.exprInput.text()
        print("First Name:\t"+fname+"\n" + "Last Name:\t"+lname+"\n"+"ID:\t"+Id+"EXPR:\t"+exprDate)
        web3_interface.add_licence(fname, lname, Id, exprDate)

    # def deploy(self):
    #     import sys
    #     app1 = QtWidgets.QApplication(sys.argv)
    #     AddDriverLicense = QtWidgets.QWidget()
    #     ui1 = Addlicense()
    #     ui1.setupUiAL(AddDriverLicense)
    #     AddDriverLicense.show()
    #     sys.exit(app1.exit)
