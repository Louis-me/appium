from Base.BaseElementEnmu import Element
from Base.BasePickle import *
from Base.BaseFile import *

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def mk_file():
    destroy()
    mkdir_file(PATH("../Log/"+Element.INFO_FILE))
    mkdir_file(PATH("../Log/"+Element.SUM_FILE))
    mkdir_file(PATH("../Log/" + Element.DEVICES_FILE))

    data = read(PATH("../Log/"+Element.INFO_FILE))
    # data["appName"] = apkInfo.getApkName()
    # data["appSize"] = apkInfo.getApkSize()
    # data["appVersion"] = apkInfo.getApkBaseInfo()[2]
    data["versionCode"] = "40"
    data["versionName"] = "1.4.0"
    data["packingTime"] = "2017/12/4 13:00"
    data["sum"] = 0
    data["pass"] = 0
    data["fail"] = 0
    write(data=data, path=PATH("../Log/"+Element.SUM_FILE))


def init(devices):
    # 每次都重新安装uiautomator2都两个应用
    os.popen("adb -s %s uninstall io.appium.uiautomator2.server.test" % devices)
    os.popen("adb -s %s uninstall io.appium.uiautomator2.server" % devices)
    os.popen("adb -s %s install -r %s" % (devices, PATH("../app/appium-uiautomator2-server-v0.1.9.apk")))
    os.popen("adb -s %s install -r %s" % (devices, PATH("../app/appium-uiautomator2-server-debug-androidTest.apk")))
    # os.popen("adb install -r "+PATH("../app/android-system-webview-60.apk"))


def destroy():
    remove_file(PATH("../Log/"+Element.INFO_FILE))
    remove_file(PATH("../Log/"+Element.SUM_FILE))
    remove_file(PATH("../Log/"+Element.DEVICES_FILE))


if __name__ == '__main__':
    print(destroy())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
