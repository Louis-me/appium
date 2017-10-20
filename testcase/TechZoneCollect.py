from Base.BaseRunner import ParametrizedTestCase
from PageObject.TechZoneCollectPage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TechZoneCollectTest(ParametrizedTestCase):

    def testTechZoneCollect(self):
        page = TechZoneCollect(driver=self.driver, path=PATH("../yaml/TechZoneCollect.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    def setUp(self):
        super(TechZoneCollectTest, self).setUp()

    def tearDown(self):
        super(TechZoneCollectTest, self).tearDown()