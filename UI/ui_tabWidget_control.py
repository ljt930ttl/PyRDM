# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tabWidget_control.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Qwidget_control(object):
    def setupUi(self, Qwidget_control):
        Qwidget_control.setObjectName("Qwidget_control")
        Qwidget_control.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Qwidget_control)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_control = QtWidgets.QTabWidget(Qwidget_control)
        self.tabWidget_control.setMinimumSize(QtCore.QSize(200, 200))
        self.tabWidget_control.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_control.setObjectName("tabWidget_control")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.tabWidget_control.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget_control)

        self.retranslateUi(Qwidget_control)
        self.tabWidget_control.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Qwidget_control)

    def retranslateUi(self, Qwidget_control):
        _translate = QtCore.QCoreApplication.translate
        Qwidget_control.setWindowTitle(_translate("Qwidget_control", "Form"))
        self.tabWidget_control.setTabText(self.tabWidget_control.indexOf(self.tab), _translate("Qwidget_control", "log"))
