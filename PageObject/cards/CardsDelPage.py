from PageObject import Pages


class CardsDelPage:
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
                if resp in self.page.get_value:  # 历史数据和实际数据对比
                    _result = False
                    msg = "删除卡片失败,删除成功的卡片为：" + ".".join(self.page.get_value) + "当前第一条获取卡片数为：" + resp
                    print(msg)
                    self.page.testInfo[0]["msg"] = msg
                    break
        else:
            _result = False

        return _result

