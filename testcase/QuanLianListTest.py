from Base.BaseRunner import ParametrizedTestCase
from PageObject.QuanLianListPage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class QuanLianListTest(ParametrizedTestCase):

    def testQuanLianList(self):
        quanList = QuanlianList(driver=self.driver, path=PATH("../yaml/QuanLianJieList.yaml"))
        quanList.operate(logTest=self.logTest)
        quanList.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    def setUp(self):
        super(QuanLianListTest, self).setUp()

    def tearDown(self):
        super(QuanLianListTest, self).tearDown()