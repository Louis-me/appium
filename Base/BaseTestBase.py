import uuid
from Base import BaseConfig
import urllib
import urllib.request
import os



def login():
    header1 = {"uuid": "8FS5T17107002234", "deviceName": "android_VIE-AL10_6.0", "appName": "WeLink",
               "traceId": "WE_28819aba-6762-43c0-9302-b49281a5e764", "needSF": "0",
               "nflag": "1", "lang": "zh", "buildCode": "84", "appVersion": "2.5.3", "osTarget": "0",
               "Content-Type": "application/x-www-form-urlencoded", "etworkType": "wifi", "isp": "unKnown",
               "User-Agent": "WeLink/2.5.3(android;android23;VIE - AL10)", "Accept-Language": "zh",
               "guid": "860075032836307kwx272211"}
    host = "w3m.huawei.com"
    protocol = "https"
    pwd = urllib.request.quote(
        "OR2ILJqjNrz9DPwLIE+bbiTKxjF+6c5yMCoqN6TgbtWupjkEvt6PS71zV1RYTENdDca7npl/sRSp9AdDEyz1JtTuFsaIJTVN8vejr1OZlm/6NCz+gQH91Jc8GORAKj5OFbWSBX98Hku7+xJbKc4eSVEMHAzDXnmrFsf0oMKYM8s=")
    loginName = urllib.request.quote(
        "Fgl7TVuYOWiknY/5Lxpi0UHIVWzpniuEsPY7mQgYpw8lgrndPtC1QNhJUQmCqgcaf3K1BZhzbJctZwGpRRXqzbL1LNZ/3HQ+aTiJxcI0O1EZreXAzZdtTBnjEi8IrB/WUbm/KB6dB9S4r0nFpznqKKcv8JCh5vClYwIKyTo5Qxo=")
    parm = "loginName=" + loginName + "&password=" + pwd + "&publicKeyFlag=0"
    url = "/mcloud/mag/LoginAutoReg?" + parm
    resp = BaseConfig.post_login(protocol=protocol, url=url, host=host, headers=header1)
    return resp.get("cookie", "0")  # 存cookie值给其他接口调用


def rm_cache(devices):
    cmd = "adb -s " + devices + " shell rm -rf  /storage/sdcard0/Huawei/HuaweiIT/WeLink/"  # 删除sd卡中的缓存
    os.system(cmd)


# 技术专区卡片排在第一位
def tech_card(cookie, devices):
    # 60111b71-4470-4e15-8bf0-557a46747587: banner
    # "cid": "a430169d-a921-403e-945c-222813c5fed1" 知识头条
    # "cid": "a69f991f8-354e-4657-aa16-99681e2f889a" 团队广场
    # 84766bfd-b0ae-4295-bdc8-5ad71c4b3b4e   政策讲话
    # "cid": "b51460a9-4e24-4187-9c9c-711b73fae9bf" 技术专区
    # "cid": "fcc42495-f803-44b4-bfc6-938c0a734589" 全联接大会
    # "cid": "7f74caff-8f95-4146-bd5b-587d43d57660" 精选博客
    # "cid": "98424416-4382-44c3-868f-8a6c0a924af5" 每日新闻
    # "cid": "f91822e8-d12a-459d-881d-76ce3c6601ce" 为您推荐
    # "cid": "92b7e9a7-5d5f-4de6-9330-1291367d004c" 销售专区
    # "cid": "d8660fbc-1b2a-4243-9d19-7cd063f61401" 营销专区
    # "cid": "fed0fdd3-19c9-4efb-959a-400572344030" GTS专区
    # "cid": "7e1cf43a-b462-4b1a-a9a6-5f7b38792003" 企业BG专区
    # "cid": "4b04ab4f-2e52-49b0-8b99-3913db800697" 供应链专区
    # "cid": "e23ec72c-61bd-47b7-8389-f9f4ffbe1160" 我的关注
    # "cid": "0d262f53-ab9c-4b4e-b6c2-41367c81e427" 我的课程
    # "cid": "b6a25e71-4a7f-4d3a-ae35-0e6ed3bc7a81" 英语学习
    # "cid": "c4ce46fc-81a8-420a-98e9-d25f9bc95010" 热点回答
    # "cid": "706a8c0a-06df-4d2b-9133-00f4c3e834c3" 视听专区
    # "cid": "64b70bed-f05c-447e-a5b4-33c196d430c8" 部门公告

    # u = https://w3m.huawei.com/mcloud/mag/ProxyForText/knowledge/api/v1/we/savesettings
    cid = "60111b71-4470-4e15-8bf0-557a46747587;a430169d-a921-403e-945c-222813c5fed1;a69f991f8-354e-4657-aa16-99681e2f889a;b51460a9-4e24-4187-9c9c-711b73fae9bf;" \
          "fcc42495-f803-44b4-bfc6-938c0a734589;7f74caff-8f95-4146-bd5b-587d43d57660;98424416-4382-44c3-868f-8a6c0a924af5;f91822e8-d12a-459d-881d-76ce3c6601ce;" \
          "92b7e9a7-5d5f-4de6-9330-1291367d004c;d8660fbc-1b2a-4243-9d19-7cd063f61401;fed0fdd3-19c9-4efb-959a-400572344030;7e1cf43a-b462-4b1a-a9a6-5f7b38792003;" \
          "4b04ab4f-2e52-49b0-8b99-3913db800697;e23ec72c-61bd-47b7-8389-f9f4ffbe1160;0d262f53-ab9c-4b4e-b6c2-41367c81e427;b6a25e71-4a7f-4d3a-ae35-0e6ed3bc7a81;" \
          "c4ce46fc-81a8-420a-98e9-d25f9bc95010;706a8c0a-06df-4d2b-9133-00f4c3e834c3;64b70bed-f05c-447e-a5b4-33c196d430c8"
    traceId = "WE-" + str(uuid.uuid1())
    header = {"Cookie": cookie, "traceId": traceId}
    host = "w3m.huawei.com"
    protocol = "https"
    url = "/mcloud/mag/ProxyForText/knowledge/api/v1/we/savesettings"
    data = {"appid": 3, "modules": [{"moduleid": 8, "settings": [{"key": "we720.hot.cn", "value": cid}]}],
            "w3account": "swx507549"}
    resp = BaseConfig.post(protocol=protocol, url=url, host=host, headers=header, data=data)
    print(resp)
    rm_cache(devices)

