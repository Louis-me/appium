from PageObject import Pages


class CancelCollectPage:
    '''
    取消收藏
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
        logTest： 日志记录
        devices 设备名
        '''

    def check(self, logTest):
        flag = True
        if self.result:
            for item in self.page.testcheck:
                resp = self.page.operateElement.toast(item["element_info"], testInfo=self.page.testInfo, logTest=logTest)
                if not resp:
                    msg = "请检查元素" + item["element_info"] + "是否存在"
                    print(msg)
                    self.page.testInfo[0]["msg"] = msg
                    flag = False

        else:
            flag = False

        return flag


if __name__ == "__main__":
    pass
