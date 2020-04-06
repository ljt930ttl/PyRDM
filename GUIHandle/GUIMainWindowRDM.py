#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/2 10:43
@Author:  linjinting
@File: GUIMainWindowRDM.py
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QAction


from UI.ui_main_PyRDM import Ui_MainWindow_PyRDM
from GUIHandle.GUITreeView_redis import RedisTreeView
from GUIHandle.GUIForm_container import FormContainer
from GUIHandle.GUIForm_control import FormControl
from GUIHandle.GUIDialog_connection import DiaogConneciton
from GUIHandle.communicate import bus

import global_config as g_config


class MainWindowRDM(QMainWindow, Ui_MainWindow_PyRDM):
    def __init__(self):
        super(MainWindowRDM,self).__init__()
        self.setupUi(self)
        self.widgets_init()
        self.initTreeView()
        self.initToolBar()

        self.__signal_init()

        self.mapServers = dict()


    def widgets_init(self):

        # 初始化显示 redis value相关tab部件
        self.tabWidgetContainer = FormContainer()
        self.verticalLayout_container.addWidget(self.tabWidgetContainer)
        self.tabWidgetContainer.show()

        # 初始化显示控制台相关tab部件
        self.tabWidgetControl = FormControl()
        self.verticalLayout_control.addWidget(self.tabWidgetControl)
        self.tabWidgetControl.show()

    def initTreeView(self):
        self.treeview_redis = RedisTreeView()
        # view.setWindowTitle("Simple Tree Model")
        self.verticalLayout_tree.addWidget(self.treeview_redis)
        self.treeview_redis.show()



        # self.treeview_redis.clicked.connect(self.clikedTreeItem)

    def initToolBar(self):
        connAct = QAction('Connection Redis Server', self)
        connAct.setShortcut('Ctrl+D')

        self.toolbar = self.addToolBar('Connection Redis Server')
        self.toolbar.addAction(connAct)
        connTest = QAction('test', self)
        connTest.setShortcut('Ctrl+Z')
        self.toolbar.addAction(connTest)
        connTest.triggered.connect(self.tabWidgetContainer.initKeyContainer)
        connAct.triggered.connect(self.showConnectionDialog)

    def __signal_init(self):
        pass
        # bus.createServerItem.connect(self.treeview_redis.createServerItem)

    def showConnectionDialog(self):

        # 初始化显示控制台相关qdialog部件
        dialog_conn = DiaogConneciton()
        dialog_conn.exec_()
        # rInfo = dialog_conn.sendredisConnInfo()
        dialog_conn.destroy()
        bus.createServerItem.emit(g_config.rdm_config)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindowRDM()
    window.show()
    sys.exit(app.exec_())

    # import get_data
    #
    # data = get_data.get_all_keys()