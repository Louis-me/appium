
from PageObject import Pages


class HistoryDetailPage:
    '''
    阅读历史进入到详情页
    '''

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"], "launch_app": 1,
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    '''
    操作步骤
    '''

    def operate(self):
        self.page.operate()

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    '''

    def checkPoint(self):
        self.page.checkPoint()
