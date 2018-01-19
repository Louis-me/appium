from PageObject import Pages


class TeamDiscussHistoryPage:

    """
    测试微群下的团队讨论浏览历史记录
     driver
     path yaml用例路径
     device 设备名
     logTest 日志记录器
     caseName 测试函数名字
     """

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()


if __name__ == "__main__":
    pass
