# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(705, 343)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonYes = QtWidgets.QPushButton(Form)
        self.pushButtonYes.setObjectName("pushButtonYes")
        self.gridLayout.addWidget(self.pushButtonYes, 1, 0, 1, 1)
        self.pushButtonNo = QtWidgets.QPushButton(Form)
        self.pushButtonNo.setObjectName("pushButtonNo")
        self.gridLayout.addWidget(self.pushButtonNo, 1, 1, 1, 1)
        self.questLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.questLabel.setFont(font)
        self.questLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.questLabel.setObjectName("questLabel")
        self.gridLayout.addWidget(self.questLabel, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonYes.setText(_translate("Form", "Да"))
        self.pushButtonNo.setText(_translate("Form", "Нет"))
        self.questLabel.setText(_translate("Form", "TextLabel"))
