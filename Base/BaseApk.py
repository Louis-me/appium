import re

__author__ = 'shikun'
from math import floor
import subprocess
import os
import json
'''
apk文件的读取信息
'''
class ApkInfo():
    def __init__(self, apkPath):
        self.apkPath = apkPath

# 得到app的文件大小
    def getApkSize(self):
        size = floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(size) + "M"


    def getApkBaseInfo(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        print(self.apkPath)
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)

        print('packagename:' + packagename)
        print('versionCode:' + versionCode)
        print('versionName:' + versionName)
        return packagename, versionName, versionCode

    #得到应用名字
    def getApkName(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        t = output.decode().split()
        for item in t:
            # print(item)
            match = re.compile("application-label:(\S+)").search(item)
            if match is not None:
                return match.group(1)


    #得到启动类

    def getApkActivity(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("launchable-activity: name=(\S+)").search(output.decode())
        if match is not None:
            return match.group(1)
if __name__ == '__main__':
    pass
    # ApkInfo(r"D:\app\appium\Img\Jianshu-2.3.1.apk").getApkActivity()
    # ApkInfo(r"D:\app\appium\Img\Jianshu-2.3.1.apk").getApkActivity()
    # # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_version()
    # # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_name()
    # ApkInfo(r"D:\app\appium_study\img\t.apk").get_apk_activity()
    # ApkInfo(r"D:\app\appium_study\Img\t.apk").get_apk_activity()


