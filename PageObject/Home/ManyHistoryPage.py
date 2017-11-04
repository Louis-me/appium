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
        caseName:测试用例函数名 用作统计
        logTest： 日志记录
        devices 设备名
        '''

    def check(self, logTest):
        _result = True
        if self.result:
            for item in self.page.testcheck:
                resp = self.page.operateElement.operate(item, self.page.testInfo, logTest=logTest)
                if not resp:
                    msg = "请检查元素" + item["element_info"] + "是否存在"
                    print(msg)
                    self.page.testInfo[0]["msg"] = msg
                    _result = False
                if resp in self.page.get_value:  # 历史数据和实际数据对比
                    _result = False
                    msg = "出现重复历史记录,数据为：" + resp
                    print(msg)
                    self.page.testInfo[0]["msg"] = msg
                    break
        else:
            _result = False

        return _result


if __name__ == "__main__":
    pass
