from Base.BaseLog import myLog


class Element(object):
    find_element_by_id = "id"
    find_element_by_xpath = "xpath"
    find_element_by_class_name = "class_name"
    CLICK = "click"
    TAP = "tap"
    SWIPELEFT = "swipeLeft"
    SET_VALUE = "set_value"
    WAIT_TIME = 5

    # logTest = myLog().getLog() # 其他日志记录

    INFO = []
    SUM = {"appName": "", "appSize": "", "appVersion": "", "testDate": "", "sum": 0, "pass": 0,
            "fail": 0, "testSumDate": ""}