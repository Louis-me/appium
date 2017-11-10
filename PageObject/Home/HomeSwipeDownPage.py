from PageObject import Pages


class HomeSwipeDownPage:
    '''
    知识-下拉刷新
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.page = Pages.PagesObjects(driver=self.driver, path=kwargs["path"], launch_app=1)

    '''
    操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):
        self.page.operate(logTest)

    def checkPoint(self, caseName, logTest, devices):

        self.page.checkPoint(contrary=1, caseName=caseName, logTest=logTest, devices=devices)