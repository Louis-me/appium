from PageObject import Pages


class HomeSwipeDownPage:
    '''
    知识-下拉刷新
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"], "launch_app": 1,
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    '''
    操作步骤
     logTest 日记记录器
    '''

    def operate(self):
        self.page.operate()

    def checkPoint(self):
        self.page.checkPoint()
