# 项目名及简介
* 基于appium+python3封装的自动化测试框架

# 介绍
* unittest参数化
* PageObject分层管理
* 本地化多机日志管理
* 用例编写基于yaml配置多关键字驱动
* 支持多设备andoird并行
* 支持失败重连
* 自动生成excel测试报告



## 命令运行

```
python runner.py
```


# 结果展示

**日志目录**

文件夹：samsung_GT-I9500_android_4.4，包含截图

```
2017-06-07 19:39:35,972  - INFO - ----  test001_第一次打开_android.widget.ImageView   START     ----
2017-06-07 19:39:44,433  - INFO - [CheckPoint_1]: FirstOpenTest: NG
2017-06-07 19:40:02,013  - INFO - ----  test0002_登录_com.jianshu.haruki:id/btn_login   START     ----
2017-06-07 19:40:03,075  - INFO - ----  test0002_登录_com.jianshu.haruki:id/et_tel   START     ----
2017-06-07 19:40:07,460  - INFO - ----  test0002_登录_com.jianshu.haruki:id/et_password   START     ----
2017-06-07 19:40:08,480  - INFO - ----  test0002_登录_com.jianshu.haruki:id/btn_register_1   START     ----
2017-06-07 19:40:13,640  - INFO - ----  test0002_登录_//android.widget.ImageView[@index='0']   START     ----
2017-09-23 17:28:26,074  - INFO - [CheckPoint_1]: TechZoneDetailTest_请检查元素//*[@id="app"]/div/div[2]/section[2]/div[1]/div是否存在: NG
```



**测试报告**

![sum.png](Img/sum.png "sum.png")

![detail.jpg](Img/detail.jpg "detail.jpg")

# 其他 
* [测试用例关键字驱动说明](mark.md)
* [使用实例](use.md)
* [changelog](CHANGELOG.md)
* [English](English.md)





