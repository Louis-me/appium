

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
    desired_caps['deviceName'] = "MXF5T15B10000039"
    desired_caps['appPackage'] = "com.huawei.works"
    desired_caps['appActivity'] = "huawei.w3.ui.welcome.W3SplashScreenActivity"
    # desired_caps['udid'] = "MXF5T15B10000039"
    desired_caps['noSign'] = "True"
    desired_caps["noReset"] = "True"
    desired_caps["unicodeKeyboard"] = "True"
    # desired_caps["automationName"]="uiautomator2"
    desired_caps["resetKeyboard"] = "True"
    remote = "http://127.0.0.1:" + "4723" + "/wd/hub"
    # desired_caps['systemPort'] = '8204'


    driver = webdriver.Remote(remote, desired_caps)
    time.sleep(4)

    driver.find_element_by_id("com.huawei.works.knowledge:id/vtb_img_right2").click()
    time.sleep(2)
    driver.find_elements_by_id("com.huawei.works.knowledge:id/browser_knowledge_history_text")[0].click()
    time.sleep(2)

    # time.sleep(2)
    # driver.press_keycode(66)
    # # time.sleep(5)
    #
    n = 1
    while n < 10:
        time.sleep(3)
        n = n + 1
        print(driver.contexts)
        for cons in driver.contexts:
            if cons.lower().startswith("webview"):
                driver.switch_to.context(cons)
                print("---切换webview---")
                print(driver.page_source)
                driver.execute_script('document.querySelectorAll("head")[0].style.display="block"')
                driver.execute_script('document.querySelectorAll("title")[0].style.display="block"')

                print(driver.find_element_by_xpath("./html/head/title").text)
                print(driver.find_element_by_xpath("/html/head/title").text)
                print(driver.find_element_by_xpath("html/head/title").text)
                print(driver.find_element_by_css_selector("head > title").text)
                # print(driver.find_element_by_xpath('//*[@id="h5-scroll"]/div[1]/div/div/div/section[3]/div[1]').text)
                return

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

run()
