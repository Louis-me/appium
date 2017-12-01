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
        page = ContactHistoryPage(driver=self.driver, path=PATH("../yaml/contact/ContactHistory.yaml"))
        page.operate(logTest=self.logTest)  # 调用page层中的用例执行
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)

    # 通讯录公众号浏览历史
    def testPublicPlatHistory(self):
        page = PublicPlatHistoryPage(driver=self.driver, path=PATH("../yaml/contact/PublicPlatformHistory.yaml"))
        page.operate(logTest=self.logTest)
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest,  devices=self.devicesName)

    @classmethod
    def setUpClass(cls):
        super(ContactTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(ContactTest, cls).tearDownClass()