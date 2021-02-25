from PyQt5 import QtCore, QtGui, QtWidgets
import web3_interface

class Ui_AllLicenses(object):
    def setupUiAll(self, AllLicenses):
        AllLicenses.setObjectName("AllLicenses")
        AllLicenses.resize(647, 484)
        row_count = 1
        self.AllLicensesView = QtWidgets.QListView(AllLicenses)
        self.AllLicensesView.setGeometry(QtCore.QRect(10, 110, 631, 361))
        self.AllLicensesView.setObjectName("AllLicensesTable")

        self.create_table()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.table)
        self.AllLicensesView.setLayout(self.layout)

        self.LicenseLabel = QtWidgets.QLabel(AllLicenses)
        self.LicenseLabel.setGeometry(QtCore.QRect(210, 30, 251, 71))
        self.LicenseLabel.setObjectName("LicenseLabel")

        self.retranslateUiAll(AllLicenses)
        QtCore.QMetaObject.connectSlotsByName(AllLicenses)

    def retranslateUiAll(self, AllLicenses):
        _translate = QtCore.QCoreApplication.translate
        AllLicenses.setWindowTitle(_translate("AllLicenses", "All Licenses Status"))
        self.LicenseLabel.setText(_translate("AllLicenses", "<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; text-decoration: underline;\">All Licenses</span></p></body></html>"))

    def create_table(self):
        self.table = QtWidgets.QTableWidget(self.AllLicensesView)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Name', 'ID', 'Expiration Date'])
        hheader = self.table.horizontalHeader()
        hheader.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)

        rows = web3_interface.get_all_licences()
        print(rows)
        self.table.setRowCount(len(rows))
        row_num = 0
        for row in rows:
            print(row)
            print(row[0])
            print(row[1])
            print(row[2])
            self.table.setItem(row_num, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table.setItem(row_num, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.table.setItem(row_num, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            row_num += 1

        self.table.resizeColumnsToContents()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AllLicenses = QtWidgets.QWidget()
#     ui = Ui_AllLicenses()
#     ui.setupUi(AllLicenses)
#     AllLicenses.show()
#     sys.exit(app.exec_())
