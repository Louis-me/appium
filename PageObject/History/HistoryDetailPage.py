
from PageObject import Pages


class HistoryDetailPage:
    '''
    阅读历史进入到详情页
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

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    '''

    def checkPoint(self, caseName, logTest, devices):
        self.page.checkPoint(caseName=caseName, logTest=logTest, devices=devices)
