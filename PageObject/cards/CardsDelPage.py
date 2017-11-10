from PageObject import Pages


class CardsDelPage:
    '''
    首页删除卡片
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.page = Pages.PagesObjects(driver=self.driver, path=kwargs["path"])

    '''
    操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):
        self.page.operate(logTest)

    def checkPoint(self, caseName, logTest, devices):

        self.page.checkPoint(contrary_getval=1, caseName=caseName, logTest=logTest, devices=devices)

