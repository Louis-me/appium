import os

from Base.BaseRunner import ParametrizedTestCase
from PageObject.contact.ContactHistoryPage import *
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ContactTest(ParametrizedTestCase):
    def testContactHistory(self):
        page = ContactHistoryPage(driver=self.driver, path=PATH("../yaml/contact/ContactHistory.yaml"))  # 调用测试用例yaml
        page.operate(logTest=self.logTest)  # 调用page层中的用例执行
        page.checkPoint(caseName=sys._getframe().f_code.co_name, logTest=self.logTest, devices=self.devicesName)  # 调用page层的用例检查点

    @classmethod
    def setUpClass(cls):
        super(ContactTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(ContactTest, cls).tearDownClass()