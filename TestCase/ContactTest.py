import os

from Base.BaseRunner import ParametrizedTestCase
from PageObject.contact.ContactHistoryPage import ContactHistoryPage
from PageObject.contact.PublicPlatHistoryPage import PublicPlatHistoryPage
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ContactTest(ParametrizedTestCase):
    # 通讯录好友动态浏览历史
    def testAContactHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/contact/ContactHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name

        page = ContactHistoryPage(app)
        page.operate()  # 调用page层中的用例执行
        page.checkPoint()

    # 通讯录公众号浏览历史
    def testPublicPlatHistory(self):
        app = {}
        app["logTest"] = self.logTest
        app["driver"] = self.driver
        app["path"] = PATH("../yaml/contact/PublicPlatformHistory.yaml")
        app["device"] = self.devicesName
        app["caseName"] = sys._getframe().f_code.co_name
        page = PublicPlatHistoryPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(ContactTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(ContactTest, cls).tearDownClass()
