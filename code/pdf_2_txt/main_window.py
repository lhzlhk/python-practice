# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(380, 398)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnOpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFile.setGeometry(QtCore.QRect(90, 200, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnOpenFile.setFont(font)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.lblConverter = QtWidgets.QLabel(self.centralwidget)
        self.lblConverter.setGeometry(QtCore.QRect(30, 30, 391, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblConverter.setFont(font)
        self.lblConverter.setObjectName("lblConverter")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 30))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "PDF 转 TXT"))
        self.btnOpenFile.setText(_translate("mainWindow", "打开文件"))
        self.lblConverter.setText(_translate("mainWindow", "PDF 转 TXT 工具"))

