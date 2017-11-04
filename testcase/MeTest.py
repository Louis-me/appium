import os
from Base.BaseRunner import ParametrizedTestCase
from PageObject.Home.NoHistoryPage import NoHistoryPage
from PageObject.me.MyCollectHistoryPage import MyCollectHistoryPage
from PageObject.me.ClearCachePage import ClearCachePage
from PageObject.me.CancelCollectPage import CancelCollectPage
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

    # def testClearCache(self):
    #     page = ClearCachePage(driver=self.driver, path=PATH("../yaml/me/ClearCache.yaml"))
    #     page.operate(logTest=self.logTest)
    #     page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # # 无浏览历史页面检测
    # def testNoHistory(self):
    #     page = NoHistoryPage(driver=self.driver, path=PATH("../yaml/home/NoHistory.yaml"))
    #     page.operate(logTest=self.logTest)
    #     page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 取消收藏
    # def testCancelCollect(self):
    #     page = CancelCollectPage(driver=self.driver, path=PATH("../yaml/me/CancelCollect.yaml"))
    #     page.operate(logTest=self.logTest)
    #     page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    @classmethod
    def setUpClass(cls):
        super(MeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MeTest, cls).tearDownClass()

