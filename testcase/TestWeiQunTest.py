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
    def testTeamBlogHistory(self):
        page = TeamBlogHistoryPage(driver=self.driver, path=PATH("../yaml/weiqun/TeamBlogHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 团队讨论浏览历史
    def testTeamDiscussHistory(self):
        page = TeamDiscussHistoryPage(driver=self.driver, path=PATH("../yaml/weiqun/TeamDiscussHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 团队求助
    def testTeamHelp(self):
        page = TeamHelpHistoryPage(driver=self.driver, path=PATH("../yaml/weiqun/TeamHelpHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 团队音频
    def testTeamAudio(self):
        page = TeamAudioHistoryPage(driver=self.driver, path=PATH("../yaml/weiqun/TeamAudioHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 团队iMiss
    def testTeamMiss(self):
        page = TeamiMissHistoryPage(driver=self.driver, path=PATH("../yaml/weiqun/TeamiMissHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 发布提问
    def testSendHelp(self):
        page = SendHelpPage(driver=self.driver, path=PATH("../yaml/weiqun/SendHelp.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 发布投票
    def testSendVote(self):
        page = SendVotePage(driver=self.driver, path=PATH("../yaml/weiqun/SendVote.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 发布博客
    def testSendBlog(self):
        page = SendBlogPage(driver=self.driver, path=PATH("../yaml/weiqun/SendBlog.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 团队介绍
    def testTeamIntro(self):
        page = TeamIntroPage(driver=self.driver, path=PATH("../yaml/weiqun/TeamIntro.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    @classmethod
    def setUpClass(cls):
        super(TestWeiQunTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestWeiQunTest, cls).tearDownClass()