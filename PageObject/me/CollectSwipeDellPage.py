from Base.BaseStatistics import countSum, countInfo
from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
from Base.BaseElementEnmu import Element as be
import re


class CollectSwipeDelPage:
    '''
    滑动删除收藏
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

    '''
     操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):
        for item in self.testCase:

            result = self.operateElement.operate(item, self.testInfo, logTest)
            if not result:
                print("执行过程中失败，请检查元素是否存在" + item["element_info"])
                self.testInfo[0]["msg"] = "执行过程中失败，请检查元素是否存在" + item["element_info"]
                self.isOperate = False
                return False

            if item.get("operate_type", "0") == be.SWIPE_LEFT:  # 根据元素左滑动
                web_element = self.driver.find_elements_by_id(item["element_info"])[item["index"]]
                start = web_element.location
                # 获取控件开始位置的坐标轴
                startx = start["x"]
                starty = start["y"]
                # 获取控件坐标轴差
                size1 = web_element.size

                width = size1["width"]
                height = size1["height"]
                # 计算出控件结束坐标
                endX = width + startx
                endY = height + starty
                self.driver.swipe(endX-50, endY, starty+500, endY)
            if item.get("operate_type", "0") == be.GET_VALUE:
                re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
                self.get_value.append("".join(re_reulst))
        return True

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    devices 设备名
    '''

    def checkPoint(self, **kwargs):
        result = True
        if self.isOperate:
            for item in self.testcheck:
                resp = self.operateElement.operate(item, self.testInfo, kwargs["logTest"])

                if resp in self.get_value:  # 删除后数据对比
                    msg = "删除数据失败,删除前数据为：" + str(self.get_value) + "当前获取的数据为：" + resp
                    print(msg)
                    self.testInfo[0]["msg"] = msg
                    break
        else:
            result = False

        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=kwargs["caseName"],
                  driver=self.driver, logTest=kwargs["logTest"], devices=kwargs["devices"], testCase=self.testCase,
                  testCheck=self.testcheck)
        return result


if __name__ == "__main__":
    pass
