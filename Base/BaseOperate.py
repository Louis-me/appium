__author__ = 'shikun'
# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions
from Base.BaseElementEnmu import Element as baseElement
import time

'''
# 此脚本主要用于查找元素是否存在，操作页面元素
'''


class OperateElement:
    def __init__(self, driver=""):
        self.driver = driver

    def findElement(self, mOperate):
        '''
        查找元素.mOperate,dict|list
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            if type(mOperate) == list:  # 多检查点
                for item in mOperate:
                    WebDriverWait(self.driver, baseElement.WAIT_TIME).until(lambda x: self.elements_by(item))
                return True
            if type(mOperate) == dict:  # 单检查点
                WebDriverWait(self.driver, baseElement.WAIT_TIME).until(lambda x: self.elements_by(mOperate))
                return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            print("找不到数据")
            return False

    '''
   查找元素.mOperate是字典
   operate_type：对应的操作
   element_info：元素详情
   find_type: find类型
   
   testInfo
   logTest: 记录日志
    '''

    def operate(self, mOperate, testInfo, logTest):
        if self.findElement(mOperate):
            elements = {
                baseElement.CLICK: lambda: self.click(mOperate),
                baseElement.SET_VALUE: lambda: self.set_value(mOperate),
                baseElement.SWIPELEFT: lambda: self.swipeLeft(mOperate)
            }
            logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + mOperate["element_info"])  # 记录日志
            elements[mOperate["operate_type"]]()
            return True
        return False

    # 点击事件
    def click(self, mOperate):
        if mOperate["find_type"] == baseElement.find_element_by_id or mOperate["find_type"] == baseElement.find_element_by_xpath:
            self.elements_by(mOperate).click()

    '''
    切换webview和native
    
    '''
    def switchToContext(self, webview=True):
        if webview:
            for cons in self.driver.contexts:
                if cons.lower().startswith("webview"):
                    self.driver._switch_to.context(cons)
                    break
        else:
            self.driver._switch_to.context("NATIVE_APP") # 切换到native



    # 左滑动
    def swipeLeft(self, mOperate):
        # time.sleep(1)
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        for i in range(mOperate["time"]):
            self.driver.swipe(width / 4 * 3, height / 2, width / 4 * 1, height / 2, 600)


# start_x,start_y,end_x,end_y

# 轻打x轴向右移动x单位，y轴向下移动y单位
# def operate_tap(elemen_by,driver,element_info, xy=[]):
#     elements_by(elemen_by, driver, element_info).tap(x=xy[0], y=xy[1])

    def set_value(self, mOperate):
        self.elements_by(mOperate).set_value(mOperate["text"])


# 封装常用的标签
    def elements_by(self, mOperate):
        elements = {
            baseElement.find_element_by_id: lambda: self.driver.find_element_by_id(mOperate["element_info"]),
            baseElement.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(mOperate["element_info"]),
            baseElement.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(mOperate['element_info'])

        }
        return elements[mOperate["find_type"]]()
