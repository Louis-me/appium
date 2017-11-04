from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
import time
from Base.BaseElementEnmu import Element as be
import re
class PagesObjects:
    '''
    page层
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
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
        self.is_get = False # 检查点特殊标志，结合get_value使用。若为真，说明检查点要对比历史数据和实际数据

    '''
     操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest, tap_swipe=None):
        for item in self.testCase:

            if tap_swipe is not None: # 如果是直接操作屏幕操作，先等待
                if item.get("is_time", "0") != "0":
                    time.sleep(item["is_time"])  # 等待时间

            result = self.operateElement.operate(item, self.testInfo, logTest)
            if not result:
                print("执行过程中失败，请检查元素是否存在" + item["element_info"])
                self.testInfo[0]["msg"] = "执行过程中失败，请检查元素是否存在" + item["element_info"]
                self.isOperate = False
                return False
            if item.get("is_time", "0") != "0":
                time.sleep(item["is_time"])  # 等待时间
                print("--等待下---")

            if item.get("operate_type", "0") == be.GET_VALUE:
                re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
                self.get_value.append("".join(re_reulst))
                self.is_get = True # 对比数据
        return True


    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    contrary 相反检查点，意思就是如果检查结果为真，检查点就是失败
    msg: 自定义错误日志
    i_fucntion 自定义函数返回结果
    '''

    def checkPoint(self, func=None, **kwargs):
        result = True
    # def checkPoint(self, caseName, logTest, devices, contrary=None, msg=None):
        if func is not None:
            result = func

        elif self.isOperate:
            for item in self.testcheck:
                resp = self.operateElement.operate(item, self.testInfo, kwargs["logTest"])

                if not resp:
                    msg = "请检查元素" + item["element_info"] + "是否存在"
                    print(msg)
                    self.isOperate = False
                    self.testInfo[0]["msg"] = msg
                    result = False
                    break

                if self.is_get and resp not in self.get_value: # 历史数据和实际数据对比
                    result = False
                    msg = "对比数据失败,获取历史数据为：" + str(self.get_value) + "当前获取的数据为：" + resp
                    print(msg)
                    self.testInfo[0]["msg"] = msg
                    break
        else:
            result = False
        self.operateElement.switchToNative()
        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=kwargs["caseName"],
                  driver=self.driver, logTest=kwargs["logTest"], devices=kwargs["devices"], testCase=self.testCase, testCheck=self.testcheck)
        return result
