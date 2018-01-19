from PageObject import Pages


class ClearCachePage:
    '''
    清空缓存
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
    '''

    def __init__(self, **kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"], "launch_app": 1,
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()


if __name__ == "__main__":
    pass
