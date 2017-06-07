from Base.BaseRunner import ParametrizedTestCase
from PageObject.WritePage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class WriteTest(ParametrizedTestCase):
    def testWrite(self):
        write = Write(driver=self.driver, path=PATH("../yaml/write.yaml"))
        write.operate(self.logTest)
        write.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    def setUp(self):
        super(WriteTest, self).setUp()

    def tearDown(self):
        self.driver.close()
