from time import sleep
import yaml

class AndroidPage:
    def __init__(self, driver, path):
        self.d = driver
        self.r = self.read_yaml(path)

    def read_yaml(self, path):
        with open(path, encoding='utf-8') as f:
            x = yaml.load(f)
            return x

    def test_plus(self):
        self.d.find_element_by_xpath(self.r["testcase1"]).click()
        self.d.find_element_by_id("com.android.calculator2:id/plus").click()
        self.d.find_element_by_xpath(self.r["testcase2"]).click()
        self.d.find_element_by_id("com.android.calculator2:id/equal").click()

    def check(self):
        result = self.d.find_element_by_xpath(self.r["check"])
        if result is not None:
            print("测试通过")
        else:
            print("测试失败")