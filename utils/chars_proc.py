#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
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

class CodingChar:
    @staticmethod
    def codingString(value):
        try:
            new_value = value.decode()
            str_type = 'unicode'
        except Exception as e:
            # print(e)
            sp_value = str(value).split('\'')
            new_value = sp_value[1]
            str_type = 'binary'

        return (new_value, str_type)

    @staticmethod
    def recoverCodeing(value , type_):
        if value is None:
            return
        if type_ == 'binary':
            value_e = eval(repr(value).replace('\\\\', '\\'))
            new_value = value_e.encode()
        else:
            new_value = value
        return new_value


def formatJsonLoad(value):
    try:
        loads = json.loads(value)
        return json.dumps(loads, sort_keys=True, indent=4)
    except:
        return value