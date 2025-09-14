# pyinstaller --onefile --add-data "../venv/Lib/site-packages/uiautomator2;uiautomator2" phone.py
import time
import uiautomator2 as u2

# 连接设备
# d = u2.connect("192.168.0.142:5555")

# d = u2.connect("192.168.0.103:5555")

# d = u2.connect("192.168.71.103:5555")

# d = u2.connect("192.168.0.13:5555")
# adb tcpip 5555
# adb connect 192.168.1.4:5555

d = u2.connect("192.168.1.4:5555")

#网页
d.press("home")
d.press("home")
d(description="Edge").click()
d(resourceId="com.microsoft.emmx:id/edge_location_bar_center").click()
time.sleep(1)
d.click(0.526, 0.331)
d(resourceId="com.microsoft.emmx:id/overflow_button_bottom").click()
d.xpath('//*[@resource-id="com.microsoft.emmx:id/grid_view"]/android.widget.FrameLayout[7]/android.view.ViewGroup[1]').click()
d(resourceId="com.microsoft.emmx:id/name", text="篡改猴").click()
time.sleep(1)
d.xpath('//*[@text="开始 ("]').click()

#新闻


d.press("home")
d.xpath('//*[@text="微软必应"]').click()
for i in range(25):
    d.swipe(0.816, 0.697,0.806, 0.144,0.8)
    time.sleep(1)
    d.click(0.496, 0.4)
    time.sleep(1)
    d.swipe(0.816, 0.697, 0.806, 0.144, 0.8)
    time.sleep(7)
    d.press("back")
