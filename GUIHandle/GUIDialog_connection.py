#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/2 14:32
@Author:  linjinting
@File: GUIDialog_connection.py
@Software: PyCharm
"""

from PyQt5.QtWidgets import QDialog
from UI.ui_Dialog_connection import Ui_DialogConnection
import global_config as g_config
from GUIHandle.communicate import bus

class DiaogConneciton(QDialog, Ui_DialogConnection):
    def __init__(self):
        super(DiaogConneciton,self).__init__()
        self.setupUi(self)
        self.init_signal()

    def init_signal(self):
        self.pushButton_ok.clicked.connect(self.clickOK)
        self.pushButton_cancel.clicked.connect(self.clickCancel)

        # self.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),self, QtCore.SLOT("accept()"))


    def clickOK(self):
        m_name = self.lineEdit_name.text()
        m_host = self.lineEdit_host.text()
        m_auth = self.lineEdit_auth.text()
        m_port = self.spinBox_port.value()
        g_config.redisConfig(name=m_name, host=m_host, port=m_port, password=m_auth)
        # self.rCI = redisConnInfo.redisConnInfo()
        # self.rCI.setdInfo(name=m_sname ,host=m_shost, port=m_iport, password=m_sauth)
        bus.createServerItem.emit(g_config.rdm_config)
        self.close()

    def sendredisConnInfo(self):
        if self.rCI == None:
            return None
        return self.rCI
        # self.close()

    def clickCancel(self):
        self.close()

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    form = DiaogConneciton()
    form.show()
    sys.exit(app.exec_())