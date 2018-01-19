
class Element(object):
    find_element_by_id = "id"
    find_elements_by_id = "ids"
    INDEX = "index"
    find_elements_by_xpath = "xpaths"
    find_element_by_xpath = "xpath"
    find_element_by_css_selector = "css"
    find_element_by_class_name = "class_name"
    CLICK = "click"
    TAP = "tap"
    ACCESSIBILITY = "accessibility"

    ADB_TAP = "adb_tap"

    SWIPE_DOWN = "swipe_down"
    SWIPE_UP = "swipe_up"

    SWIPE_LEFT = "swipe_left"
    SET_VALUE = "set_value"
    GET_VALUE = "get_value"
    WAIT_TIME = 20
    PRESS_KEY_CODE = "press_keycode"

    GET_CONTENT_DESC = "get_content_desc"

    RE_CONNECT = 1 # 是否打开失败后再次运行一次用例

    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    DEVICES_FILE = "devices.pickle"
    REPORT_FILE = "Report.xlsx"
