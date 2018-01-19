from PageObject import Pages


class CollectCheckBoxDelPage:
    '''
    多选框删除我的收藏
    '''

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    '''
    操作步骤
    '''
    def operate(self):
        self.page.operate()

    '''
    contrary_getval 获取到了数据与历史数据对比，若对比成功，检查点则为失败
    '''

    def checkPoint(self):
        _check = {"check": "contrary_getval"}
        self.page.checkPoint(_check)

if __name__ == "__main__":
    pass
