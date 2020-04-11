# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Dialog_setTTL.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_SetTTL(object):
    def setupUi(self, Dialog_SetTTL):
        Dialog_SetTTL.setObjectName("Dialog_SetTTL")
        Dialog_SetTTL.resize(543, 115)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_SetTTL)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog_SetTTL)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_ttl = QtWidgets.QLineEdit(Dialog_SetTTL)
        self.lineEdit_ttl.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_ttl.setObjectName("lineEdit_ttl")
        self.horizontalLayout_2.addWidget(self.lineEdit_ttl)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_SetTTL)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.pushButton_save = QtWidgets.QPushButton(Dialog_SetTTL)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_SetTTL)
        QtCore.QMetaObject.connectSlotsByName(Dialog_SetTTL)

    def retranslateUi(self, Dialog_SetTTL):
        _translate = QtCore.QCoreApplication.translate
        Dialog_SetTTL.setWindowTitle(_translate("Dialog_SetTTL", "Set Key TTL"))
        self.label_3.setText(_translate("Dialog_SetTTL", "New Key:"))
        self.pushButton_cancel.setText(_translate("Dialog_SetTTL", "Cancel"))
        self.pushButton_save.setText(_translate("Dialog_SetTTL", "Save"))
