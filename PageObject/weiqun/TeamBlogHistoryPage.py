from PageObject import Pages


class TeamBlogHistoryPage:
    """
    测试微群下的团队博客浏览历史记录
    driver
    path yaml用例路径
    device 设备名
    logTest 日志记录器
    launch_app 若为1 表示不重新打开app
    caseName 测试函数名字
    """

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"], "launch_app": 1,
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()


if __name__ == "__main__":
    pass
