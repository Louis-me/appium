from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
from Base.BaseElementEnmu import Element

import time
class QuanlianList():
    '''
    知识-全联接大会列表页面
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
        self.getValue = []

    '''
    操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):



        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)

            if not result:
                print("操作失败")
                self.isOperate = False
                self.testInfo[0]["msg"] = "执行过程中失败，请检查元素是否存在"+item["element_info"]
                break

            elif item.get("operate_type", "0") == Element.GET_VALUE:
                self.getValue.append(result)


            if item.get("swipe", "0") == "up":
                # MXF5T15B10000039
               self.operateElement.swipeToUp(n=9)


            if item.get("is_time", "0") != "0":
                    time.sleep(int(item["is_time"]))  # 等待时间，从详情页返回到列表后，列表数据需要时间更新

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    '''

    def checkPoint(self, caseName, logTest, devices):

        # time.sleep(2) #  从详情页返回到列表后，列表数据需要时间更新

        result = False
        if self.isOperate:
            for item in self.testcheck:
                temp = self.operateElement.operate(item, self.testInfo, logTest)

                if not temp:
                    print("查找元素"+item["element_info"]+"失败")
                    self.isOperate = False
                    self.testInfo[0]["msg"] = "请检查元素"+item["element_info"]+"是否存在"
                    result = False
                    break

                elif temp in self.getValue:
                    result = True
                else:
                    result = False # 只要有一条数据不匹配，用例就失败
                    self.testInfo[0]["msg"] = "首页到知识专区到列表三条数据和详情页到三条数据对不上。详情页三条数据为："+ str(self.getValue)+"。首页当前匹配数据为:"+temp
                    break

        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=caseName, driver=self.driver, logTest=logTest, devices=devices, testCase=self.testCase, testCheck=self.testcheck)
        return result

