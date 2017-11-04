from Base.BaseRunner import ParametrizedTestCase
from PageObject.TestWeiQunPage import *
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestWeiQunTest(ParametrizedTestCase):

    def testWeiQun(self):
        page = TestWeiQun(driver=self.driver, path=PATH("../yaml/TestWeiqun.yaml")) # 调用测试用例yaml
        page.operate(logTest=self.logTest) # 调用page层中的用例执行


    def setUp(self):
        super(TestWeiQunTest, self).setUp()

    '''
    用例结束后，关闭app
    '''
    def tearDown(self):
        super(TestWeiQunTest, self).tearDown()