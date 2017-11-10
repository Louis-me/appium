from Base.BaseRunner import ParametrizedTestCase
from PageObject.team.OtherTeamHomePage import OtherTeamHomePage
import os
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
'''
团队列表测试
'''


class TeamTest(ParametrizedTestCase):
    # 我没有加入到团队首页
    def testAOtherTeamHome(self):
        page = OtherTeamHomePage(driver=self.driver, path=PATH("../yaml/team/OtherTeamHome.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    @classmethod
    def setUpClass(cls):
        super(TeamTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TeamTest, cls).tearDownClass()
