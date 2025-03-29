import pyautogui
import tkinter as tk
from tkinter import messagebox
import time

# 创建一个列表存储点击坐标
click_positions = []

# 定义一个函数来模拟点击并记录坐标
def simulate_clicks():
    for _ in range(2):  # 模拟点击2次
        # 获取当前鼠标的坐标
        x, y = pyautogui.position()
        click_positions.append((x, y))
        
        # 在当前坐标模拟点击
        pyautogui.click(x, y)
        time.sleep(1)  # 等待1秒，以便看到鼠标点击

    # 显示弹窗
    show_popup()

# 弹窗显示坐标
def show_popup():
    root = tk.Tk()
    root.withdraw()  # 不显示主窗口，只显示弹窗

    # 格式化坐标
    coordinates = "\n".join([f"Click {i+1}: ({x}, {y})" for i, (x, y) in enumerate(click_positions)])
    
    # 弹出窗口显示点击的坐标
    messagebox.showinfo("Click Coordinates", coordinates)
    
    root.quit()

# 调用函数来模拟点击
simulate_clicks()
