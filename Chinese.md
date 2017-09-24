# 项目名及简介
* 基于appium+python3封装的自动化测试框架

# 功能
* python3
* unittest参数化
* objectpage
* 数据维护用的YMAL
* excel的测试报告
* 支持多设备andoird并行

# 常用目录
* Base封装常用方法
* Log记录不同设备的操作用例的日志，操作失败的截图
* PageObject 放page
* test目录写测试用例
* runner 运行入口


# 配置





# 实例-第一次启动app


**配置用例yaml**

```
testinfo:
    - id: test001
      title: 第一次打开
testcase:
    - operate_type: swipeLeft
      time: 4
      element_info: android.widget.ImageView
      find_type: class_name
    - element_info: com.jianshu.haruki:id/tv_enter
      find_type: id
      operate_type: click
check:
    - element_info: com.jianshu.haruki:id/btn_login
      find_type: id
```



**PageObject**

```
class FirstOpen:
    '''
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
        self.testInfo = getYam(self.path)["testinfo"]
        self.testCase = getYam(self.path)["testcase"]


    '''
    操作步骤
    logTest 日记记录器
    '''

    def operate(self, logTest):
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)

            if not result:
                print("操作失败")
                self.isOperate = False
                break

    '''
    检查点
    caseName:函数名
    logTest 记录日志：一个手机记录单独记录一个日志
    '''

    def checkPoint(self, caseName, logTest, devices):
        result = False
        if not self.isOperate:
            print("操作失败,检查点失败")
            # return self.isOperate
        else:
            check = getYam(self.path)["check"]
            result = self.operateElement.findElement(check)  # 检查点

        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=caseName, driver=self.driver, logTest=logTest, devices=devices)
        return result

```


**test**

```
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class FirstOpenTest(ParametrizedTestCase):
    def testFirst(self):
        firsOpen = FirstOpen(driver=self.driver, path=PATH("../yaml/firstOpen.yaml"))
        firsOpen.operate(logTest=self.logTest)
        firsOpen.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])


    def setUp(self):
        super(FirstOpenTest, self).setUp()
```

# 实例-登录

**配置yaml**

```
testinfo:
    - id: test0002
      title: 登录
testcase:
    - element_info: com.jianshu.haruki:id/btn_login
      find_type: id
      operate_type: click
    - element_info: com.jianshu.haruki:id/et_tel
      find_type: id
      operate_type: set_value
      text: username
    - element_info: com.jianshu.haruki:id/et_password
      find_type: id
      operate_type: set_value
      text: pwd
    - element_info: com.jianshu.haruki:id/btn_register_1
      find_type: id
      operate_type: click
    - element_info: //android.widget.ImageView[@index='0']
      find_type: xpath
      operate_type: click
check:
    - element_info: com.jianshu.haruki:id/add_subscribe
      find_type: id
    - element_info: com.jianshu.haruki:id/tab_more
      find_type: id
```



**PageObject**

```
class Login:
    '''
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
        self.testInfo = getYam(self.path)["testinfo"]
        self.testCase = getYam(self.path)["testcase"]

    '''
    操作步骤
     logTest 日记记录器
    '''

    def operate(self, logTest):
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)

            if not result:
                print("操作失败")
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
        if not self.isOperate:
            print("操作失败,检查点失败")
        else:
            check = getYam(self.path)["check"]
            result = self.operateElement.findElement(check)  # 检查点

        countSum(result)
        countInfo(result=result, testInfo=self.testInfo, caseName=caseName, driver=self.driver, logTest=logTest, devices=devices)
        return result
```

**test**

```
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class LoginTest(ParametrizedTestCase):

    def testLogin(self):
        login = Login(driver=self.driver, path=PATH("../yaml/login.yaml"))
        login.operate(logTest=self.logTest)
        login.checkPoint(caseName=self.__class__.__name__, logTest=self.logTest, devices=self.devices["deviceName"])

    # def testWrongPwd(self):
    #     pass

    def setUp(self):
        super(LoginTest, self).setUp()
```

# 代码入口实例

```
def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(FirstOpenTest, param=devices)) # 引用不同的测试类
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest, param=devices)) # 引用不同的测试类
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒"
	
	...
	
	
if __name__ == '__main__':
    devicess = AndroidDebugBridge().attached_devices()
    if len(devicess) > 0:
        l_devices = []
        init()
        for devices in devicess:
            app = {}
            port = random.randint(4700, 4900)
            bpport = random.randint(4700, 4900)
            app["port"] = str(port)
            app["devices"] = devices
            l_devices.append(app)
            appium_server = AppiumServer(port=port, bport=bpport, devices=devices)
            appium_server.start_server()
            while not appium_server.is_runnnig():
                time.sleep(2)
        runnerPool(l_devices)
        stopAppiumMacAndroid(l_devices)
        writeExcel()
    else:
        print("没有可用的安卓设备")

```

## 命令运行

```
python runner.py
```


# 结果展示

**日志目录**

文件夹：samsung_GT-I9500_android_4.4，包含截图

```
2017-06-07 19:39:35,972  - INFO - ----  test001_第一次打开_android.widget.ImageView   START     ----
2017-06-07 19:39:44,433  - INFO - [CheckPoint_1]: FirstOpenTest: NG
2017-06-07 19:40:02,013  - INFO - ----  test0002_登录_com.jianshu.haruki:id/btn_login   START     ----
2017-06-07 19:40:03,075  - INFO - ----  test0002_登录_com.jianshu.haruki:id/et_tel   START     ----
2017-06-07 19:40:07,460  - INFO - ----  test0002_登录_com.jianshu.haruki:id/et_password   START     ----
2017-06-07 19:40:08,480  - INFO - ----  test0002_登录_com.jianshu.haruki:id/btn_register_1   START     ----
2017-06-07 19:40:13,640  - INFO - ----  test0002_登录_//android.widget.ImageView[@index='0']   START     ----
2017-09-23 17:28:26,074  - INFO - [CheckPoint_1]: TechZoneDetailTest_请检查元素//*[@id="app"]/div/div[2]/section[2]/div[1]/div是否存在: NG
```



**测试报告**

![sum.png](Img/sum.png "sum.png")

![detail.jpg](Img/detail.jpg "detail.jpg")






