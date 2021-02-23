from PyQt5 import QtCore, QtGui, QtWidgets
from AddLicense import Addlicense
from GetLicense import Ui_GetLicense
from RenewLicense import Ui_RenewLicense
from AllLicenses import Ui_AllLicenses
from web3 import Web3
import BackGround

class BCgui():
    def openAddlicense(self):
        self.window=QtWidgets.QMainWindow()
        self.uiNew=Addlicense()
        self.uiNew.setupUiAL(self.window)
        self.window.show()

    def openGetLicense(self):
        self.window=QtWidgets.QMainWindow()
        self.uiNew=Ui_GetLicense()
        self.uiNew.setupUiGL(self.window)
        self.window.show()

    def openRenewLicense(self):
        self.window=QtWidgets.QMainWindow()
        self.uiNew=Ui_RenewLicense()
        self.uiNew.setupUiRL(self.window)
        self.window.show()

    def openAllLicenses(self):
        self.window=QtWidgets.QMainWindow()
        self.uiNew=Ui_AllLicenses()
        self.uiNew.setupUiAll(self.window)
        self.window.show()


    def setupUi(self, DriverLicense):
        DriverLicense.setObjectName("DriverLicense")
        DriverLicense.resize(785, 495)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setUnderline(True)
        DriverLicense.setFont(font)
        DriverLicense.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        DriverLicense.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Police.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DriverLicense.setWindowIcon(icon)
        DriverLicense.setIconSize(QtCore.QSize(10, 24))
        self.widget = QtWidgets.QWidget(DriverLicense)
        self.widget.setObjectName("widget")
        # -----ADD LICENSE BUTTON-----------------------------
        self.AddLicense = QtWidgets.QPushButton(self.widget)
        self.AddLicense.setGeometry(QtCore.QRect(0, 400, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.AddLicense.setFont(font)
        self.AddLicense.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddLicense.setCheckable(False)
        self.AddLicense.setChecked(False)
        self.AddLicense.setObjectName("AddLicense")
        self.AddLicense.clicked.connect(self.openAddlicense)
        #------------GET LICENSE BUTTON-----------------------
        self.GetLicenseStatus = QtWidgets.QPushButton(self.widget)
        self.GetLicenseStatus.setGeometry(QtCore.QRect(190, 400, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.GetLicenseStatus.setFont(font)
        self.GetLicenseStatus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GetLicenseStatus.setCheckable(False)
        self.GetLicenseStatus.setChecked(False)
        self.GetLicenseStatus.setObjectName("GetLicenseStatus")
        self.GetLicenseStatus.clicked.connect(self.openGetLicense)
        #---------------RENEW LICENSE BUTTON----------------------
        self.RenewLicense = QtWidgets.QPushButton(self.widget)
        self.RenewLicense.setGeometry(QtCore.QRect(380, 400, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.RenewLicense.setFont(font)
        self.RenewLicense.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RenewLicense.setCheckable(False)
        self.RenewLicense.setChecked(False)
        self.RenewLicense.setObjectName("RenewLicense")
        self.RenewLicense.clicked.connect(self.openRenewLicense)
        #-----------Show All Licenses Butten-------------------
        self.ShowAllLicenses = QtWidgets.QPushButton(self.widget)
        self.ShowAllLicenses.setGeometry(QtCore.QRect(590, 400, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setUnderline(True)
        self.ShowAllLicenses.setFont(font)
        self.ShowAllLicenses.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowAllLicenses.setCheckable(False)
        self.ShowAllLicenses.setChecked(False)
        self.ShowAllLicenses.setObjectName("ShowAllLicenses")
        self.BackGround_Police = QtWidgets.QLabel(self.widget)
        self.BackGround_Police.setGeometry(QtCore.QRect(0, 0, 801, 391))
        self.BackGround_Police.setStyleSheet("background-image: url(:/BackGround/ISRAEL POLICE.jpg);")
        self.BackGround_Police.setText("")
        self.BackGround_Police.setPixmap(QtGui.QPixmap(":/BackGround/ISRAEL POLICE.jpg"))
        self.BackGround_Police.setScaledContents(True)
        self.BackGround_Police.setObjectName("BackGround_Police")
        DriverLicense.setCentralWidget(self.widget)
        self.statusbar = QtWidgets.QStatusBar(DriverLicense)
        self.statusbar.setObjectName("statusbar")
        DriverLicense.setStatusBar(self.statusbar)

        self.retranslateUi(DriverLicense)
        QtCore.QMetaObject.connectSlotsByName(DriverLicense)
        self.ShowAllLicenses.clicked.connect(self.openAllLicenses)

    def retranslateUi(self, DriverLicense):
        _translate = QtCore.QCoreApplication.translate
        DriverLicense.setWindowTitle(_translate("DriverLicense", "Police Driver License Check"))
        self.AddLicense.setText(_translate("DriverLicense", "Add License"))
        self.GetLicenseStatus.setText(_translate("DriverLicense", "Get License"))
        self.RenewLicense.setText(_translate("DriverLicense", "Renew License"))
        self.ShowAllLicenses.setText(_translate("DriverLicense", "All Licenses"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DriverLicense = QtWidgets.QMainWindow()
    ui = BCgui()
    ui.setupUi(DriverLicense)
    DriverLicense.show()

    sys.exit(app.exec_())

