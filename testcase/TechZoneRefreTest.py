from Base.BaseRunner import ParametrizedTestCase
from PageObject.TechZoneRefrePage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TechZoneRefreTest(ParametrizedTestCase):

    def testTechZoneRefre(self):
        techZoneRefre = TechZoneRefre(driver=self.driver, path=PATH("../yaml/TechZoneRefre.yaml"))
        techZoneRefre.operate(logTest=self.logTest)
        techZoneRefre.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    def setUp(self):
        super(TechZoneRefreTest, self).setUp()

    def tearDown(self):
        super(TechZoneRefreTest, self).tearDown()