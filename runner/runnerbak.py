
# -*- coding: utf-8 -*-

__author__ = 'shikun'

import sys

sys.path.append("..")
import time
from Base.BaseAndroidPhone import *
from Base.BaseAdb import *
from Base.BaseRunner import ParametrizedTestCase
from TestCase.TechZoneListTest import TechZoneListTest
from TestCase.TechZoneDetailTest import TechZoneDetailTest
from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import init
from Base.BaseStatistics import countDate, writeExcel
from Base.BasePickle import *
from datetime import datetime
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def runnerPool(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        print("----runnerPool------")
        print(getDevices[i])
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = getDevices[i]["platformName"]
        _initApp["port"] = getDevices[i]["port"]
        _initApp["appPackage"] = getDevices[i]["appPackage"]
        _initApp["appActivity"] = getDevices[i]["appActivity"]
        # _initApp["app"] = getDevices[i]["app"]
        _pool.append(_initApp)
        devices_Pool.append(_initApp)
    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TechZoneListTest, param=devices))
    suite.addTest(ParametrizedTestCase.parametrize(TechZoneDetailTest, param=devices))
    # fp = open(PATH("../report/index.html"), "wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"自动化测试报告", description=u"用例执行情况")
    # runner.run(suite)
    # fp.close()
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")
if __name__ == '__main__':
    if AndroidDebugBridge().attached_devices():
        getDevices = init()
        appium_server = AppiumServer(getDevices)
        appium_server.start_server()
        while not appium_server.is_runnnig():
            time.sleep(2)
        runnerPool(getDevices)
        appium_server.stop_server()
        writeExcel()
    else:
        print(u"设备不存在")
