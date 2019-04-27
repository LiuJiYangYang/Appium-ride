from appium import webdriver
import time,traceback
# 跳过引导页，直接执行程序，或跳过安装执行现有程序

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1.1'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'C:\Work\poutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['onReset'] = True
desired_caps['newCommandTimeout'] = 6000

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print('-----------')

driver.implicitly_wait(10)
time.sleep(1)
driver.find_element_by_id('io.manong.developerdaily:id/tab_bar_plus').click()
time.sleep(3)
print(u"登录成功")
driver.quit()
