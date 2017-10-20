from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
import time
from Base.BaseElementEnmu import Element

class TechZoneDel:
    '''
    知识-删除技术专区
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True
        test_msg = getYam(self.path)
        self.testInfo = test_msg["testinfo"]
        self.testCase = test_msg["testcase"]
        self.testcheck = test_msg["check"]

    '''
    操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):

        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest) # 执行操作

            if item.get("swipe", "0") == "up":
                self.operateElement.swipeToUp(n=1) # 上滑

            if not result:
                print("执行过程中失败，请检查元素是否存在" + item["element_info"])
                self.testInfo[0]["msg"] = "执行过程中失败，请检查元素是否存在" + item["element_info"]
                self.isOperate = False
                break
            if item.get("is_time", "0") != "0":
                time.sleep(int(item["is_time"]))  # 等待时间


    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    '''

    def checkPoint(self, caseName, logTest, devices):

        result = False
        if self.isOperate:
            for item in self.testcheck:
                temp = self.operateElement.operate(item, self.testInfo, logTest)

                if temp:
                    # print("查找元素" + item["element_info"] + "失败")
                    self.isOperate = False
                    self.testInfo[0]["msg"] = "请检查元素" + item["element_info"] + "是否已经删除"
                    result = False
                    break

                else:
                    result = True
        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=caseName, driver=self.driver, logTest=logTest,
                  devices=devices, testCase=self.testCase, testCheck=self.testcheck)
        return result
