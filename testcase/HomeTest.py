from PageObject.Home.BannerHistoryPage import BannerHistoryPage
from PageObject.Home.DeptNoticeHistoryPage import DeptNoticeHistoryPage
from PageObject.Home.HomeSearchHistoryPage import HomeSearhHistoryPage
from PageObject.Home.HomeSearhPage import HomeSearchPage
from PageObject.Home.HomeSwipeDownPage import HomeSwipeDownPage
from PageObject.Home.ManyHistoryPage import ManyHistoryPage
from PageObject.Home.MyClassHistoryPage import MyClassHistoryPage
from PageObject.Home.NoAccessHistoryPage import NoAccessHistoryPage
from PageObject.Home.NoHistoryPage import NoHistoryPage
from Base.BaseRunner import ParametrizedTestCase
from PageObject.Home.DelCardPage import *
from PageObject.Home.TechHistoryPage import TechHistoryPage
from PageObject.Home.TechNoNullPage import TechNotNullPage
from PageObject.me.ClearCachePage import ClearCachePage
from PageObject.weiqun.WeiBBSHistoryPage import WeiBBsHistoryPage
from PageObject.Home.TopNewHistoryPage import TopNewHistoryPage
from PageObject.Home.TechCollectPage import TechCollectPage
from TestCase.TestCaseBase import *
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeTest(ParametrizedTestCase):
    def testA1ClearCache(self):
        page = ClearCachePage(driver=self.driver, path=PATH("../yaml/me/ClearCache.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 无浏览历史页面检测
    def testA2NoHistory(self):
        page = NoHistoryPage(driver=self.driver, path=PATH("../yaml/home/NoHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 首页下拉
    def testHomeSwipeDown(self):
        page = HomeSwipeDownPage(driver=self.driver, path=PATH("../yaml/home/HomeSwipeDown.yaml"),)
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # banner浏览历史记录
    def testBannerHistory(self):

        page = BannerHistoryPage(driver=self.driver, path=PATH("../yaml/home/BannerHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 知识头条浏览历史
    def testTopNewHistory(self):
        page = TopNewHistoryPage(driver=self.driver, path=PATH("../yaml/home/TopNewHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 技术专区收藏
    def testTechCollect(self):
        devices = self.devicesName
        tech_card(login(), devices)
        page = TechCollectPage(driver=self.driver, path=PATH("../yaml/home/TechCollect.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=devices)

    # 技术专区浏览历史记录
    def testTechHistory(self):
        devices = self.devicesName
        tech_card(login(), devices)
        page = TechHistoryPage(driver=self.driver, path=PATH("../yaml/home/TechHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=devices)

    # 技术专区列表内容为空检测
    def testTechNotNull(self):

        devices = self.devicesName
        tech_card(login(), devices)
        page = TechNotNullPage(driver=self.driver, path=PATH("../yaml/home/TechNotNull.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=devices)

        # 多次浏览后的历史记录

    def testManyHistory(self):

        page = ManyHistoryPage(driver=self.driver, path=PATH("../yaml/home/ManyHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 我的课程浏览历史记录
    def testMyClassHistory(self):
        devices = self.devicesName
        myClass_card(login(), devices)
        page = MyClassHistoryPage(driver=self.driver, path=PATH("../yaml/home/MyClassHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=devices)

    # 部门公告浏览历史记录
    def testDeptNoticeHistory(self):
        devices = self.devicesName
        notice_card(login(), devices)

        page = DeptNoticeHistoryPage(driver=self.driver, path=PATH("../yaml/home/DeptNoticeHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=devices)

    # 搜索后的浏览历史记录
    def testHomeSearchHistory(self):
        page = HomeSearhHistoryPage(driver=self.driver, path=PATH("../yaml/home/HomeSearchHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 没有权限浏览的历史记录
    def testNoAccessHistory(self):
        devices = self.devicesName
        notice_card(login(), devices)

        page = NoAccessHistoryPage(driver=self.driver, path=PATH("../yaml/home/NoAccessHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=devices)

    # 测试微群浏览历史记录
    def testBWeiBBSHistory(self):
        page = WeiBBsHistoryPage(driver=self.driver, path=PATH("../yaml/home/WeiBBSHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 删除首页卡片
    def testZDelHomeCard(self):
        devices = self.devicesName
        tech_card(login(), devices)

        page = DelCardPage(driver=self.driver, path=PATH("../yaml/home/DelTech.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=devices)

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()
