# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SimpleWindow(object):
    def setupUi(self, SimpleWindow):
        SimpleWindow.setObjectName("SimpleWindow")
        SimpleWindow.resize(844, 595)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        SimpleWindow.setFont(font)
        SimpleWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(SimpleWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_left = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_left.setGeometry(QtCore.QRect(50, 110, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(80)
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
        self.textBrowser_right.setGeometry(QtCore.QRect(360, 110, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(80)
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
        self.lable_plus = QtWidgets.QLabel(self.centralwidget)
        self.lable_plus.setGeometry(QtCore.QRect(290, 190, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.lable_plus.setFont(font)
        self.lable_plus.setObjectName("lable_plus")
        self.label_equal = QtWidgets.QLabel(self.centralwidget)
        self.label_equal.setGeometry(QtCore.QRect(590, 190, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.label_equal.setFont(font)
        self.label_equal.setObjectName("label_equal")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(640, 180, 161, 71))
        self.textEdit.setObjectName("textEdit")
        self.label_tip1 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip1.setGeometry(QtCore.QRect(50, 370, 731, 61))
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
        self.label_tips.setGeometry(QtCore.QRect(30, 320, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_tips.setFont(font)
        self.label_tips.setObjectName("label_tips")
        self.label_tip2 = QtWidgets.QLabel(self.centralwidget)
        self.label_tip2.setGeometry(QtCore.QRect(50, 430, 731, 61))
        self.label_tip2.setMinimumSize(QtCore.QSize(271, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_tip2.setFont(font)
        self.label_tip2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_tip2.setTextFormat(QtCore.Qt.PlainText)
        self.label_tip2.setWordWrap(True)
        self.label_tip2.setObjectName("label_tip2")
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
        SimpleWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SimpleWindow)
        QtCore.QMetaObject.connectSlotsByName(SimpleWindow)

    def retranslateUi(self, SimpleWindow):
        _translate = QtCore.QCoreApplication.translate
        SimpleWindow.setWindowTitle(_translate("SimpleWindow", "MainWindow"))
        self.textBrowser_left.setHtml(_translate("SimpleWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:80pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_title.setText(_translate("SimpleWindow", "简单测试"))
        self.textBrowser_right.setHtml(_translate("SimpleWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:80pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pbt_start1.setText(_translate("SimpleWindow", "开始测试"))
        self.lable_plus.setText(_translate("SimpleWindow", "+"))
        self.label_equal.setText(_translate("SimpleWindow", "="))
        self.label_tip1.setText(_translate("SimpleWindow", "    数字出现的频率是20次/分钟，每组数字显示时间为0.5秒，给您2.5秒计算和填写的时间。即每3秒计算一组数字。"))
        self.label_tips.setText(_translate("SimpleWindow", "注意："))
        self.label_tip2.setText(_translate("SimpleWindow", "    点击开始后，5秒后出现第一组数字，请保证鼠标光标放在右侧的输入栏中。"))
        self.pbt_back1.setText(_translate("SimpleWindow", "返回主界面"))
        self.pbt_over1.setText(_translate("SimpleWindow", "结束测试"))


    def handle_click(self):
        if not self.isVisible():
            self.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_SimpleWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())