def dayNew_card(cookie, devices):
    cid = "60111b71-4470-4e15-8bf0-557a46747587;a430169d-a921-403e-945c-222813c5fed1;a69f991f8-354e-4657-aa16-99681e2f889a;98424416-4382-44c3-868f-8a6c0a924af5;" \
          "fcc42495-f803-44b4-bfc6-938c0a734589;7f74caff-8f95-4146-bd5b-587d43d57660;c4ce46fc-81a8-420a-98e9-d25f9bc95010;f91822e8-d12a-459d-881d-76ce3c6601ce;" \
          "92b7e9a7-5d5f-4de6-9330-1291367d004c;d8660fbc-1b2a-4243-9d19-7cd063f61401;fed0fdd3-19c9-4efb-959a-400572344030;7e1cf43a-b462-4b1a-a9a6-5f7b38792003;" \
          "4b04ab4f-2e52-49b0-8b99-3913db800697;e23ec72c-61bd-47b7-8389-f9f4ffbe1160;0d262f53-ab9c-4b4e-b6c2-41367c81e427;b6a25e71-4a7f-4d3a-ae35-0e6ed3bc7a81;" \
          "b51460a9-4e24-4187-9c9c-711b73fae9bf;706a8c0a-06df-4d2b-9133-00f4c3e834c3;64b70bed-f05c-447e-a5b4-33c196d430c8"
    traceId = "WE-" + str(uuid.uuid1())
    header = {"Cookie": cookie, "traceId": traceId}
    host = "w3m.huawei.com"
    protocol = "https"
    url = "/mcloud/mag/ProxyForText/knowledge/api/v1/we/savesettings"
    data = {"appid": 3, "modules": [{"moduleid": 8, "settings": [{"key": "we720.hot.cn", "value": cid}]}],
            "w3account": "swx507549"}
    resp = BaseConfig.post(protocol=protocol, url=url, host=host, headers=header, data=data)
    print(resp)
    rm_cache(devices)

# 热门问答
def hotAnswer_card(cookie, devices):
    cid = "60111b71-4470-4e15-8bf0-557a46747587;a430169d-a921-403e-945c-222813c5fed1;a69f991f8-354e-4657-aa16-99681e2f889a;c4ce46fc-81a8-420a-98e9-d25f9bc95010;" \
          "fcc42495-f803-44b4-bfc6-938c0a734589;7f74caff-8f95-4146-bd5b-587d43d57660;98424416-4382-44c3-868f-8a6c0a924af5;f91822e8-d12a-459d-881d-76ce3c6601ce;" \
          "92b7e9a7-5d5f-4de6-9330-1291367d004c;d8660fbc-1b2a-4243-9d19-7cd063f61401;fed0fdd3-19c9-4efb-959a-400572344030;7e1cf43a-b462-4b1a-a9a6-5f7b38792003;" \
          "4b04ab4f-2e52-49b0-8b99-3913db800697;e23ec72c-61bd-47b7-8389-f9f4ffbe1160;0d262f53-ab9c-4b4e-b6c2-41367c81e427;b6a25e71-4a7f-4d3a-ae35-0e6ed3bc7a81;" \
          "b51460a9-4e24-4187-9c9c-711b73fae9bf;706a8c0a-06df-4d2b-9133-00f4c3e834c3;64b70bed-f05c-447e-a5b4-33c196d430c8"
    traceId = "WE-" + str(uuid.uuid1())
    header = {"Cookie": cookie, "traceId": traceId}
    host = "w3m.huawei.com"
    protocol = "https"
    url = "/mcloud/mag/ProxyForText/knowledge/api/v1/we/savesettings"
    data = {"appid": 3, "modules": [{"moduleid": 8, "settings": [{"key": "we720.hot.cn", "value": cid}]}],
            "w3account": "swx507549"}
    resp = BaseConfig.post(protocol=protocol, url=url, host=host, headers=header, data=data)
    print(resp)
    rm_cache(devices)


