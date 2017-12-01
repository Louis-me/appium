

from appium import webdriver
import time
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

import os
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
def run():
    # desired_caps = {}
    # desired_caps['platformName'] = "android"
    # desired_caps['platformVersion'] = "6.0"
    # desired_caps['deviceName'] = "DU2TAN15AJ049163"
    # desired_caps['appPackage'] = "com.android.calculator2"
    # desired_caps['appActivity'] = ".Calculator'"

    # desired_caps["unicodeKeyboard"] = "True"
    # desired_caps["automationName"]="uiautomator2"
    # desired_caps["resetKeyboard"] = "True"


    # ios
    desired_caps = {}
    desired_caps['automationName'] = 'XCUITest'  # Xcode8.2以上无UIAutomation,需使用XCUITest
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '9.3.3'
    desired_caps['deviceName'] = 'iPhone 6 '
    desired_caps['bundleId'] = 'com.huawei.works'
    desired_caps['udid'] = 'fb5991a499fb96bde153923f4b9d61c68fbeee42'
    # desired_caps['app'] = PATH("../app/WeLink.ipa")
    desired_caps['newCommandTimeout'] = 3600  # 1 hour
    desired_caps['noSign'] = "True"
    desired_caps["noReset"] = "True"

    remote = "http://127.0.0.1:" + "4723" + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    driver.find_element_by_accessibility_id("知识").click()
    if driver.find_element_by_xpath("//*[starts-with(@label,'测试微群')") is not None:

        print(driver.page_source)


    # driver.find_elements_by_id("com.huawei.works.knowledge:id/title_my_team_item")[0].click()
    # time.sleep(2)
    # driver.find_element_by_id("com.huawei.works.knowledge:id/fcc_btn_more").click()
    # time.sleep(2)
    # driver.find_element_by_xpath("//android.widget.TextView[@text='wiki新']").click()
    # n = 1
    # while n < 10:
    #     time.sleep(3)
    #     n = n + 1
    #     print(driver.contexts)
    #     for cons in driver.contexts:
    #         if cons.lower().startswith("webview"):
    #             driver.switch_to.context(cons)
    #             print("---切换webview---")
    #             print(driver.page_source)
    #             return


    # driver.switch_to.alert.accept()


run()

