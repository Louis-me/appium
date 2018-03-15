# -*- coding: UTF-8 -*-
from PageObject.Login.LoginPage import LoginPage
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OrderingUITest(ParametrizedTestCase):
    # 登陆
    def testLogin(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/Login/LoginTest.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = LoginPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(OrderingUITest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(OrderingUITest, cls).tearDownClass()
