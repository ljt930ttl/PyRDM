#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/1 11:41
@Author:  linjinting
@File: tree_item.py
@Software: PyCharm
"""
# try:
#     import simpletreemodel_rc3
# except ImportError:
#     import simpletreemodel_rc2
import redis

class TreeItem(object):

    def __init__(self, data=None, parent=None, isDebug=True):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []

        # self.childIds = {}

        self.isDebug = isDebug

    def appendChild(self, item):
        self.childItems.append(item)

    def getAllChilds(self):
        return self.childItems

    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)

    def columnCount(self):
        ## 基本的tree 固定一列，
        # return len(self.itemData)
        return 1
    def data(self, column):
        try:
            # return (self.getItemName(),self.getItemId(),self.getItemUid(),self.getItemCode())[column]
            if isinstance(self.itemData,dict):
                value = self.itemData.get('name','NOT')
            else:
                value = self.itemData
            return value
        except IndexError:
            return None

    def parent(self):
        return self.parentItem

    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)

        return 0

    def itemdata(self):
        return self.itemData

    def remove(self, itme):
        # print(itme.itemData['bizOrgName'],self.childItems)
        if self.isDebug:
            print("remove itme",itme)
        self.childItems.remove(itme)