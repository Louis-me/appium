import time
from datetime import datetime

from Base.BaseApk import ApkInfo
from Base.BaseElementEnmu import Element
from Base.BaseYaml import getYam
from Base.BasePickle import *
import os
from Base.BaseFile import *


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def init():
    # getDevices = getYam(PATH("../yaml/devices.yaml"))
    # apkPath = PATH("../yaml/" + getYam(PATH("../yaml/run.yaml"))["app"])
    # print(apkPath)
    # apkInfo = ApkInfo(apkPath=apkPath)
    # for item in getDevices:
    #     # item["app"] = apkPath
    #     # item["appPackage"] = apkInfo.getApkBaseInfo()[0]
    #     # item["appActivity"] = apkInfo.getApkActivity()
    #     item["appPackage"] = "com.huawei.works"
    #     item["appActivity"] = "huawei.w3.ui.welcome.W3SplashScreenActivity"

    destroy()
    of = OperateFile(PATH("../Log/info.pickle"))
    of.mkdir_file()
    of = OperateFile(PATH("../Log/sum.pickle"))
    of.mkdir_file()

    data = read(PATH("../Log/sum.pickle"))
    # data["appName"] = apkInfo.getApkName()
    # data["appSize"] = apkInfo.getApkSize()
    # data["appVersion"] = apkInfo.getApkBaseInfo()[2]
    data["versionCode"] = "35"
    data["versionName"] = "1.3.5"
    data["packingTime"] = "2017/11/8 9:30"
    data["sum"] = 0
    data["pass"] = 0
    data["fail"] = 0
    write(data=data, path=PATH("../Log/sum.pickle"))

    # 每次都重新安装uiautomator2都两个应用
    os.popen("adb uninstall io.appium.uiautomator2.server.test")
    os.popen("adb uninstall io.appium.uiautomator2.server")
    os.popen("adb install -r "+PATH("../app/appium-uiautomator2-server-v0.1.9.apk"))
    os.popen("adb install -r "+PATH("../app/appium-uiautomator2-server-debug-androidTest.apk"))


def destroy():
    of = OperateFile(PATH("../Log/info.pickle"))
    of.remove_file()
    of = OperateFile(PATH("../Log/sum.pickle"))
    of.remove_file()

if __name__ == '__main__':
    print(destroy())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
