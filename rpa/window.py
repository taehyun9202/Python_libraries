import pyautogui

fw = pyautogui.getActiveWindow()
print(fw.title)
print(fw.size)
print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left+25, fw.top+20)


# for w in pyautogui.getAllWindows():
#     print(w.title)

# for w in pyautogui.getWindowsWithTitle("Settings"):
#     print(w)


w = pyautogui.getWindowsWithTitle("Command Prompt")[0]
if w.isActive == False:
    w.activate()

if w.isMaximized == False:
    w.maximize()

pyautogui.sleep(1)

# if w.isMinimized == False:
#     w.minimize()

w.restore()

# w.close()