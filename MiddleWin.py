# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MiddleWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MiddleWindow(object):
    def setupUi(self, MiddleWindow):
        MiddleWindow.setObjectName("MiddleWindow")
        MiddleWindow.resize(844, 593)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        MiddleWindow.setFont(font)
        MiddleWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MiddleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_left = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_left.setGeometry(QtCore.QRect(70, 110, 200, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_left.setFont(font)
        self.textBrowser_left.setObjectName("textBrowser_left")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(360, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.textBrowser_right = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_right.setGeometry(QtCore.QRect(380, 120, 200, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_right.setFont(font)
        self.textBrowser_right.setObjectName("textBrowser_right")
        self.pbt_start1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_start1.setGeometry(QtCore.QRect(120, 500, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_start1.setFont(font)
        self.pbt_start1.setObjectName("pbt_start1")
        self.label_tip1 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip1.setGeometry(QtCore.QRect(50, 350, 731, 61))
        self.label_tip1.setMinimumSize(QtCore.QSize(271, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip1.setFont(font)
        self.label_tip1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_tip1.setTextFormat(QtCore.Qt.PlainText)
        self.label_tip1.setWordWrap(True)
        self.label_tip1.setObjectName("label_tip1")
        self.label_tips = QtWidgets.QLabel(self.centralwidget)
        self.label_tips.setGeometry(QtCore.QRect(30, 300, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tips.setFont(font)
        self.label_tips.setObjectName("label_tips")
        self.pbt_back1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_back1.setGeometry(QtCore.QRect(590, 500, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_back1.setFont(font)
        self.pbt_back1.setObjectName("pbt_back1")
        self.pbt_over1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_over1.setGeometry(QtCore.QRect(360, 500, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_over1.setFont(font)
        self.pbt_over1.setObjectName("pbt_over1")
        self.label_tip1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip1_2.setGeometry(QtCore.QRect(90, 400, 731, 61))
        self.label_tip1_2.setMinimumSize(QtCore.QSize(271, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip1_2.setFont(font)
        self.label_tip1_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_tip1_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_tip1_2.setWordWrap(True)
        self.label_tip1_2.setObjectName("label_tip1_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 170, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(660, 170, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_tip1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip1_3.setGeometry(QtCore.QRect(700, 110, 271, 41))
        self.label_tip1_3.setMinimumSize(QtCore.QSize(271, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip1_3.setFont(font)
        self.label_tip1_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_tip1_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_tip1_3.setWordWrap(True)
        self.label_tip1_3.setObjectName("label_tip1_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 170, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MiddleWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MiddleWindow)
        QtCore.QMetaObject.connectSlotsByName(MiddleWindow)

    def retranslateUi(self, MiddleWindow):
        _translate = QtCore.QCoreApplication.translate
        MiddleWindow.setWindowTitle(_translate("MiddleWindow", "MainWindow"))
        self.label_title.setText(_translate("MiddleWindow", "中等测试"))
        self.textBrowser_right.setHtml(_translate("MiddleWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:100pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:80pt;\"><br /></p></body></html>"))
        self.pbt_start1.setText(_translate("MiddleWindow", "开始测试"))
        self.label_tip1.setText(_translate("MiddleWindow", "    1.数字出现的频率是30次/分钟，每组的两个数字显示的间隔时间是0.25秒。"))
        self.label_tips.setText(_translate("MiddleWindow", "注意："))
        self.pbt_back1.setText(_translate("MiddleWindow", "返回主界面"))
        self.pbt_over1.setText(_translate("MiddleWindow", "结束测试"))
        self.label_tip1_2.setText(_translate("MiddleWindow", "2.点击【开始测试】按钮，开始测试，3秒后出现第一组数字，请您做好准备。"))
        self.label.setText(_translate("MiddleWindow", "+"))
        self.label_tip1_3.setText(_translate("MiddleWindow", "输入框"))
        self.label_3.setText(_translate("MiddleWindow", "="))

