# -*- coding: utf-8 -*-
from Base.BaseAppiumServer import AppiumServer
from Base.BaseLog import myLog
import unittest
from appium import webdriver
import os
import time
from Base.BaseYaml import getYam
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def appium_testcase(devices):

    desired_caps = {}
    desired_caps['platformName'] = devices["platformName"]
    desired_caps['platformVersion'] = devices["platformVersion"]
    desired_caps['deviceName'] = devices["deviceName"]
    desired_caps['appPackage'] = devices["appPackage"]
    desired_caps['appActivity'] = devices["appActivity"]
    desired_caps['udid'] = devices["deviceName"]

    desired_caps["noReset"] = "True"
    desired_caps['noSign'] = "True"
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    desired_caps["recreateChromeDriverSessions"] = "True"
    # 解决多次切换到webview报错问题，每次切换到非chrome-Driver时kill掉session 注意这个设置在appium 1.5版本上才做了处理
    desired_caps["automationName"] = "uiautomator2"
    # desired_caps['app'] = devices["app"]
    remote = "http://127.0.0.1:" + str(devices["port"]) + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    return driver


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should  
        inherit from this class.  
    """
    devices = None

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        global devices
        devices = param

    @classmethod
    def setUpClass(cls):
        cls.driver = appium_testcase(devices)
        cls.devicesName = devices["deviceName"]
        cls.logTest = myLog().getLog(cls.devicesName)  # 每个设备实例化一个日志记录器

    def setUp(self):
        pass
        # self.driver = appium_testcase(self.devices)
        # self.logTest = myLog().getLog(self.devices["deviceName"]) # 每个设备实例化一个日志记录器

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        # self.driver.quit()
        pass

    @staticmethod
    def parametrize(testcase_klass, param=None):
        # print("---parametrize-----")
        # print(param)
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite

