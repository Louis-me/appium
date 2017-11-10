import os
from Base.BaseRunner import ParametrizedTestCase
from PageObject.me.CancelCollectPage import CancelCollectPage
from PageObject.me.MyCollectHistoryPage import MyCollectHistoryPage
from PageObject.me.CollectSwipeDellPage import CollectSwipeDelPage
from PageObject.me.CollectCheckBoxDelPage import CollectCheckBoxDelPage
import sys
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
我的测试模块

'''


class MeTest(ParametrizedTestCase):
    # 我的收藏进行详情的历史记录
    def testAMyCollectHistory(self):
        page = MyCollectHistoryPage(driver=self.driver, path=PATH("../yaml/me/MyCollectHistory.yaml"))  # 调用测试用例yaml
        page.operate(logTest=self.logTest)  # 调用page层中的用例执行
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)  # 调用page层的用例检查点

    # 取消收藏
    def testCancelCollect(self):
        page = CancelCollectPage(driver=self.driver, path=PATH("../yaml/me/CancelCollect.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 滑动删除
    def testSwipeDelCollect(self):
        page = CollectSwipeDelPage(driver=self.driver, path=PATH("../yaml/me/CollectSwipeDel.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # checkbox删除
    def testCollectCheckBoxDel(self):
        page = CollectCheckBoxDelPage(driver=self.driver, path=PATH("../yaml/me/CollectCheckBoxDel.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    @classmethod
    def setUpClass(cls):
        super(MeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MeTest, cls).tearDownClass()

