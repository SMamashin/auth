# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ProfileUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(451, 538)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(451, 538))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        MainWindow.setWindowOpacity(0.99)
        MainWindow.setStyleSheet("QWidget {\n"
"  background-color: rgba(255, 255, 255, 0.5); /* белый цвет с 50% прозрачностью */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(45)
        sizePolicy.setVerticalStretch(45)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("QWidget {\n"
"  background: url(:/background/3exXqXqqT4U.jpg);\n"
"  background-repeat: no-repeat;\n"
"  background-position: center;\n"
"  background-attachment: fixed;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    background: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background: none;\n"
"    background-color: rgb(198, 188, 255);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: none;\n"
"    background-color: rgb(170, 170, 255);\n"
"    border-radius: 20px;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(123, 123, 184);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(146, 148, 255);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(90, 90, 271, 61))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("font-size: 25px;\n"
"text-align: center;\n"
"position: center;\n"
"color: #fff;\n"
"background-color: #131313;\n"
"border-radius: 15px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 280, 271, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 490, 321, 31))
        self.label_2.setStyleSheet("font-size: 14px;\n"
"color: #fff;\n"
"background-color: #131313;\n"
"border-radius: 15px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 271, 31))
        self.label_3.setStyleSheet("font-size: 16px;\n"
"color: #fff;\n"
"background-color: #131313;\n"
"border-radius: 15px;\n"
"")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 200, 271, 31))
        self.label_4.setStyleSheet("font-size: 16px;\n"
"color: #fff;\n"
"background-color: #131313;\n"
"border-radius: 15px;\n"
"")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 240, 271, 31))
        self.label_5.setStyleSheet("font-size: 16px;\n"
"color: #fff;\n"
"background-color: #131313;\n"
"border-radius: 15px;\n"
"")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auth"))
        self.label.setText(_translate("MainWindow", "ПРОФИЛЬ"))
        self.pushButton.setText(_translate("MainWindow", "Выйти"))
        self.label_2.setText(_translate("MainWindow", "Mamashin Squad Industries. 2024 v1.2.0 build #4"))
import bg
