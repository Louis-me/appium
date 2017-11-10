from PageObject.History.HistoryDetailPage import HistoryDetailPage
from PageObject.History.HistorySwipeDellPage import HistorySwipeDelPage
from PageObject.History.HistoryCheckBoxDelPage import HistoryCheckBoxDelPage
from PageObject.History.HistoryDelAllPage import HistoryDellAllPage
from Base.BaseRunner import ParametrizedTestCase
from Base.BaseTestBase import *
import sys
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
'''
浏览历史列表测试
'''


class HistoryTest(ParametrizedTestCase):
    # # 滑动删除浏览历史记录
    # def testBSwipeDelHistory(self):
    #     page = HistorySwipeDelPage(driver=self.driver, path=PATH("../yaml/history/HistorySwipeDel.yaml"))
    #     page.operate(logTest=self.logTest)
    #     page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 从浏览历史进入到详情页
    def testADetail(self):
        page = HistoryDetailPage(driver=self.driver, path=PATH("../yaml/history/HistoryDetail.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    #     # 多选框删除阅读历史
    # def testCCheckBoxDel(self):
    #     page = HistoryCheckBoxDelPage(driver=self.driver, path=PATH("../yaml/history/HistoryCheckBoxDel.yaml"))
    #     page.operate(logTest=self.logTest)
    #     page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)
    #
    # def testZDelALl(self):
    #     page = HistoryDellAllPage(driver=self.driver, path=PATH("../yaml/history/HistoryDelAll.yaml"))
    #     page.operate(logTest=self.logTest)
    #     page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    @classmethod
    def setUpClass(cls):
        super(HistoryTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HistoryTest, cls).tearDownClass()
