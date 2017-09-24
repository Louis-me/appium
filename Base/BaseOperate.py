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
                # if mOperate.get("is_webview", "0") == 1: # 1表示切换到webview
                #     self.switchToWebview()
                WebDriverWait(self.driver, baseElement.WAIT_TIME).until(lambda x: self.elements_by(mOperate))
                return True
        except selenium.common.exceptions.TimeoutException:
            print("查找元素"+mOperate["element_info"]+"超时")
            return False
        except selenium.common.exceptions.NoSuchElementException:
            print("查找元素" + mOperate["element_info"] + "不存在")
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
            logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + mOperate["element_info"])  # 记录日志
            if mOperate["operate_type"] == baseElement.CLICK:
                self.click(mOperate)
                return True
            if mOperate["operate_type"] == baseElement.GET_VALUE:
                return self.get_value(mOperate)
            if mOperate["operate_type"] == baseElement.SWIPELEFT:
                self.swipeLeft(mOperate)
                return True

        return False

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

                break

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
