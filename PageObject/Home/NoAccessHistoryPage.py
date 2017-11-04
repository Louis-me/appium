from PageObject import Pages


class NoAccessHistoryPage:
    '''
    无权限详情的浏览历史
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
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
        self.result = self.page.operate(logTest)

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
                # 如果resp为假说明无此元素，检查点就是成功
                if resp and resp in self.page.get_value:
                    msg = "无权限浏览详情页数据显示在了历史记录中，数据为：" + resp
                    print(msg)
                    self.page.testInfo[0]["msg"] = msg
                    _result = False
                    break
                # if resp in self.page.get_value:  # 历史数据和实际数据对比
                #     _result = False
                #     msg = "无权限浏览详情页数据显示在了历史记录中，数据为：" + resp
                #     print(msg)
                #     self.page.testInfo[0]["msg"] = msg
                #     break
        else:
            _result = False

        return _result


if __name__ == "__main__":
    pass
