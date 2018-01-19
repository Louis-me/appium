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
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/team/OtherTeamHome.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = OtherTeamHomePage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(TeamTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TeamTest, cls).tearDownClass()
