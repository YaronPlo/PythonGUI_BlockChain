from PyQt5 import QtCore, QtGui, QtWidgets
from web3 import Web3
import json
import RenewL
import web3_interface
from AddLicense import Addlicense
from datetime import datetime, date

from ErrorMessage import Ui_Error
expiration_date = 0


class Ui_RenewLicense(object):
    def setupUiRL(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 257)

        self.id = QtWidgets.QLabel(Form)
        self.id.setGeometry(QtCore.QRect(20, 20, 131, 41))
        self.id.setObjectName("id")

        # self.lname = QtWidgets.QLabel(Form)
        # self.lname.setGeometry(QtCore.QRect(80, 100, 111, 61))
        # self.lname.setObjectName("lname")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 210, 93, 28))
        self.pushButton.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\ntext-decoration: underline;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.renew_license)
        self.pushButton.clicked.connect(Form.close)

        current_month = datetime.now().month
        current_year = datetime.now().year
        self.calendar = QtWidgets.QCalendarWidget(Form)
        # self.LNameInput.setGeometry(QtCore.QRect(264, 230, 113, 22))
        self.calendar.setGeometry(QtCore.QRect(20, 100, 275, 140))
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumDate(QtCore.QDate(current_year, current_month + 6, 1))
        self.calendar.clicked.connect(self.set_expiration)

        self.picture = QtWidgets.QLabel(Form)
        self.picture.setGeometry(QtCore.QRect(300, 20, 271, 141))
        self.picture.setStyleSheet("image: url(:/RenewL/Renew.png);")
        self.picture.setText("")
        self.picture.setObjectName("picture")

        self.inputID = QtWidgets.QLineEdit(Form)
        self.inputID.setGeometry(QtCore.QRect(20, 60, 151, 31))
        self.inputID.setObjectName("inputID")

        # self.inputLname = QtWidgets.QLineEdit(Form)
        # self.inputLname.setGeometry(QtCore.QRect(80, 140, 151, 31))
        # self.inputLname.setObjectName("inputLname")

        self.retranslateUiRL(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUiRL(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "RenewLicense"))
        self.id.setText(_translate("Form", "Enter Driver ID:"))
        # self.lname.setText(_translate("Form", "Enter Last Name:"))
        self.pushButton.setText(_translate("Form", "Renew Licence"))

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

    def renew_license(self):
        id = self.inputID.text()
        print(f'id = {id}')
        license = web3_interface.get_single_license(int(id))
        print(f'license = {license}')
        fname = license[0].split(' ')[0]
        print(f'fname = {fname}')
        lname = license[0].split(' ')[1]
        print(f'lname = {lname}')
        try:
            web3_interface.add_licence(fname, lname, id, expiration_date)
        except:
            self.ErrorMsg()
        # self.ErrorMsg

    def ErrorMsg(self):
        self.window = QtWidgets.QMainWindow()
        self.uiNew = Ui_Error()
        self.uiNew.setupUi(self.window)
        self.window.show()
