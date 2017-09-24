from Base.BaseRunner import ParametrizedTestCase
from PageObject.TechZoneListPage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TechZoneListTest(ParametrizedTestCase):

    def testTechZoneList(self):
        techZoneList = TechZoneList(driver=self.driver, path=PATH("../yaml/TechZoneList.yaml"))
        techZoneList.operate(logTest=self.logTest)
        techZoneList.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    # def testWrongPwd(self):
    #     pass

    def setUp(self):
        super(TechZoneListTest, self).setUp()

    def tearDown(self):
        super(TechZoneListTest, self).tearDown()