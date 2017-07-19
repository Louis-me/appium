# project and introduction
* automated testing framework based on appium+python3 

# outline
* python3
* unittest  parameterization
* objectpage
* testcase use YMAL
* excel show report
* multi device Andoird parallel

# project package
* Base
* Log logs of operating cases for different devices, and screenshots of failed operations
* PageObject 
* test
* runner 


# configure

**configure run.yaml**

```
app: Jianshu.apk
```

**configure devices.yaml**

```
 - devices:  emulator-5554
   port: 4724
   config: appium --session-override  -p 4724 -bp 4734 -U  emulator-5554
   platformName: android
 - devices: DU2TAN15AJ049163
   port: 4725
   config: appium --session-override  -p 4725 -bp 4735 -U  DU2TAN15AJ049163
   platformName: android

```

# Example - first boot app


**configure yaml**

```
testinfo:
    - id: test001
      title: first open app
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
    kwargs: WebDriver driver, String path
    isOperate: The operation failed and the checkpoint failed
    testInfo£º
    testCase£º
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True
        self.testInfo = getYam(self.path)["testinfo"]
        self.testCase = getYam(self.path)["testcase"]


    '''
    operate steps
    logTest logger
    '''

    def operate(self, logTest):
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)

            if not result:
                self.isOperate = False
                break

    '''
    checkpoint
    caseName
    logTest 
    '''

    def checkPoint(self, caseName, logTest, devices):
        result = False
        if not self.isOperate:
            print("he operation failed and the checkpoint failed")
            # return self.isOperate
        else:
            check = getYam(self.path)["check"]
            result = self.operateElement.findElement(check)

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





# main funciton code

- runner.py

```
def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(FirstOpenTest, param=devices)) # Reference different testcase classes
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest, param=devices))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds)
	
	...
	
	
if __name__ == '__main__':
    if AndroidDebugBridge().attached_devices():
        getDevices = init()
        appium_server = AppiumServer(getDevices)
        appium_server.start_server()
        while not appium_server.is_runnnig():
            time.sleep(2)
        runnerPool(getDevices)
        appium_server.stop_server()
        writeExcel()
    else:
        print("Device does not exist")
```



# show report

**log**

samsung_GT-I9500_android_4.4£¬screenshot

```
2017-06-07 19:39:35,972  - INFO - ----  test001_FirstOpenTest_android.widget.ImageView   START     ----
2017-06-07 19:39:44,433  - INFO - [CheckPoint_1]: FirstOpenTest: NG
........

```

**excel report**

![sum.png](Img/sum.png "sum.png")

![detail.png](Img/detail.PNG "detail.png")


# other
* [Chinese](Chinese.md)






