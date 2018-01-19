# ��Ŀ�������
* ����appium+python3��װ���Զ������Կ��

# ����
* python3
* unittest������
* objectpage
* ����ά���õ�YMAL
* excel�Ĳ��Ա���
* ֧�ֶ��豸andoird����

# ����Ŀ¼
* Base��װ���÷���
* Log��¼��ͬ�豸�Ĳ�����������־������ʧ�ܵĽ�ͼ
* PageObject ��page
* testĿ¼д��������
* runner �������


# ����





# ʵ��-��һ������app


**��������yaml**

```
testinfo:
    - id: test001
      title: ��һ�δ�
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
    kwargs: WebDriver driver, String path(yaml���ò���)
    isOperate: ����ʧ�ܣ������ʧ��
    testInfo��
    testCase��
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True
        self.testInfo = getYam(self.path)["testinfo"]
        self.testCase = getYam(self.path)["testcase"]


    '''
    ��������
    logTest �ռǼ�¼��
    '''

    def operate(self, logTest):
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)

            if not result:
                print("����ʧ��")
                self.isOperate = False
                break

    '''
    ����
    caseName:������
    logTest ��¼��־��һ���ֻ���¼������¼һ����־
    '''

    def checkPoint(self, caseName, logTest, devices):
        result = False
        if not self.isOperate:
            print("����ʧ��,����ʧ��")
            # return self.isOperate
        else:
            check = getYam(self.path)["check"]
            result = self.operateElement.findElement(check)  # ����

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

# ʵ��-��¼

**����yaml**

```
testinfo:
    - id: test0002
      title: ��¼
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
    kwargs: WebDriver driver, String path(yaml���ò���)
    isOperate: ����ʧ�ܣ������ʧ��
    testInfo��
    testCase��
    '''

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.path = kwargs["path"]
        self.operateElement = OperateElement(self.driver)
        self.isOperate = True
        self.testInfo = getYam(self.path)["testinfo"]
        self.testCase = getYam(self.path)["testcase"]

    '''
    ��������
     logTest �ռǼ�¼��
    '''

    def operate(self, logTest):
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, logTest)

            if not result:
                print("����ʧ��")
                self.isOperate = False
                break
    '''
    ����
    caseName:�������������� ����ͳ��
    logTest�� ��־��¼
    devices �豸��
    '''

    def checkPoint(self, caseName, logTest, devices):
        result = False
        if not self.isOperate:
            print("����ʧ��,����ʧ��")
        else:
            check = getYam(self.path)["check"]
            result = self.operateElement.findElement(check)  # ����

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

# �������ʵ��

```
def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(FirstOpenTest, param=devices)) # ���ò�ͬ�Ĳ�����
    suite.addTest(ParametrizedTestCase.parametrize(LoginTest, param=devices)) # ���ò�ͬ�Ĳ�����
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "��"
	
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
        print("û�п��õİ�׿�豸")

```

## ��������

```
python runner.py
```


# ���չʾ

**��־Ŀ¼**

�ļ��У�samsung_GT-I9500_android_4.4��������ͼ

```
2017-06-07 19:39:35,972  - INFO - ----  test001_��һ�δ�_android.widget.ImageView   START     ----
2017-06-07 19:39:44,433  - INFO - [CheckPoint_1]: FirstOpenTest: NG
2017-06-07 19:40:02,013  - INFO - ----  test0002_��¼_com.jianshu.haruki:id/btn_login   START     ----
2017-06-07 19:40:03,075  - INFO - ----  test0002_��¼_com.jianshu.haruki:id/et_tel   START     ----
2017-06-07 19:40:07,460  - INFO - ----  test0002_��¼_com.jianshu.haruki:id/et_password   START     ----
2017-06-07 19:40:08,480  - INFO - ----  test0002_��¼_com.jianshu.haruki:id/btn_register_1   START     ----
2017-06-07 19:40:13,640  - INFO - ----  test0002_��¼_//android.widget.ImageView[@index='0']   START     ----
2017-09-23 17:28:26,074  - INFO - [CheckPoint_1]: TechZoneDetailTest_����Ԫ��//*[@id="app"]/div/div[2]/section[2]/div[1]/div�Ƿ����: NG
```



**���Ա���**

![sum.png](Img/sum.png "sum.png")

![detail.jpg](Img/detail.jpg "detail.jpg")






