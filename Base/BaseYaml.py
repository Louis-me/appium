__author__ = 'shikun'
import yaml

# -*- coding:utf-8 -*-
def getYam(path):
    try:
        with open(path, encoding='utf-8') as f:
            x = yaml.load(f)
            print(x)
            return x
    except FileNotFoundError:
        print(u"找不到文件")


