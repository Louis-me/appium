from PageObject import Pages


class ManyHistoryPage:
    '''
    多次浏览微社区历史
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
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

        self.page.checkPoint(caseName=caseName, logTest=logTest, devices=devices, contrary_getval=1)

if __name__ == "__main__":
    pass
