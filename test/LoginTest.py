from Base.BaseRunner import ParametrizedTestCase
from PageObject.FirstOpenPage import FirstOpen
from PageObject.LoginPage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginTest(ParametrizedTestCase):

    def testLogin(self):
        login = Login(driver=self.driver, path=PATH("../yaml/login.yaml"))
        login.operate(logTest=self.logTest)
        login.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    # def testWrongPwd(self):
    #     pass

    def setUp(self):
        super(LoginTest, self).setUp()
