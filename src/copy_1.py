import pyautogui
import time

# 获取用户输入的点击次数
t = int(input('输入点击总次数（0=不限制，慎用！）：'))
if t == 0:
    print('[W]您设定了不限制，您需要考虑您是否有办法关闭它！')

# 获取用户输入的点击间隔
d = float(input('输入两次点击之间的间隔（单位为秒，可以为0）：'))
if d < 0.005:
    print('[W]您设定的间隔很小，您需要考虑您的计算机或要点击的东西是否可以承受它。')

# 获取用户输入的点击键
p = int(input('点击的键（1=左键，2=右键，3=中键）：'))
print('[I]全部设置完毕！')
print('[I]你有5秒的时间移动鼠标到想要连点的地方或关闭点击器。')

# 倒计时
for i in range(5):
    print('[I]剩余', 5-i, '秒')
    time.sleep(1)

print('[I]开始点击.')

# 记录开始时间
s = time.time()
i = 0

# 执行点击
while i < t or t == 0:
    pyautogui.click(pyautogui.position())  # 获取当前鼠标位置并点击
    i += 1
    time.sleep(d)

# 记录结束时间
e = time.time()

# 输出完成信息
print('[S]点击', ['左', '右', '中'][p-1], '键', t, '次，点击间隔为', d, '的任务成功结束，共用时约', round(e-s, 2), '秒，平均每秒约点击', round(t/(e-s), 2), '次。')
