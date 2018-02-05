from PageObject.History.HistoryDelAllPage import HistoryDellAllPage
from PageObject.Home.BannerHistoryPage import BannerHistoryPage
from PageObject.Home.DeptNoticeHistoryPage import DeptNoticeHistoryPage
from PageObject.Home.HomeSearchHistoryPage import HomeSearhHistoryPage
from PageObject.Home.HomeSwipeDownPage import HomeSwipeDownPage
from PageObject.Home.ManyHistoryPage import ManyHistoryPage
from PageObject.Home.MyClassHistoryPage import MyClassHistoryPage
from PageObject.Home.NoAccessHistoryPage import NoAccessHistoryPage
from PageObject.Home.NoHistoryPage import NoHistoryPage
from Base.BaseRunner import ParametrizedTestCase
from PageObject.Home.DelCardPage import DelCardPage
from PageObject.Home.TechHistoryPage import TechHistoryPage
from PageObject.Home.TechNoNullPage import TechNotNullPage
from PageObject.Home.ClearCachePage import ClearCachePage
from PageObject.Home.WeiBBSHistoryPage import WeiBBsHistoryPage
from PageObject.Home.TopNewHistoryPage import TopNewHistoryPage
from PageObject.Home.TechCollectPage import TechCollectPage
from PageObject.Home.HotAnswerHistoryPage import HotAnswerHistoryPage
from PageObject.Home.DayNewHistoryPage import DayNewHistoryPage
from PageObject.Home.YourCommendDetailLinkPage import YourCommendDetailLinkPage
from PageObject.Home.HotAnswerMyTeamHistoryPage import HotAnswerMyTeamHistoryPage
from PageObject.Home.GoodBologHistoryPage import GoodBlogHistoryPage
from PageObject.Home.LivePage import LivePage
from PageObject.Home.VideoAudioHistory import VideoAudioHistoryPage
from Base.BaseTestBase import *
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeTest(ParametrizedTestCase):
    # 首页下拉
    def testAHomeSwipeDown(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/HomeSwipeDown.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = HomeSwipeDownPage(app)
        page.operate()
        page.checkPoint()

    # banner浏览历史记录
    def testB0annerHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/BannerHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = BannerHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 一键清阅读历史空
    def testB1DelALl(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/history/HistoryDelAll.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = HistoryDellAllPage(app)
        page.operate()
        page.checkPoint()

    # 无浏览历史页面检测
    def testB2NoHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/NoHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = NoHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 技术专区收藏
    def testTechCollect(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/TechCollect.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        tech_card(login(), app["device"])
        page = TechCollectPage(app)
        page.operate()
        page.checkPoint()

    # 热门问答-最高悬赏浏览历史记录
    def testHotAnswerHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/HotAnswerHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        hotAnswer_card(login(), app["device"])
        page = HotAnswerHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 热门问答-我的团队问答浏览历史记录
    def testHotAnswerMyTeamHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/HotAnswerMyTeamHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        hotAnswer_card(login(), app["device"])
        page = HotAnswerMyTeamHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 精选博客-浏览历史记录
    def testGoodBlogHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/GoodBlogHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        good_blog_card(login(), app["device"])
        page = GoodBlogHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 直播详情页
    def testLive(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/Live.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        live_card(login(), app["device"])
        page = LivePage(app)
        page.operate()
        page.checkPoint()

    # 视听专区详情页
    def testVideoAudioHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/VideoAudioHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        video_audio_card(login(), app["device"])
        page = VideoAudioHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 为您推荐详情页链接跳转
    def testYourCommendDetailLink(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/YourCommendDetailLink.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        your_commend(login(), app["device"])
        page = YourCommendDetailLinkPage(app)
        page.operate()
        page.checkPoint()

    # 每日新闻浏览历史记录
    def testDayNewHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/DayNewHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        dayNew_card(login(), app["device"])
        page = DayNewHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 多次浏览后的历史记录
    def testManyHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/ManyHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = ManyHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 我的课程浏览历史记录
    def testMyClassHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/MyClassHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        myClass_card(login(), app["device"])
        page = MyClassHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 部门公告浏览历史记录
    def testDeptNoticeHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/DeptNoticeHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        notice_card(login(), app["device"])

        page = DeptNoticeHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 搜索后的浏览历史记录
    def testHomeSearchHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/HomeSearchHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = HomeSearhHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 没有权限浏览的历史记录
    def testNoAccessHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/NoAccessHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        notice_card(login(), app["device"])

        page = NoAccessHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 测试微群浏览历史记录
    def testBWeiBBSHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/WeiBBSHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = WeiBBsHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 删除首页卡片
    def testZDelHomeCard(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/home/DelTech.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        tech_card(login(), app["device"])

        page = DelCardPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()
