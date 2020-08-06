# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def ExitClicked(self):
        print("Program Exit")
        quit()

    # Error Popup - Not yet Implimented
    def popup_MissingFeature(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Feature Not Yet Implemented!")
        # msg.setIcon(QMessage)
        x = msg.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 584)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(395, 30, 381, 501))
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.popup_MissingFeature)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 151, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.popup_MissingFeature)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(lambda: self.popup_MissingFeature())

        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport.triggered.connect(lambda: self.popup_MissingFeature())

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setCheckable(False)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(lambda: self.ExitClicked())

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExport)

        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("BFRO Analyzer", "BFRO Analyzer"))
        self.pushButton.setText(_translate("MainWindow", "Download BFRO Data"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert BFRO Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

