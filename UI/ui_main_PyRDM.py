# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_PyRDM.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_PyRDM(object):
    def setupUi(self, MainWindow_PyRDM):
        MainWindow_PyRDM.setObjectName("MainWindow_PyRDM")
        MainWindow_PyRDM.resize(926, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow_PyRDM)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setLineWidth(0)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(1)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_tree = QtWidgets.QVBoxLayout()
        self.verticalLayout_tree.setSpacing(0)
        self.verticalLayout_tree.setObjectName("verticalLayout_tree")
        self.verticalLayout.addLayout(self.verticalLayout_tree)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setMinimumSize(QtCore.QSize(500, 0))
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(1)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_container = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_container.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_container.setSpacing(0)
        self.verticalLayout_container.setObjectName("verticalLayout_container")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_control = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_control.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_control.setSpacing(0)
        self.verticalLayout_control.setObjectName("verticalLayout_control")
        self.verticalLayout_2.addWidget(self.splitter_2)
        MainWindow_PyRDM.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_PyRDM)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_PyRDM)

    def retranslateUi(self, MainWindow_PyRDM):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_PyRDM.setWindowTitle(_translate("MainWindow_PyRDM", "PyRDM"))
