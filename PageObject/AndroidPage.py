from time import sleep

class AndroidPage:
    def __init__(self, driver):
        self.d = driver

    def test_plus(self):
        self.d.find_element_by_xpath("//android.widget.Button[@text='1']").click()
        self.d.find_element_by_id("com.android.calculator2:id/plus").click()
        self.d.find_element_by_xpath("//android.widget.Button[@text='9']").click()
        self.d.find_element_by_id("com.android.calculator2:id/equal").click()

    def check(self):
        result = self.d.find_element_by_xpath("//android.widget.EditText[@text='10']")
        if result is not None:
            print("测试通过")
        else:
            print("测试失败")