# -*- coding: utf-8 -*-
import os
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
import threading
class AppiumServer:
    def __init__(self, port, bport, devices):
        self.port = str(port)
        self.bport = str(bport)
        self.devices = devices
    def start_server(self):
        """start the appium server
        :return:
        """
        print("---------start_server----------")
        cmd = "appium --session-override  -p %s -bp %s -U %s" %(self.port, self.bport, self.devices)
        t1 = RunServer(cmd)
        p = Process(target=t1.start())
        p.start()
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
    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        url = " http://127.0.0.1:"+ self.port + "/wd/hub"+"/status"
        try:
            response = urllib.request.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()
class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)


# if __name__ == "__main__":
#
#     oo = AppiumServer()
#     oo.start_server()
#     print("strart server")
#     print("running server")
#     oo.stop_server()
#     print("stop server")