# 技术专区卡片排在第一位
def notice_card(cookie, devices):
    cid = "60111b71-4470-4e15-8bf0-557a46747587;a430169d-a921-403e-945c-222813c5fed1;a69f991f8-354e-4657-aa16-99681e2f889a;64b70bed-f05c-447e-a5b4-33c196d430c8;" \
          "fcc42495-f803-44b4-bfc6-938c0a734589;7f74caff-8f95-4146-bd5b-587d43d57660;98424416-4382-44c3-868f-8a6c0a924af5;f91822e8-d12a-459d-881d-76ce3c6601ce;" \
          "92b7e9a7-5d5f-4de6-9330-1291367d004c;d8660fbc-1b2a-4243-9d19-7cd063f61401;fed0fdd3-19c9-4efb-959a-400572344030;7e1cf43a-b462-4b1a-a9a6-5f7b38792003;" \
          "4b04ab4f-2e52-49b0-8b99-3913db800697;e23ec72c-61bd-47b7-8389-f9f4ffbe1160;0d262f53-ab9c-4b4e-b6c2-41367c81e427;b6a25e71-4a7f-4d3a-ae35-0e6ed3bc7a81;" \
          "c4ce46fc-81a8-420a-98e9-d25f9bc95010;706a8c0a-06df-4d2b-9133-00f4c3e834c3;b51460a9-4e24-4187-9c9c-711b73fae9bf"
    traceId = "WE-" + str(uuid.uuid1())
    header = {"Cookie": cookie, "traceId": traceId}
    host = "w3m.huawei.com"
    protocol = "https"
    url = "/mcloud/mag/ProxyForText/knowledge/api/v1/we/savesettings"
    data = {"appid": 3, "modules": [{"moduleid": 8, "settings": [{"key": "we720.hot.cn", "value": cid}]}],
            "w3account": "swx507549"}
    resp = BaseConfig.post(protocol=protocol, url=url, host=host, headers=header, data=data)
    print("--技术专区卡片排在第一位--")
    print(resp)
    rm_cache(devices)


# 我的课程卡片排第一位
def myClass_card(cookie, devices):
    cid = "60111b71-4470-4e15-8bf0-557a46747587;a430169d-a921-403e-945c-222813c5fed1;a69f991f8-354e-4657-aa16-99681e2f889a;0d262f53-ab9c-4b4e-b6c2-41367c81e427;" \
          "fcc42495-f803-44b4-bfc6-938c0a734589;7f74caff-8f95-4146-bd5b-587d43d57660;98424416-4382-44c3-868f-8a6c0a924af5;f91822e8-d12a-459d-881d-76ce3c6601ce;" \
          "92b7e9a7-5d5f-4de6-9330-1291367d004c;d8660fbc-1b2a-4243-9d19-7cd063f61401;fed0fdd3-19c9-4efb-959a-400572344030;7e1cf43a-b462-4b1a-a9a6-5f7b38792003;" \
          "4b04ab4f-2e52-49b0-8b99-3913db800697;e23ec72c-61bd-47b7-8389-f9f4ffbe1160;b51460a9-4e24-4187-9c9c-711b73fae9bf;b6a25e71-4a7f-4d3a-ae35-0e6ed3bc7a81;" \
          "c4ce46fc-81a8-420a-98e9-d25f9bc95010;706a8c0a-06df-4d2b-9133-00f4c3e834c3;64b70bed-f05c-447e-a5b4-33c196d430c8"
    traceId = "WE-" + str(uuid.uuid1())
    header = {"Cookie": cookie, "traceId": traceId}
    host = "w3m.huawei.com"
    protocol = "https"
    url = "/mcloud/mag/ProxyForText/knowledge/api/v1/we/savesettings"
    data = {"appid": 3, "modules": [{"moduleid": 8, "settings": [{"key": "we720.hot.cn", "value": cid}]}],
            "w3account": "swx507549"}
    resp = BaseConfig.post(protocol=protocol, url=url, host=host, headers=header, data=data)
    print("--我的课程卡片排第一位--")
    print(resp)
    rm_cache(devices)


if __name__ == '__main__':
    pass
