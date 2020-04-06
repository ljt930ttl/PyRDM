# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Dialog_connection.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogConnection(object):
    def setupUi(self, DialogConnection):
        DialogConnection.setObjectName("DialogConnection")
        DialogConnection.resize(363, 348)
        DialogConnection.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogConnection)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(DialogConnection)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(35)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_name = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_host = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_host.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.gridLayout.addWidget(self.lineEdit_host, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.spinBox_port = QtWidgets.QSpinBox(self.tab)
        self.spinBox_port.setMinimumSize(QtCore.QSize(0, 25))
        self.spinBox_port.setMaximum(65535)
        self.spinBox_port.setProperty("value", 6379)
        self.spinBox_port.setObjectName("spinBox_port")
        self.gridLayout.addWidget(self.spinBox_port, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_auth = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_auth.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_auth.setObjectName("lineEdit_auth")
        self.gridLayout.addWidget(self.lineEdit_auth, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_testconnection = QtWidgets.QPushButton(DialogConnection)
        self.pushButton_testconnection.setObjectName("pushButton_testconnection")
        self.horizontalLayout.addWidget(self.pushButton_testconnection)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_ok = QtWidgets.QPushButton(DialogConnection)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(DialogConnection)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogConnection)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DialogConnection)

    def retranslateUi(self, DialogConnection):
        _translate = QtCore.QCoreApplication.translate
        DialogConnection.setWindowTitle(_translate("DialogConnection", "Dialog"))
        self.label.setText(_translate("DialogConnection", "Name:"))
        self.label_2.setText(_translate("DialogConnection", "Host:"))
        self.lineEdit_host.setText(_translate("DialogConnection", "127.0.0.1"))
        self.label_4.setText(_translate("DialogConnection", "Port:"))
        self.label_3.setText(_translate("DialogConnection", "Auth:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DialogConnection", "Connection"))
        self.pushButton_testconnection.setText(_translate("DialogConnection", "Test Connection"))
        self.pushButton_ok.setText(_translate("DialogConnection", "OK"))
        self.pushButton_cancel.setText(_translate("DialogConnection", "Cancel"))
