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
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/me/MyCollectHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = MyCollectHistoryPage(app)
        page.operate()  # 调用page层中的用例执行
        page.checkPoint()  # 调用page层的用例检查点

    # 取消收藏
    def testCancelCollect(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/me/CancelCollect.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = CancelCollectPage(app)
        page.operate()
        page.checkPoint()

    # 滑动删除
    def testSwipeDelCollect(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/me/CollectSwipeDel.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = CollectSwipeDelPage(app)
        page.operate()
        page.checkPoint()

    # checkbox删除
    def testCollectCheckBoxDel(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/me/CollectCheckBoxDel.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = CollectCheckBoxDelPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(MeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MeTest, cls).tearDownClass()

