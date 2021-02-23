from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AllLicenses(object):
    def setupUiAll(self, AllLicenses):
        AllLicenses.setObjectName("AllLicenses")
        AllLicenses.resize(647, 484)
        self.AllLicensesTable = QtWidgets.QListView(AllLicenses)
        self.AllLicensesTable.setGeometry(QtCore.QRect(10, 110, 631, 361))
        self.AllLicensesTable.setObjectName("AllLicensesTable")
        self.LicenseLabel = QtWidgets.QLabel(AllLicenses)
        self.LicenseLabel.setGeometry(QtCore.QRect(210, 30, 251, 71))
        self.LicenseLabel.setObjectName("LicenseLabel")

        self.retranslateUiAll(AllLicenses)
        QtCore.QMetaObject.connectSlotsByName(AllLicenses)

    def retranslateUiAll(self, AllLicenses):
        _translate = QtCore.QCoreApplication.translate
        AllLicenses.setWindowTitle(_translate("AllLicenses", "All Licenses Status"))
        self.LicenseLabel.setText(_translate("AllLicenses", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; text-decoration: underline;\">All Licenses</span></p></body></html>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AllLicenses = QtWidgets.QWidget()
#     ui = Ui_AllLicenses()
#     ui.setupUi(AllLicenses)
#     AllLicenses.show()
#     sys.exit(app.exec_())
