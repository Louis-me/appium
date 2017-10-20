import random

from Base.BaseAdb import AndroidDebugBridge

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


if __name__ == '__main__':
    import os
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    t = getYam(PATH("../yaml/test.yaml"))
    print(t)

    # port = str(random.randint(4700, 4900))
    # bpport = str(random.randint(4700, 4900))
    # devices = "DU2TAN15AJ049163"
    #
    # cmd1 = "appium --session-override  -p %s -bp %s -U %s" % (port, bpport, devices)
    # print(cmd1)
    # os.popen(cmd1)




