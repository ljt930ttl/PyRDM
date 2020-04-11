# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tabWidget_container.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
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
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.widget)
        self.tabWidget_container.addTab(self.tab, "")
        self.verticalLayout_4.addWidget(self.tabWidget_container)

        self.retranslateUi(tabWidgetContainer)
        self.tabWidget_container.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabWidgetContainer)

    def retranslateUi(self, tabWidgetContainer):
        _translate = QtCore.QCoreApplication.translate
        tabWidgetContainer.setWindowTitle(_translate("tabWidgetContainer", "Form"))
        self.textBrowser.setHtml(_translate("tabWidgetContainer", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:48pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600;\">Welcome</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">PyRDM-V0.1</span></p></body></html>"))
        self.tabWidget_container.setTabText(self.tabWidget_container.indexOf(self.tab), _translate("tabWidgetContainer", "Tab 1"))
