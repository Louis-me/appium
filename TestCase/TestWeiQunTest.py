from Base.BaseRunner import ParametrizedTestCase
from PageObject.weiqun.TeamBlogHistoryPage import TeamBlogHistoryPage
from PageObject.weiqun.TeamDiscussHistoryPage import TeamDiscussHistoryPage
from PageObject.weiqun.TeamHelpHistoryPage import TeamHelpHistoryPage
from PageObject.weiqun.TeamAudioHistoryPage import TeamAudioHistoryPage
from PageObject.weiqun.TeamiMissHistoryPage import TeamiMissHistoryPage
from PageObject.weiqun.SendHelpPage import SendHelpPage
from PageObject.weiqun.SendVotePage import SendVotePage
from PageObject.weiqun.SendBlogPage import SendBlogPage
from PageObject.weiqun.TeamIntroPage import TeamIntroPage
from PageObject.weiqun.SearchHistoryPage import SearchHistoryPage
from PageObject.weiqun.KAPage import KAPage
from PageObject.weiqun.WikiPage import WiKiPage
import os
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
测试微群
'''


class TestWeiQunTest(ParametrizedTestCase):

    # 团队博客浏览历史
    def testATeamBlogHistory(self):

        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/weiqun/TeamBlogHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = TeamBlogHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 团队讨论浏览历史
    def testTeamDiscussHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/weiqun/TeamDiscussHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = TeamDiscussHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 团队求助历史记录
    def testTeamHelp(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/weiqun/TeamHelpHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = TeamHelpHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 团队音频历史记录
    def testTeamAudio(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/weiqun/TeamAudioHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = TeamAudioHistoryPage(app)
        page.operate()
        page.checkPoint()

    # 团队iMiss历史记录
    def testTeamMiss(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/weiqun/TeamiMissHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = TeamiMissHistoryPage(app)
        page.operate()
        page.checkPoint()

    # # 发布提问
    # def testSendHelp(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/weiqun/SendHelp.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = SendHelpPage(app)
    #     page.operate()
    #     page.checkPoint()
    #
    # # 发布投票
    # def testSendVote(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/weiqun/SendVote.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = SendVotePage(app)
    #     page.operate()
    #     page.checkPoint()
    #
    # # 发布博客
    # def testSendBlog(self):
    #     app = {}
    #     app["logTest"] = self.logTest
    #     app["driver"] = self.driver
    #     app["path"] = PATH("../yaml/weiqun/SendBlog.yaml")
    #     app["device"] = self.devicesName
    #     app["caseName"] = sys._getframe().f_code.co_name
    #     page = SendBlogPage(app)
    #     page.operate()
    #     page.checkPoint()

    # 团队介绍
    def testTeamIntro(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/weiqun/TeamIntro.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = TeamIntroPage(app)
        page.operate()
        page.checkPoint()

    # wiki
    def testWiki(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/weiqun/Wiki.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = WiKiPage(app)
        page.operate()
        page.checkPoint()

    # KA
    def testKA(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/weiqun/KA.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = WiKiPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(TestWeiQunTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestWeiQunTest, cls).tearDownClass()


    # def setUp(self):
    #     super(TestWeiQunTest, self).setUp()
    #
    # def tearDown(self):
    #     super(TestWeiQunTest, self).tearDown()
