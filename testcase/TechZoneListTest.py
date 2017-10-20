from Base.BaseRunner import ParametrizedTestCase
from PageObject.TechZoneListPage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TechZoneListTest(ParametrizedTestCase):

    def testTechZoneList(self):
        techZoneList = TechZoneList(driver=self.driver, path=PATH("../yaml/TechZoneList.yaml")) # 调用测试用例yaml
        techZoneList.operate(logTest=self.logTest) # 调用page层中的用例执行
        techZoneList.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest,
                                devices=self.devices["deviceName"])# 调用page层的用例检查点

    def setUp(self):
        super(TechZoneListTest, self).setUp()

    '''
    用例结束后，关闭app
    '''
    def tearDown(self):
        super(TechZoneListTest, self).tearDown()