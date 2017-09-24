from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
import time
class TechZoneDetail:
    '''
    知识-技术专区详情页
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
        self.getValue = ""

    '''
    操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):
        import time
        time.sleep(3) #防止页面元素没有加载完，就滚动页面
        self.swipeToUp()

        for item in self.testCase:
            if item.get("get_value", "0") == 1 : # 点击之前，取列表中某个元素到文本
                if self.operateElement.findElement(item): # 查找获取到元素是否存在
                    self.getValue = self.driver.find_element_by_xpath(item["element_info"]).get_attribute("text")
                    print("-getValue---")
                    print(self.getValue)
                    self.isOperate = True
                else:
                    self.isOperate = False
                    self.testInfo[0]["msg"] = "获取列表元素到文本值失败"
                    break
            result = self.operateElement.operate(item, self.testInfo, logTest) # 执行操作
            if not result:
                print("操作失败")
                self.testInfo[0]["msg"] = "执行过程中失败"
                self.isOperate = False
                break

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    '''

    def checkPoint(self, caseName, logTest, devices):

        result = False
        if self.isOperate:
            time.sleep(2)  # 进入详情后，页面即使没有加载完成默认也会现实次标签，默认值为博客详情，等待2秒，尽量让页面加载完成后，加载后台数据
            # result = self.operateElement.findElement(self.testcheck)  # 检查点
            self.operateElement.switchToWebview() # 切换到webview
            temp = self.operateElement.operate(self.testcheck, self.testInfo, logTest)
            if not temp:
                print("查找元素" + self.testcheck["element_info"] + "失败")
                self.isOperate = False
                self.testInfo[0]["msg"] = "请检查元素" + self.testcheck["element_info"] + "是否存在"
                result = False
            elif temp == self.getValue: # 对比列表中到一条数据和详情页数据是否相同
                result = True
            else:
                result = False
                self.testInfo[0]["msg"] = "详情页值为="+temp+";列表获取到值为："+self.getValue + "。两者值不相等"

        self.driver.switch_to.context("NATIVE_APP")  # 切换到native,还原
        self.swipeToUp()
        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=caseName, driver=self.driver, logTest=logTest, devices=devices, testCase=self.testCase, testCheck=self.testcheck)

        return result

    def swipeToUp(self):

        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        # self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 600)
        self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToDown--")