import os
import pyautogui
import sys
import pyperclip
pyautogui.hotkey('win', 'r')
pyautogui.write('mspaint')
pyautogui.press('enter')

pyautogui.sleep(0.5)
paint = pyautogui.getWindowsWithTitle('untitled')[0]
# if paint.isMaximized == False:
    # paint.maximize()
# print(os.getcwd())
image = "pygui/paint_text.png"
paint_text = pyautogui.locateOnScreen(image)
if paint_text:
    pyautogui.click(paint_text)
else:
    print("can't find button")
    sys.exit()

pyautogui.move(0, 200)
pyautogui.click()

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')

my_write("안녕")

pyautogui.countdown(3)
paint.close()
pyautogui.sleep(0.5)
pyautogui.press('n')