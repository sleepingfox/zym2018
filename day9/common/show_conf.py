__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import configparser
from etc import setting
def show_conf():
    config = configparser.ConfigParser()
    config.read(setting.CONF_PATH)
    res = config.sections()

    for i in res:
        print(i)
        item_list = config.items(i)
        print(item_list)
