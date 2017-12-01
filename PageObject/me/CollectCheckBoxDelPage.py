from PageObject import Pages


class CollectCheckBoxDelPage:
    '''
    多选框删除我的收藏
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

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    excepts 如果检查点获取数据失败，则为成功
    contrary_getval 获取到了数据与历史数据对比，若对比成功，检查点则为失败
    '''

    def checkPoint(self, caseName, logTest, devices):
        self.page.checkPoint(excepts=1, contrary_getval=1, caseName=caseName, logTest=logTest, devices=devices)

if __name__ == "__main__":
    pass
