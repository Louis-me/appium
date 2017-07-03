from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
class Write:
    '''
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    logTest: 日记记录
    testInfo：用例介绍
    testCase：操作步骤
    prefix： 前置条件
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True

        _getYam = getYam(self.path)
        self.testInfo = _getYam["testinfo"]
        self.testCase = _getYam["testcase"]
        self._prefix = _getYam["prefix"]

    '''
    前置条件
    logTest 日记记录器
    '''
    def prefix(self, logTest):
        result = self.operateElement.operate(mOperate=self._prefix[0], testInfo=self.testInfo, logTest=logTest)
        self.operateElement.switchToContext(self._prefix[0]["isWebView"])
        if not result:
            print("前置条件失败")
            self.isOperate = False
            return
    '''
       操作步骤
        logTest 日记记录器
       '''

    def operate(self, logTest):

        self.prefix(logTest)

        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)
            if not result:
                print("操作失败")
                self.isOperate = False
                break
    '''
    检查点
    '''

    def checkPoint(self, caseName, logTest, devices):
        result = False
        if not self.isOperate:
            print("操作失败,检查点失败")
        else:
            check = getYam(self.path)["check"]
            result = self.operateElement.findElement(check)  # 检查点

        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=caseName, driver=self.driver, logTest=logTest,
                  devices=devices)
        return result


