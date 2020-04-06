# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tabWidget_container.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tabWidgetContainer(object):
    def setupUi(self, tabWidgetContainer):
        tabWidgetContainer.setObjectName("tabWidgetContainer")
        tabWidgetContainer.resize(1091, 817)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(tabWidgetContainer)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget_container = QtWidgets.QTabWidget(tabWidgetContainer)
        self.tabWidget_container.setMinimumSize(QtCore.QSize(200, 300))
        self.tabWidget_container.setObjectName("tabWidget_container")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.widget)
        self.tabWidget_container.addTab(self.tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget_container)

        self.retranslateUi(tabWidgetContainer)
        self.tabWidget_container.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabWidgetContainer)

    def retranslateUi(self, tabWidgetContainer):
        _translate = QtCore.QCoreApplication.translate
        tabWidgetContainer.setWindowTitle(_translate("tabWidgetContainer", "Form"))
        self.label.setText(_translate("tabWidgetContainer", "welcome"))
        self.tabWidget_container.setTabText(self.tabWidget_container.indexOf(self.tab), _translate("tabWidgetContainer", "Tab 1"))
