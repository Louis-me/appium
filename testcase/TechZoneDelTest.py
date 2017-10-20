from Base.BaseRunner import ParametrizedTestCase
from PageObject.TechZoneDelPage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TechZoneDelTest(ParametrizedTestCase):

    def testTechZoneDel(self):
        techZoneDel = TechZoneDel(driver=self.driver, path=PATH("../yaml/TechZoneDel.yaml"))
        techZoneDel.operate(logTest=self.logTest)
        techZoneDel.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    def setUp(self):
        super(TechZoneDelTest, self).setUp()

    def tearDown(self):
        super(TechZoneDelTest, self).tearDown()