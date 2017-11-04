from PageObject import Pages


class HistoryCheckBoxDelPage:
    '''
    多选框删除历史记录
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

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    '''

    def checkPoint(self, caseName, logTest, devices):
        self.page.checkPoint(func=self.check(logTest), caseName=caseName, logTest=logTest, devices=devices)

    def check(self, logTest):
        flag = True
        if self.result:
            for item in self.page.testcheck:
                resp = self.page.operateElement.operate(item, self.page.testInfo, logTest=logTest)

                if resp in self.page.get_value:  # 删除前后历史数据和实际数据对比
                    flag = False
                    msg = "删除数据失败,想要删除的数据为：" + ".".join(self.page.get_value) + ",当前获取的数据为：" + resp
                    print(msg)
                    self.page.testInfo[0]["msg"] = msg
                    break
        else:
            flag = False

        return flag


if __name__ == "__main__":
    pass
