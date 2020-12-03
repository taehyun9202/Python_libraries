import pyautogui
# pyautogui.mouseInfo()

# size = pyautogui.size()
# pyautogui.moveTo(100, 100, 1)

# pyautogui.move(0, 500, 0.5)
# pyautogui.move(-500, 0, 0.5)
# pyautogui.move(0, -500, 0.5)
# pyautogui.move(500, 0, 0.5)

# pyautogui.moveRel(-500,500,0.5)

# pyautogui.sleep(1)
# p = pyautogui.position()
# print(p[0], p[1])
# print(p.x, p.y)

# pyautogui.click(434, 617)
# pyautogui.click(click=100)
# pyautogui.doubleClick()

# pyautogui.moveTo(392, 64)
# pyautogui.mouseDown
# pyautogui.moveTo(434, 617, 1)
# pyautogui.mouseUp

# pyautogui.moveTo(533, 25)
# pyautogui.drag(100, 100, 0.25)
# pyautogui.dragTo(1500, 400, 0.26)


# pyautogui.scroll(-800)

# pyautogui.FAILSAFE = False
# pyautogui.PAUSE = 1 # same as sleep for every motion
# for i in range(10):
#     pyautogui.moveTo(100, 100)
#     # pyautogui.sleep(1)


# img = pyautogui.screenshot()
# img.save('screenshot.png')

# 809,28 34,167,242 #22A7F2
pixel = pyautogui.pixel(809, 28)
print(pixel)

print(pyautogui.pixelMatchesColor(809, 28, (34, 167, 242)))
print(pyautogui.pixelMatchesColor(809, 28, pixel))