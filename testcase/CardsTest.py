from Base.BaseRunner import ParametrizedTestCase
from PageObject.cards.CardsDelPage import CardsDelPage
from PageObject.cards.CardsSortPage import CardsSortPage
from Base.BaseTestBase import *
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
'''
卡片列表测试
'''


class CardsTest(ParametrizedTestCase):
    # 排序
    def testASortCard(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/cards/SortCard.yaml")
        app["device"] = self.devicesName
        app["launch_app"] = 1
        app["caseName"] = sys._getframe().f_code.co_name
        page = CardsSortPage(app)
        page.operate()
        page.checkPoint()

    # 删除卡片
    def testDelCard(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/cards/CardsDel.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = CardsDelPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(CardsTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CardsTest, cls).tearDownClass()
