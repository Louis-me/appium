from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
from Base.BaseElementEnmu import Element as be
import re


class CardsSortPage:
    '''
    滑动删除历史记录
    isOperate: 操作失败，检查点就失败,kwargs: WebDriver driver, String path(yaml配置参数)
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        if kwargs.get("launch_app", "0") == "0":  # 若为空，重新打开app
            self.driver.launch_app()
        self.path = kwargs["path"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True
        test_msg = getYam(self.path)
        self.testInfo = test_msg["testinfo"]
        self.testCase = test_msg["testcase"]
        self.testcheck = test_msg["check"]
        self.get_value = []
        self.location = []
        self.msg = ""

    '''
     操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):
        for item in self.testCase:

            result = self.operateElement.operate(item, self.testInfo, logTest)
            if not result["result"]:
                m_s_g = self.msg + "\n" if self.msg != "" else ""
                msg = m_s_g + "执行过程中失败，请检查元素是否存在" + item["element_info"]
                print(msg)

                self.testInfo[0]["msg"] = msg
                self.isOperate = False
                return False

            if item.get("operate_type", "0") == "location":
                app = {}
                web_element = self.driver.find_elements_by_id(item["element_info"])[item["index"]]
                start = web_element.location
                # 获取控件开始位置的坐标轴
                app["startX"] = start["x"]
                app["startY"] = start["y"]
                # 获取控件坐标轴差
                size1 = web_element.size

                width = size1["width"]
                height = size1["height"]
                # 计算出控件结束坐标
                endX = width + app["startX"]
                endY = height + app["startY"]

                app["endX"] = endX - 20
                app["endY"] = endY - 60

                self.location.append(app)
                # self.driver.swipe(endX, endY, starty, endY)
            if item.get("operate_type", "0") == be.GET_VALUE:
                self.get_value.append(result["text"])

            if item.get("is_swpie", "0") != "0":
                print(self.location)
                self.driver.swipe(self.location[0]["endX"], self.location[0]["endY"], self.location[1]["endX"], self.location[1]["endY"]+10)

        return True

    def checkPoint(self, **kwargs):
        result = self.check(**kwargs)
        if result is not True and be.RE_CONNECT:
            self.msg = "用例失败重连过一次，失败原因:" + self.testInfo[0]["msg"]
            kwargs["logTest"].buildStartLine(kwargs["caseName"] + "_失败重连")  # 记录日志
            self.operateElement.switchToNative()
            self.driver.launch_app()
            self.isOperate = True
            self.operate(kwargs["logTest"])
            self.get_value = []
            self.location = ""
            result = self.check(**kwargs)
            self.testInfo[0]["msg"] = self.msg
        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=kwargs["caseName"],
                  driver=self.driver, logTest=kwargs["logTest"], devices=kwargs["devices"], testCase=self.testCase,
                  testCheck=self.testcheck)
        return result

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    contrary 相反检查点，意思就是如果检查结果为真，检查点就是失败
    '''

    def check(self, **kwargs):
        result = True
        m_s_g = self.msg + "\n" if self.msg != "" else ""
        # 重跑后异常日志
        if self.isOperate:
            for item in self.testcheck:
                resp = self.operateElement.operate(item, self.testInfo, kwargs["logTest"])
                if not resp["result"]:
                    msg = "请检查元素" + item["element_info"] + "是否存在"
                    self.msg = m_s_g + msg
                    print(msg)
                    self.testInfo[0]["msg"] = msg
                    result = False
                if resp['text'] not in self.get_value:  # 删除后数据对比
                    msg = "卡片排序失败" + str(self.get_value) + "当前首页第一条卡片数据为：" + resp["text"] + "排序成功的第一个卡片值为："+".".join(self.get_value)
                    self.msg = m_s_g + msg
                    print(msg)
                    self.testInfo[0]["msg"] = msg
                    break
        else:
            result = False
        return result


if __name__ == "__main__":
    pass
