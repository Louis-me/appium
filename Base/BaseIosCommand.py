import subprocess

import os

'''
获取ios下的硬件信息
'''


def get_ios_devices():
    devices = []
    result = subprocess.Popen("ideviceinfo -k UniqueDeviceID", shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()

    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            devices.append(t[0])
    print(devices)
    return devices


def get_ios_version(udid):
    command = "ideviceinfo -u %s -k ProductVersion" % udid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


def get_ios_product_name(udid):
    command = "ideviceinfo -u %s -k DeviceName" % udid
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE).stdout.readlines()
    for item in result:
        t = item.decode().split("\n")
        if len(t) >= 2:
            return t[0]


# 编译facebook的wda到真机
def build_wda_ios(udid):
    os.popen(
        "xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination id=" + udid + " test")


if __name__ == '__main__':
    udid = get_ios_devices()[0]
    print(get_ios_product_name(udid))
