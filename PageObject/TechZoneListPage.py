from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
from Base.BaseElementEnmu import Element
import time
class TechZoneList:
    '''
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
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
        self.getValue = []
    def operate(self, logTest): # 操作步骤
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)
            if not result:
                self.isOperate = False
                self.testInfo[0]["msg"] = "执行过程中失败，请检查元素是否存在"+item["element_info"]
                break
            if item.get("operate_type", "0") == Element.GET_VALUE:
                self.getValue.append(result)
            if item.get("swipe", "0") == "up": # 滑动
                self.operateElement.swipeToUp(n=1)
            if item.get("is_time", "0") != "0":
                time.sleep(int(item["is_time"]))  # 等待时间，从详情页返回到列表后，列表数据需要时间更新
    def checkPoint(self, caseName, logTest, devices): #检查点
        result = False
        if self.isOperate:
            for item in self.testcheck:
                resp = self.operateElement.operate(item, self.testInfo, logTest)
                if not resp:
                    self.isOperate = False
                    self.testInfo[0]["msg"] = "请检查元素"+item["element_info"]+"是否存在"
                    result = False
                    break
                elif resp in self.getValue:
                    result = True
                else:
                    result = False # 只要有一条数据不匹配，用例就失败
                    self.testInfo[0]["msg"] = "首页到知识专区到列表三条数据和详情页到三条数据对不上。" \
                        "详情页三条数据为："+ str(self.getValue)+"。首页当前匹配数据为:" + resp
                    break
        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=caseName, driver=self.driver, logTest=logTest,
                  devices=devices, testCase=self.testCase, testCheck=self.testcheck)
        return result