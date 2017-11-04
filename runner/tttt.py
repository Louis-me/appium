

from appium import webdriver
import time
import os
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
def run():
    desired_caps = {}
    desired_caps['platformName'] = "android"
    # desired_caps['platformVersion'] = "6.0"
    desired_caps['deviceName'] = "A7J5T15722007958"
    desired_caps['appPackage'] = "com.huawei.works"
    desired_caps['appActivity'] = "huawei.w3.ui.welcome.W3SplashScreenActivity"
    # desired_caps['udid'] = "MXF5T15B10000039"
    desired_caps['noSign'] = "True"
    desired_caps["noReset"] = "True"
    desired_caps["unicodeKeyboard"] = "True"
    # desired_caps["automationName"]="uiautomator2"
    desired_caps["resetKeyboard"] = "True"
    remote = "http://127.0.0.1:" + "4723" + "/wd/hub"
    driver = webdriver.Remote(remote, desired_caps)
    time.sleep(4)

    driver.find_elements_by_id("com.huawei.works.knowledge:id/title")[0].click()
    time.sleep(3)
    driver.find_element_by_id("com.huawei.works.knowledge:id/vdr_fav").click()

    # driver.switch_to.alert.accept()

def test():
    n = 1
    a = [1,2,3,4,5,6]
    while n < 5:
        n = n + 1
        for i in a:
            print(i)
            return
        print("------")

test()
