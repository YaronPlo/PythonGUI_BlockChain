from PyQt5 import QtCore, QtGui, QtWidgets
import PCheck

class Ui_GetLicense(object):
    def setupUiGL(self, GetLicense):
        GetLicense.setObjectName("GetLicense")
        GetLicense.resize(608, 392)
        self.enterName = QtWidgets.QLineEdit(GetLicense)
        self.enterName.setGeometry(QtCore.QRect(110, 70, 171, 31))
        self.enterName.setStyleSheet("font: 11pt \"Calibri\";")
        self.enterName.setText("")
        self.enterName.setObjectName("enterName")
        self.enterLName = QtWidgets.QLineEdit(GetLicense)
        self.enterLName.setGeometry(QtCore.QRect(110, 130, 171, 31))
        self.enterLName.setStyleSheet("font: 11pt \"Calibri\";")
        self.enterLName.setText("")
        self.enterLName.setObjectName("enterLName")
        self.name = QtWidgets.QLabel(GetLicense)
        self.name.setGeometry(QtCore.QRect(110, 50, 131, 21))
        self.name.setObjectName("name")
        self.LName = QtWidgets.QLabel(GetLicense)
        self.LName.setGeometry(QtCore.QRect(110, 110, 131, 21))
        self.LName.setObjectName("LName")
        self.CheckBttn = QtWidgets.QPushButton(GetLicense)
        self.CheckBttn.setGeometry(QtCore.QRect(150, 180, 93, 28))
        self.CheckBttn.setObjectName("CheckBttn")
        self.ExpirationDate = QtWidgets.QGraphicsView(GetLicense)
        self.ExpirationDate.setGeometry(QtCore.QRect(300, 210, 256, 31))
        self.ExpirationDate.setObjectName("ExpirationDate")
        self.PoliceCheckPIC = QtWidgets.QLabel(GetLicense)
        self.PoliceCheckPIC.setGeometry(QtCore.QRect(370, 60, 121, 91))
        self.PoliceCheckPIC.setStyleSheet("image: url(:/PoliceCheck/immigration_check_officer_security_passport-512.jpg);")
        self.PoliceCheckPIC.setText("")
        self.PoliceCheckPIC.setObjectName("PoliceCheckPIC")
        self.label = QtWidgets.QLabel(GetLicense)
        self.label.setGeometry(QtCore.QRect(310, 180, 151, 16))
        self.label.setObjectName("label")

        self.retranslateUiGL(GetLicense)
        QtCore.QMetaObject.connectSlotsByName(GetLicense)

    def retranslateUiGL(self, GetLicense):
        _translate = QtCore.QCoreApplication.translate
        GetLicense.setWindowTitle(_translate("GetLicense", "Get License"))
        self.name.setText(_translate("GetLicense", "Enter Name:"))
        self.LName.setText(_translate("GetLicense", "Enter Last Name:"))
        self.CheckBttn.setText(_translate("GetLicense", "Check"))
        self.label.setText(_translate("GetLicense", "Your Exiration Date is:"))



# if __name__ == "__main__":
#     import sys
#     app2 = QtWidgets.QApplication(sys.argv)
#     GetLicense = QtWidgets.QWidget()
#     ui2 = Ui_GetLicense()
#     ui2.setupUiGL(GetLicense)
#     GetLicense.show()
#     sys.exit(app2.exec_())
