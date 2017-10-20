from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

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
                    # if item.get("is_webview", "0") == 1:  # 1表示切换到webview
                    #     self.switchToWebview()
                    WebDriverWait(self.driver, baseElement.WAIT_TIME).until(lambda x: self.elements_by(item))
                return True
            if type(mOperate) == dict:  # 单检查点
                WebDriverWait(self.driver, baseElement.WAIT_TIME).until(lambda x: self.elements_by(mOperate))
                return True
        except selenium.common.exceptions.TimeoutException:
            # print("查找元素"+mOperate["element_info"]+"超时")
            return False
        except selenium.common.exceptions.NoSuchElementException:
            # print("查找元素" + mOperate["element_info"] + "不存在")
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

        try:
            if self.findElement(mOperate):
                logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + mOperate["element_info"]+ "_"+mOperate.get("operate_type", " ")) # 记录日志

                if mOperate.get("operate_type", "0") == "0": # 如果没有此字段，说明没有相应操作，直接返回
                    return True

                if mOperate["operate_type"] == baseElement.CLICK:
                    self.click(mOperate)
                    return True

                if mOperate.get("is_webview", "0") == 1 and mOperate["operate_type"] == baseElement.GET_VALUE:
                    return self.get_web_value(mOperate)

                if mOperate["operate_type"] == baseElement.GET_VALUE:
                    return self.get_value(mOperate)

                if mOperate["operate_type"] == baseElement.SWIPELEFT:
                    self.swipeLeft(mOperate)
                    return True

        except selenium.common.exceptions.NoSuchElementException:
            return False

    def toast(self, message):

        # message = '//*[@text=\'{}\']'.format(message)
        element = WebDriverWait(self.driver, 10, 0.5).until(
            expected_conditions.presence_of_element_located((By.XPATH, message)))
        return element

    # 点击事件
    def click(self, mOperate):
        if mOperate["find_type"] == baseElement.find_element_by_id or mOperate["find_type"] == baseElement.find_element_by_xpath:
            self.elements_by(mOperate).click()

    '''
    切换native
    
    '''
    def switchToNative(self):
        self.driver.switch_to.context("NATIVE_APP")  # 切换到native

    '''
    切换webview
    '''
    def switchToWebview(self):
        for cons in self.driver.contexts:
            if cons.lower().startswith("webview"):
                self.driver.switch_to.context(cons)
                print("---切换webview---")
                print(self.driver.current_context)
                # print(self.driver.page_source)
                break

    # 左滑动
    def swipeLeft(self, mOperate):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        x1 = int(width * 0.75)
        y1 = int(height * 0.5)
        x2 = int(width * 0.05)
        self.driver(x1, y1, x2, y1, 600)
        # for i in range(mOperate["time"]):
        #     self.driver.swipe(width / 4 * 3, height / 2, width / 4 * 1, height / 2, 600)


    # swipe start_x: 200, start_y: 200, end_x: 200, end_y: 400, duration: 2000 从200滑动到400
    def swipeToDown(self):
        height = self.driver.get_window_size()["height"]
        x1 = int(self.driver.get_window_size()["width"]*0.5)
        y1 = int(height*0.25)
        y2 = int(height*0.75)
        self.driver.swipe(x1, y1, x1, y2, 1000)
        # self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToDown--")

    def swipeToUp(self, n=0):
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]

        for i in range(n):
            self.driver.swipe(540, 800, 540, 560, 0)
            time.sleep(2)
    #
    # def swipe_to_down(self):
    #     window_size = self.get_size()
    #
    # width = window_size.get("width")
    # height = window_size.get("height")
    # self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 1000)
    def swipeToRight(self):
        height = self.driver.get_window_size()["height"]
        width = self.driver.get_window_size()["width"]
        x1 = int(width * 0.05)
        y1 = int(height * 0.5)
        x2 = int(width * 0.75)
        self.driver.swipe(x1, y1, x1, x2, 1000)
        # self.driver.swipe(0, 1327, 500, 900, 1000)
        print("--swipeToUp--")
# start_x,start_y,end_x,end_y

# 轻打x轴向右移动x单位，y轴向下移动y单位
# def operate_tap(elemen_by,driver,element_info, xy=[]):
#     elements_by(elemen_by, driver, element_info).tap(x=xy[0], y=xy[1])

    def set_value(self, mOperate):
        '''
        输入值，代替过时的send_keys
        :param mOperate:
        :return:
        '''
        self.elements_by(mOperate).set_value(mOperate["text"])

    def get_value(self, mOperate):
        '''
        读取element的值
        :param mOperate:
        :return:
        '''

        return self.elements_by(mOperate).get_attribute("text")

    def get_web_value(self, mOperate):
        return self.elements_by(mOperate).text

# 封装常用的标签
    def elements_by(self, mOperate):
        elements = {
            baseElement.find_element_by_id: lambda: self.driver.find_element_by_id(mOperate["element_info"]),
            baseElement.find_element_by_xpath: lambda: self.driver.find_element_by_xpath(mOperate["element_info"]),
            baseElement.find_element_by_css_selector: lambda: self.driver.find_element_by_css_selector(mOperate['element_info']),
            baseElement.find_element_by_class_name: lambda: self.driver.find_element_by_class_name(mOperate['element_info'])

        }
        return elements[mOperate["find_type"]]()
        # if mOperate["find_type"] == baseElement.find_element_by_id:
        #     return self.driver.find_element_by_id(mOperate["element_info"])
        # if mOperate["find_type"] == baseElement.find_element_by_xpath:
        #     return self.driver.find_element_by_xpath(mOperate["element_info"])
        # if mOperate["find_type"] == baseElement.find_elements_by_xpath:
        #     return self.driver.find_elements_by_xpath(mOperate["element_info"])
        # if mOperate["find_type"] == baseElement.find_element_by_class_name:
        #     return self.driver.find_element_by_class_name(mOperate["element_info"])
        # if mOperate["find_type"]  == baseElement.find_element_by_css_selector:
        #     return self.driver.find_element_by_css_selector(mOperate["element_info"])
