import requests

# requests.packages.urllib.disable_warnings(InsecureRequestWarning)
from urllib3 import disable_warnings
from urllib3.connectionpool import InsecureRequestWarning
disable_warnings(InsecureRequestWarning)


import json

# 封装HTTP GET请求方法
def get(**kwargs):
    data = {}
    url = kwargs["protocol"] + "://"+kwargs["host"]+ kwargs["url"]
    print(url)
    r = requests.get(url, headers=kwargs.get("headers", None), verify=False)
    if r.status_code == 200 and len(r.text) > 0:
        r.encoding = 'UTF-8'
        data = json.loads(r.text)
    data["status_code"] = r.status_code
    print(data)
    return data
# 封装HTTP POST请求方法,支持上传图片
def post(files=None, **kwargs):
    result = {}
    # url = kwargs["protocol"] + "://" + kwargs["host"] + ':' + str(kwargs["port"])+ kwargs["url"]
    url = kwargs["protocol"] + "://" + kwargs["host"] + kwargs["url"]
    data = None
    if kwargs.get("data", "none") != "none":
        data = json.dumps(kwargs["data"])
        print(data)
    print(url)
    r = requests.post(url, files=files,  data=data, verify=False, headers=kwargs["headers"])
    result["status_code"] = r.status_code
    if r.status_code == 200 and len(r.text) > 0:
        r.encoding = 'UTF-8'
        result = json.loads(r.text)
    result["status_code"] = r.status_code
    return result
'''
 登陆
'''
def post_login(**kwargs):
    result = {}
    # url = kwargs["protocol"] + "://" + kwargs["host"] + ':' + str(kwargs["port"])+ kwargs["url"]
    url = kwargs["protocol"] + "://" + kwargs["host"] + kwargs["url"]
    data = None
    if kwargs.get("data", "none") != "none":
        data = json.dumps(kwargs["data"])
        print(data)
    print(url)
    r = requests.post(url, data=data, verify=False, headers=kwargs["headers"])
    if len(r.text):
        r.encoding = 'UTF-8'
        result = json.loads(r.text)
    result["status_code"] = r.status_code
    if result["status_code"] == 200:
        result["cookie"] = r.headers.get("Set-Cookie")
    print("--登陆接口--")
    print(result)
    return result