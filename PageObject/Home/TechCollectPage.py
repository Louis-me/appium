from PageObject import Pages


class TechCollectPage:
    '''
    技术专区详情页的收藏
    '''

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.page = Pages.PagesObjects(_init)

        '''
        操作步骤
        '''

    def operate(self):
        self.page.operate()

    def checkPoint(self):
        _check = {"toast": 1}
        self.page.checkPoint(_check)

if __name__ == "__main__":
    pass
