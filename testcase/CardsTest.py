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
        page = CardsSortPage(driver=self.driver, path=PATH("../yaml/cards/SortCard.yaml"), launch_app=1)
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 删除卡片
    def testDelCard(self):
        page = CardsDelPage(driver=self.driver, path=PATH("../yaml/cards/CardsDel.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    @classmethod
    def setUpClass(cls):
        super(CardsTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CardsTest, cls).tearDownClass()
