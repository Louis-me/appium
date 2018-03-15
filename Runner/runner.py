# -*- coding: utf-8 -*-

__author__ = 'shikun'
import sys

sys.path.append("..")
import platform
from Base.BaseAndroidPhone import *
from Base.BaseAdb import *
from Base.BaseRunner import ParametrizedTestCase
from TestCase.HomeTest import HomeTest
from TestCase.ContactTest import ContactTest
from TestCase.CardsTest import CardsTest
from TestCase.MeTest import MeTest
from TestCase.HistoryTest import HistoryTest
from TestCase.TeamTest import TeamTest
from TestCase.TestWeiQunTest import TestWeiQunTest
from TestCase.OrderingUITest import OrderingUITest
from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import init, mk_file
from Base.BaseStatistics import countDate, writeExcel, countSumDevices
from Base.BasePickle import *
from datetime import datetime

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def kill_adb():
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill5037.bat"))
    else:
        os.popen("killall adb")
    os.system("adb start-server")

def runnerPool(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        print("----runnerPool------")
        print(getDevices[i])
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        # _initApp["platformVersion"] = "6.0"
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        #_initApp["appPackage"] = "com.huawei.works"
        _initApp["appPackage"] = "com.hp.marykay"
        #_initApp["appActivity"] = "huawei.w3.ui.welcome.W3SplashScreenActivity"
        _initApp["appActivity"] = "MaryKayActivity"
        _initApp["automationName"] = "Appium"
        #_initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = getDevices[i]["systemPort"]
        # _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        # _initApp["appActivity"] = apkInfo.getApkActivity()
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
    # suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(TestWeiQunTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(HistoryTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(ContactTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(MeTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(CardsTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(TeamTest, param=devices))
    suite.addTest(ParametrizedTestCase.parametrize(OrderingUITest, param=devices))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")

if __name__ == '__main__':

    kill_adb()

    devicess = AndroidDebugBridge().attached_devices()
    if len(devicess) > 0:
        mk_file()
        l_devices = []
        for dev in devicess:
            app = {}
            app["devices"] = dev
            init(dev)
            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["systemPort"] = str(random.randint(4700, 4900))
            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPool(l_devices)
        writeExcel()
        appium_server.stop_server(l_devices)
    else:
        print("没有可用的安卓设备")
