from datetime import datetime, date

from PyQt5 import QtCore, QtGui, QtWidgets
from ErrorMessage import Ui_Error
from web3 import Web3
import json
import LicenseBF
import web3_interface

infura_url = 'https://ropsten.infura.io/v3/a1b856fc34e24754bdf947bb1ca04432'
expiration_date = 0

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
        self.fNameInput.setGeometry(QtCore.QRect(80, 230, 113, 22))
        self.fNameInput.setObjectName("fNameInput")

        self.LNameInput = QtWidgets.QLineEdit(AddDriverLicense)
        self.LNameInput.setGeometry(QtCore.QRect(80, 260, 113, 22))
        self.LNameInput.setObjectName("LNameInput")

        self.IdInput = QtWidgets.QLineEdit(AddDriverLicense)
        self.IdInput.setGeometry(QtCore.QRect(80, 290, 113, 22))
        self.IdInput.setObjectName("IdInput")

        # self.exprInput = QtWidgets.QLineEdit(AddDriverLicense)
        # self.exprInput.setGeometry(QtCore.QRect(80, 350, 113, 22))
        # self.exprInput.setObjectName("exprInput")

        current_month = datetime.now().month
        current_year = datetime.now().year
        self.calendar = QtWidgets.QCalendarWidget(AddDriverLicense)
        # self.LNameInput.setGeometry(QtCore.QRect(264, 230, 113, 22))
        self.calendar.setGeometry(QtCore.QRect(203, 260, 275, 140))
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumDate(QtCore.QDate(current_year, current_month + 6, 1))
        self.calendar.clicked.connect(self.set_expiration)
        # self.calendar.move(20, 20)
        # cal.clicked[QtCore.QDate].connect(self.showDate)

        self.FirstName = QtWidgets.QLabel(AddDriverLicense)
        self.FirstName.setGeometry(QtCore.QRect(20, 230, 101, 16))
        self.FirstName.setObjectName("FirstName")

        self.LastName = QtWidgets.QLabel(AddDriverLicense)
        self.LastName.setGeometry(QtCore.QRect(20, 260, 101, 16))
        # self.LastName.setGeometry(QtCore.QRect(90, 290, 101, 16))
        self.LastName.setObjectName("LastName")

        self.Id = QtWidgets.QLabel(AddDriverLicense)
        self.Id.setGeometry(QtCore.QRect(20, 290, 101, 16))
        self.Id.setObjectName("ID")

        self.ExprDate = QtWidgets.QLabel(AddDriverLicense)
        # self.LastName.setGeometry(QtCore.QRect(203, 230, 101, 16))
        self.ExprDate.setGeometry(QtCore.QRect(203, 230, 101, 16))
        self.ExprDate.setObjectName("ExprDate")

        self.DeployBttn = QtWidgets.QPushButton(AddDriverLicense)
        self.DeployBttn.setGeometry(QtCore.QRect(80, 340, 111, 51))


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
        self.DeployBttn.clicked.connect(AddDriverLicense.close)


    def retranslateUiAL(self, AddDriverLicense):
        _translate = QtCore.QCoreApplication.translate
        AddDriverLicense.setWindowTitle(_translate("AddDriverLicense", "Add License"))
        self.FirstName.setText(_translate("AddDriverLicense", "First Name:"))
        self.LastName.setText(_translate("AddDriverLicense", "Last Name:"))
        self.Id.setText(_translate("AddDriverLicense", "ID:"))
        self.ExprDate.setText(_translate("AddDriverLicense", "Expiration Date:"))
        self.DeployBttn.setText(_translate("AddDriverLicense", "Add license"))

    def ErrorMsg(self):
        self.window = QtWidgets.QMainWindow()
        self.uiNew = Ui_Error()
        self.uiNew.setupUi(self.window)
        self.window.show()

    def set_expiration(self, _date):
        global expiration_date
        print(f'{_date}')
        now = datetime.now()
        now = date(now.year, now.month, now.day)
        selected = date(_date.year(), _date.month(), _date.day())
        print(f'now = {now}\n'
              f'selected = {selected}')
        expiration_date = (selected - now).days
        print(f'expiration: {expiration_date}')

    def addLicense(self):
        fname = self.fNameInput.text()
        lname = self.LNameInput.text()
        id = self.IdInput.text()
        try:
            web3_interface.add_licence(fname, lname, id, expiration_date)
        except:
            self.ErrorMsg()
