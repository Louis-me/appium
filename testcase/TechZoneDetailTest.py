from Base.BaseRunner import ParametrizedTestCase
from PageObject.TechZoneDetailPage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TechZoneDetailTest(ParametrizedTestCase):

    def testTechZoneDetail(self):
        techZoneDetail = TechZoneDetail(driver=self.driver, path=PATH("../yaml/TechZoneDetail.yaml"))
        techZoneDetail.operate(logTest=self.logTest)
        techZoneDetail.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    # def testWrongPwd(self):
    #     pass

    def setUp(self):
        super(TechZoneDetailTest, self).setUp()

    def tearDown(self):
        super(TechZoneDetailTest, self).tearDown()