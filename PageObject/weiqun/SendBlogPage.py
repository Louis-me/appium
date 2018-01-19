from PageObject import Pages


class SendBlogPage:
    '''
    发布博客
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
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

    def checkPoint(self):
        _check = {"toast": 1}
        self.page.checkPoint(_check)

if __name__ == "__main__":
    pass
