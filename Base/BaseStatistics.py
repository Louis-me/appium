import xlsxwriter

from Base.BaseAndroidPhone import getPhoneInfo
from Base.BaseElementEnmu import *
from Base.BaseExcel import OperateReport
from Base.BaseInit import destroy
from Base.BasePickle import *
from datetime import datetime

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

'''
统计数据相关
'''

'''
result bool
logTest 记录日志类 class
driver
testinfo

'''


def countInfo(**kwargs):
    get_phone = getPhoneInfo(kwargs["devices"])
    phone_name = get_phone["brand"] + "_" + get_phone["model"] + "_" + "android" + "_" + get_phone["release"]

    info = {}
    if kwargs["result"]:
        info["result"] = "通过"
    else:
        info["result"] = "失败"
        info["img"] = kwargs["logTest"].checkPointNG(driver=kwargs["driver"], caseName=kwargs["testInfo"][0]["title"],
                                                     checkPoint=kwargs["caseName"])
    info["id"] = kwargs["testInfo"][0]["id"]
    info["title"] = kwargs["testInfo"][0]["title"]
    info["caseName"] = kwargs["caseName"]
    info["phoneName"] = phone_name
    print("--------- Element.INFO--------")
    print(info)
    writeInfo(data=info, path=PATH("../Log/info.pickle"))
    print(read(PATH("../Log/info.pickle")))


def countSum(result):
    print("--------- countSum-------")
    data = {"sum": 0, "pass": 0, "fail": 0}
    _read = read(PATH("../Log/sum.pickle"))
    if _read:
        data = _read
    data["sum"] = data["sum"] + 1
    if result:
        data["pass"] = data["pass"] + 1
    else:
        data["fail"] = data["fail"] + 1
    write(data=data, path=PATH("../Log/sum.pickle"))
    print(read(PATH("../Log/sum.pickle")))


def countDate(testDate, testSumDate):
    print("--------- countDate------")
    data = read(PATH("../Log/sum.pickle"))
    print(data)
    if data:
        # data["testDate"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data["testDate"] = testDate
        # data["testSumDate"] = str((endtime - starttime).seconds) + "秒"
        data["testSumDate"] = testSumDate
        write(data=data, path=PATH("../Log/sum.pickle"))
    else:
        print("统计数据失败")


def writeExcel():
    workbook = xlsxwriter.Workbook('Report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    operateReport = OperateReport(workbook)
    operateReport.init(worksheet, read(PATH("../Log/sum.pickle")))
    operateReport.detail(worksheet2, readInfo(PATH("../Log/info.pickle")))
    operateReport.close()

    destroy()  # 删除文件
if __name__ == '__main__':
    # data = {'result': '失败', 'caseName': 'FirstOpenTest', 'title': '第一次打开', 'phoneName': 'samsung_GT-I9500_android_4.4.2', 'img': 'D:\\app\\appium\\log\\samsung_GT-I9500_android_4.4.220170607184558\\第一次打开CheckPoint_1_NG.png', 'id': 'test001'}
    # writeInfo(data, PATH("../Log/info.pickle"))
    # writeInfo(data, PATH("../Log/info.pickle"))
    _read = readInfo(PATH("../Log/info.pickle"))
    # writeExcel()