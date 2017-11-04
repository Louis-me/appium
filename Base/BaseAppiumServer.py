# -*- coding: utf-8 -*-
import os
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
import time
import platform
import subprocess

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
import threading
class AppiumServer:
    def __init__(self, kwargs={}):
        # self.port = str(kwargs["port"])
        # print("port="+self.port)
        # self.bport = str(kwargs["bport"])
        # self.devices = kwargs["devices"]
        self.kwargs = kwargs
    def start_server(self):
        """start the appium server
        """
        for i in range(0, len(self.kwargs)):
            # print("---------start_server----------")
            cmd = "appium --session-override  -p %s -bp %s -U %s" %(self.kwargs[i]["port"], self.kwargs[i]["bport"], self.kwargs[i]["devices"])
            if platform.system() == "Windows":  # windows下，另外在匹配后续优化
                subprocess.Popen(cmd, shell=True)
            else:
                appium = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, close_fds=True)
                while True:
                    appium_line = appium.stdout.readline().strip().decode()
                    time.sleep(1)
                    if 'listener started' in appium_line or 'Error: listen' in appium_line:
                        print("----启动服务器成功---")
                        print(cmd)
                        break

    def stop_server(self):
        """stop the appium server
        selenium_appium: appium selenium
        :return:
        """
        # os.system('taskkill /f /im  node.exe')
        # mac
        cmd = "lsof -i :{0}".format("4725")
        plist = os.popen(cmd).readlines()
        plisttmp = plist[1].split("    ")
        plists = plisttmp[1].split(" ")
        # print plists[0]
        os.popen("kill -9 {0}".format(plists[0]))
    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()


# if __name__ == "__main__":
#
#     oo = AppiumServer()
#     oo.start_server()
#     print("strart server")
#     print("running server")
#     oo.stop_server()
#     print("stop server")