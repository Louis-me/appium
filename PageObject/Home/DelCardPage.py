from PageObject import Pages


class DelCardPage:
    '''
    删除技术卡片
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.page = Pages.PagesObjects(driver=self.driver, path=kwargs["path"])
        self.result = True

    '''
    操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):
        self.result = self.page.operate(logTest, 1)

    def checkPoint(self, caseName, logTest, devices):

        self.page.checkPoint(func=self.check(logTest), caseName=caseName, logTest=logTest, devices=devices)

    '''
    检查点
    logTest： 日志记录
    '''

    def check(self, logTest):
        _result = True
        if self.result:
            for item in self.page.testcheck:
                resp = self.page.operateElement.operate(item, self.page.testInfo, logTest=logTest)
                if resp:
                    msg = "技术专区卡片删除不成功，依然停留在页面"
                    print(msg)
                    self.page.testInfo[0]["msg"] = msg
                    _result = False
        else:
            _result = False

        return _result

