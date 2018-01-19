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
    # 滑动删除浏览历史记录
    def testBSwipeDelHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/history/HistorySwipeDel.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = HistorySwipeDelPage(app)
        page.operate()
        page.checkPoint()

    # 从浏览历史进入到详情页
    def testADetail(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/history/HistoryDetail.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = HistoryDetailPage(app)
        page.operate()
        page.checkPoint()

        # 多选框删除阅读历史
    def testCCheckBoxDel(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/history/HistoryCheckBoxDel.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = HistoryCheckBoxDelPage(app)
        page.operate()
        page.checkPoint()

    # 一键清空
    def testZDelALl(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/history/HistoryDelAll.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = HistoryDellAllPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HistoryTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HistoryTest, cls).tearDownClass()
