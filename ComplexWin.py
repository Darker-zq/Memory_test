# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComplexWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ComplexWindow(object):
    def setupUi(self, ComplexWindow):
        ComplexWindow.setObjectName("ComplexWindow")
        ComplexWindow.resize(1123, 832)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        ComplexWindow.setFont(font)
        ComplexWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(ComplexWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(510, 40, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pbt_start1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_start1.setGeometry(QtCore.QRect(120, 710, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_start1.setFont(font)
        self.pbt_start1.setObjectName("pbt_start1")
        self.label_tips = QtWidgets.QLabel(self.centralwidget)
        self.label_tips.setGeometry(QtCore.QRect(850, 110, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tips.setFont(font)
        self.label_tips.setObjectName("label_tips")
        self.pbt_back1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_back1.setGeometry(QtCore.QRect(860, 710, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_back1.setFont(font)
        self.pbt_back1.setObjectName("pbt_back1")
        self.pbt_over1 = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_over1.setGeometry(QtCore.QRect(470, 710, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pbt_over1.setFont(font)
        self.pbt_over1.setObjectName("pbt_over1")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_1.setGeometry(QtCore.QRect(60, 100, 200, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_1.setFont(font)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(610, 110, 200, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(340, 300, 200, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(60, 500, 200, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(610, 500, 200, 171))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_tip1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip1_2.setGeometry(QtCore.QRect(850, 270, 271, 91))
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
        self.label_tip1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip1_3.setGeometry(QtCore.QRect(850, 180, 271, 91))
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
        self.label_tip1_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip1_4.setGeometry(QtCore.QRect(950, 490, 271, 41))
        self.label_tip1_4.setMinimumSize(QtCore.QSize(271, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip1_4.setFont(font)
        self.label_tip1_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_tip1_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_tip1_4.setWordWrap(True)
        self.label_tip1_4.setObjectName("label_tip1_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(900, 550, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        ComplexWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ComplexWindow)
        QtCore.QMetaObject.connectSlotsByName(ComplexWindow)

    def retranslateUi(self, ComplexWindow):
        _translate = QtCore.QCoreApplication.translate
        ComplexWindow.setWindowTitle(_translate("ComplexWindow", "MainWindow"))
        self.label_title.setText(_translate("ComplexWindow", "复杂测试"))
        self.pbt_start1.setText(_translate("ComplexWindow", "开始测试"))
        self.label_tips.setText(_translate("ComplexWindow", "注意："))
        self.pbt_back1.setText(_translate("ComplexWindow", "返回主界面"))
        self.pbt_over1.setText(_translate("ComplexWindow", "结束测试"))
        self.label_tip1_2.setText(_translate("ComplexWindow", "    2.点击【开始测试】按钮，开始测试，3秒后出现第一组数字，请您做好准备。"))
        self.label_tip1_3.setText(_translate("ComplexWindow", "    1.数字出现的频率是40次/分钟，每组的两个数字显示的间隔时间是0.15秒。"))
        self.label_tip1_4.setText(_translate("ComplexWindow", "输入框"))

