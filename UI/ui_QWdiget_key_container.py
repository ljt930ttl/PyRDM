# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_QWdiget_key_container.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QWidget_key_container(object):
    def setupUi(self, QWidget_key_container):
        QWidget_key_container.setObjectName("QWidget_key_container")
        QWidget_key_container.resize(976, 679)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(QWidget_key_container)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtWidgets.QSplitter(QWidget_key_container)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_title = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_title.sizePolicy().hasHeightForWidth())
        self.widget_title.setSizePolicy(sizePolicy)
        self.widget_title.setObjectName("widget_title")
        self.horizontalLayout_title = QtWidgets.QHBoxLayout(self.widget_title)
        self.horizontalLayout_title.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_title.setObjectName("horizontalLayout_title")
        self.label_keyType = QtWidgets.QLabel(self.widget_title)
        self.label_keyType.setObjectName("label_keyType")
        self.horizontalLayout_title.addWidget(self.label_keyType)
        self.lineEdit_keyTitle = QtWidgets.QLineEdit(self.widget_title)
        self.lineEdit_keyTitle.setObjectName("lineEdit_keyTitle")
        self.horizontalLayout_title.addWidget(self.lineEdit_keyTitle)
        self.label_fieldCount = QtWidgets.QLabel(self.widget_title)
        self.label_fieldCount.setObjectName("label_fieldCount")
        self.horizontalLayout_title.addWidget(self.label_fieldCount)
        self.label_TTL = QtWidgets.QLabel(self.widget_title)
        self.label_TTL.setObjectName("label_TTL")
        self.horizontalLayout_title.addWidget(self.label_TTL)
        self.pushButton_rebaneKey = QtWidgets.QPushButton(self.widget_title)
        self.pushButton_rebaneKey.setObjectName("pushButton_rebaneKey")
        self.horizontalLayout_title.addWidget(self.pushButton_rebaneKey)
        self.pushButton_deleteKey = QtWidgets.QPushButton(self.widget_title)
        self.pushButton_deleteKey.setObjectName("pushButton_deleteKey")
        self.horizontalLayout_title.addWidget(self.pushButton_deleteKey)
        self.pushButton_setTTL = QtWidgets.QPushButton(self.widget_title)
        self.pushButton_setTTL.setObjectName("pushButton_setTTL")
        self.horizontalLayout_title.addWidget(self.pushButton_setTTL)
        self.verticalLayout_3.addWidget(self.widget_title)
        self.widget_table_operation = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_table_operation.sizePolicy().hasHeightForWidth())
        self.widget_table_operation.setSizePolicy(sizePolicy)
        self.widget_table_operation.setObjectName("widget_table_operation")
        self.gridLayout_table = QtWidgets.QGridLayout(self.widget_table_operation)
        self.gridLayout_table.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_table.setObjectName("gridLayout_table")
        self.tableWidget_values = QtWidgets.QTableWidget(self.widget_table_operation)
        self.tableWidget_values.setMinimumSize(QtCore.QSize(0, 100))
        self.tableWidget_values.setObjectName("tableWidget_values")
        self.tableWidget_values.setColumnCount(0)
        self.tableWidget_values.setRowCount(0)
        self.gridLayout_table.addWidget(self.tableWidget_values, 0, 0, 6, 1)
        self.pushButton_addRow = QtWidgets.QPushButton(self.widget_table_operation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_addRow.sizePolicy().hasHeightForWidth())
        self.pushButton_addRow.setSizePolicy(sizePolicy)
        self.pushButton_addRow.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_addRow.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_addRow.setObjectName("pushButton_addRow")
        self.gridLayout_table.addWidget(self.pushButton_addRow, 0, 1, 1, 2)
        self.pushButton_deleteRow = QtWidgets.QPushButton(self.widget_table_operation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_deleteRow.sizePolicy().hasHeightForWidth())
        self.pushButton_deleteRow.setSizePolicy(sizePolicy)
        self.pushButton_deleteRow.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_deleteRow.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_deleteRow.setObjectName("pushButton_deleteRow")
        self.gridLayout_table.addWidget(self.pushButton_deleteRow, 1, 1, 1, 2)
        self.pushButton_reload_value = QtWidgets.QPushButton(self.widget_table_operation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reload_value.sizePolicy().hasHeightForWidth())
        self.pushButton_reload_value.setSizePolicy(sizePolicy)
        self.pushButton_reload_value.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_reload_value.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_reload_value.setObjectName("pushButton_reload_value")
        self.gridLayout_table.addWidget(self.pushButton_reload_value, 2, 1, 1, 2)
        self.lineEdit_search = QtWidgets.QLineEdit(self.widget_table_operation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_search.sizePolicy().hasHeightForWidth())
        self.lineEdit_search.setSizePolicy(sizePolicy)
        self.lineEdit_search.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_search.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.gridLayout_table.addWidget(self.lineEdit_search, 3, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_table.addItem(spacerItem, 4, 1, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_table_operation)
        self.pushButton_2.setMaximumSize(QtCore.QSize(48, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_table.addWidget(self.pushButton_2, 5, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_table_operation)
        self.pushButton.setMaximumSize(QtCore.QSize(48, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_table.addWidget(self.pushButton, 5, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.widget_table_operation)
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_View_Field = QtWidgets.QWidget(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_View_Field.sizePolicy().hasHeightForWidth())
        self.widget_View_Field.setSizePolicy(sizePolicy)
        self.widget_View_Field.setObjectName("widget_View_Field")
        self.verticalLayout_field = QtWidgets.QVBoxLayout(self.widget_View_Field)
        self.verticalLayout_field.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_field.setObjectName("verticalLayout_field")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_feild = QtWidgets.QLabel(self.widget_View_Field)
        self.label_feild.setMinimumSize(QtCore.QSize(20, 0))
        self.label_feild.setObjectName("label_feild")
        self.horizontalLayout_3.addWidget(self.label_feild)
        self.label_fieldSize = QtWidgets.QLabel(self.widget_View_Field)
        self.label_fieldSize.setText("")
        self.label_fieldSize.setObjectName("label_fieldSize")
        self.horizontalLayout_3.addWidget(self.label_fieldSize)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.widget_View_Field)
        self.label_5.setMinimumSize(QtCore.QSize(20, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.comboBox_Viewas_Field = QtWidgets.QComboBox(self.widget_View_Field)
        self.comboBox_Viewas_Field.setObjectName("comboBox_Viewas_Field")
        self.comboBox_Viewas_Field.addItem("")
        self.comboBox_Viewas_Field.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_Viewas_Field)
        self.verticalLayout_field.addLayout(self.horizontalLayout_3)
        self.textEdit_key = QtWidgets.QTextEdit(self.widget_View_Field)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_key.sizePolicy().hasHeightForWidth())
        self.textEdit_key.setSizePolicy(sizePolicy)
        self.textEdit_key.setMinimumSize(QtCore.QSize(0, 50))
        self.textEdit_key.setMaximumSize(QtCore.QSize(16777215, 80))
        self.textEdit_key.setObjectName("textEdit_key")
        self.verticalLayout_field.addWidget(self.textEdit_key)
        self.verticalLayout.addWidget(self.widget_View_Field)
        self.widget_value = QtWidgets.QWidget(self.widget1)
        self.widget_value.setObjectName("widget_value")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_value)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_view_value = QtWidgets.QHBoxLayout()
        self.horizontalLayout_view_value.setObjectName("horizontalLayout_view_value")
        self.label_value = QtWidgets.QLabel(self.widget_value)
        self.label_value.setMinimumSize(QtCore.QSize(20, 0))
        self.label_value.setObjectName("label_value")
        self.horizontalLayout_view_value.addWidget(self.label_value)
        self.label_valueSize = QtWidgets.QLabel(self.widget_value)
        self.label_valueSize.setText("")
        self.label_valueSize.setObjectName("label_valueSize")
        self.horizontalLayout_view_value.addWidget(self.label_valueSize)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_view_value.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(self.widget_value)
        self.label_6.setMinimumSize(QtCore.QSize(20, 0))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_view_value.addWidget(self.label_6)
        self.comboBox_View_Value = QtWidgets.QComboBox(self.widget_value)
        self.comboBox_View_Value.setObjectName("comboBox_View_Value")
        self.comboBox_View_Value.addItem("")
        self.comboBox_View_Value.addItem("")
        self.horizontalLayout_view_value.addWidget(self.comboBox_View_Value)
        self.verticalLayout_2.addLayout(self.horizontalLayout_view_value)
        self.textEdit_value = QtWidgets.QTextEdit(self.widget_value)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_value.sizePolicy().hasHeightForWidth())
        self.textEdit_value.setSizePolicy(sizePolicy)
        self.textEdit_value.setMinimumSize(QtCore.QSize(0, 50))
        self.textEdit_value.setObjectName("textEdit_value")
        self.verticalLayout_2.addWidget(self.textEdit_value)
        self.horizontalLayout_save = QtWidgets.QHBoxLayout()
        self.horizontalLayout_save.setObjectName("horizontalLayout_save")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_save.addItem(spacerItem3)
        self.pushButton_save = QtWidgets.QPushButton(self.widget_value)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_save.addWidget(self.pushButton_save)
        self.verticalLayout_2.addLayout(self.horizontalLayout_save)
        self.verticalLayout.addWidget(self.widget_value)
        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(QWidget_key_container)
        QtCore.QMetaObject.connectSlotsByName(QWidget_key_container)
        QWidget_key_container.setTabOrder(self.pushButton_deleteRow, self.pushButton_rebaneKey)
        QWidget_key_container.setTabOrder(self.pushButton_rebaneKey, self.pushButton_deleteKey)
        QWidget_key_container.setTabOrder(self.pushButton_deleteKey, self.pushButton_setTTL)
        QWidget_key_container.setTabOrder(self.pushButton_setTTL, self.tableWidget_values)
        QWidget_key_container.setTabOrder(self.tableWidget_values, self.pushButton)
        QWidget_key_container.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget_key_container.setTabOrder(self.pushButton_2, self.lineEdit_search)
        QWidget_key_container.setTabOrder(self.lineEdit_search, self.pushButton_addRow)
        QWidget_key_container.setTabOrder(self.pushButton_addRow, self.pushButton_reload_value)
        QWidget_key_container.setTabOrder(self.pushButton_reload_value, self.lineEdit_keyTitle)

    def retranslateUi(self, QWidget_key_container):
        _translate = QtCore.QCoreApplication.translate
        QWidget_key_container.setWindowTitle(_translate("QWidget_key_container", "Form"))
        self.label_keyType.setText(_translate("QWidget_key_container", "___:"))
        self.label_fieldCount.setText(_translate("QWidget_key_container", "Size:"))
        self.label_TTL.setText(_translate("QWidget_key_container", "TTL:"))
        self.pushButton_rebaneKey.setText(_translate("QWidget_key_container", "Rename"))
        self.pushButton_deleteKey.setText(_translate("QWidget_key_container", "Delete"))
        self.pushButton_setTTL.setText(_translate("QWidget_key_container", "Set TTL"))
        self.pushButton_addRow.setText(_translate("QWidget_key_container", "Add row"))
        self.pushButton_deleteRow.setText(_translate("QWidget_key_container", "Delete row"))
        self.pushButton_reload_value.setText(_translate("QWidget_key_container", "Reload Value"))
        self.pushButton_2.setText(_translate("QWidget_key_container", "<"))
        self.pushButton.setText(_translate("QWidget_key_container", ">"))
        self.label_feild.setText(_translate("QWidget_key_container", "Key:  "))
        self.label_5.setText(_translate("QWidget_key_container", "View as:"))
        self.comboBox_Viewas_Field.setItemText(0, _translate("QWidget_key_container", "Plain Text"))
        self.comboBox_Viewas_Field.setItemText(1, _translate("QWidget_key_container", "Json"))
        self.textEdit_key.setHtml(_translate("QWidget_key_container", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_value.setText(_translate("QWidget_key_container", "Value:  "))
        self.label_6.setText(_translate("QWidget_key_container", "View as:"))
        self.comboBox_View_Value.setItemText(0, _translate("QWidget_key_container", "Plain Text"))
        self.comboBox_View_Value.setItemText(1, _translate("QWidget_key_container", "Json"))
        self.pushButton_save.setText(_translate("QWidget_key_container", "save"))
