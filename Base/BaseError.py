from Base.BaseElementEnmu import Element

"""
element_info: 元素
info: 用例说明
current: 当前值
history: 历史值
type: 错误类型
"""


def get_error(kw):
    elements = {
        Element.TIME_OUT: lambda: "==%s请求超时==" % kw["element_info"],
        Element.NO_SUCH: lambda: "==%s不存在==" % kw["element_info"],
        Element.WEB_DROVER_EXCEPTION: lambda: "==%s的driver错误==" % kw["element_info"],
        Element.INDEX_ERROR: lambda: "==%s索引错误==" % kw["element_info"],
        Element.STALE_ELEMENT_REFERENCE_EXCEPTION: lambda: "==%s页面元素已经发生==" % kw["element_info"],
        Element.DEFAULT_ERROR: lambda: "==请检查%s==" % kw["element_info"],
        Element.CONTRARY: lambda: "==检查点_%s失败_%s依然在页面==" % (kw["info"], kw["element_info"]),
        Element.CONTRARY_GETVAL: lambda: "==检查点_对比数据失败，当前取到到数据为:%s,历史取到数据为:%s" % (kw["current"], kw["history"]),
        Element.DEFAULT_CHECK: lambda: "==检查点_%s失败，请检查_%s==" % (kw["info"], kw["element_info"]),
        Element.COMPARE: lambda: "==检查点_对比数据失败，当前取到到数据为:%s,历史取到数据为:%s" % (kw["current"], kw["history"]),
        Element.TOAST: lambda: "==检查点_%s_查找弹框失败==" % kw["element_info"]
    }
    return elements[kw["type"]]()
