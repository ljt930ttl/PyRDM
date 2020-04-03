#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class ldata_split:
    def __init__(self, line):
        self.line = line

    def split_ldata(self):
        # 用 “空格”，“：” 分割逻辑表达式，分别为 设备编号，动作，表达式
        line1 = self.line.split(" ")
        line2 = line1[1].split(":")
        device = line1[0]
        action = line2[0]
        wfldata = line2[1]
        return device, action, wfldata

    def split_station(self):
        # 用 # 分割站名，站号
        line_name = self.line.split("#")
        station_name = line_name[0]
        station_num = line_name[1]
        # station = {station_num: station_name}
        return station_num


class RedisNamespaceSplit:

    @staticmethod
    def split_namespace(namespace, separator=":"):
        if namespace == "":
            return None
        name_list = namespace.split(separator, 1)
        return name_list
