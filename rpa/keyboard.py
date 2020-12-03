import pyautogui
# w = pyautogui.getWindowsWithTitle("Untitled")[0]
# w.activate()

# pyautogui.write("1234")
# pyautogui.write("Hello World", interval=0.25)


# pyautogui.write(['t','e','s','t','left','left','right','l','a','enter'], interval=0.25)
# pyautogui.keyDown("shift")
# pyautogui.press('4')
# pyautogui.press('1')
# pyautogui.keyUp("shift")

# pyautogui.keyDown('ctrl')
# pyautogui.keyDown('a')
# pyautogui.keyUp('a')
# pyautogui.keyUp('ctrl')

# pyautogui.hotkey('ctrl', 'alt', 'shift' 'a')

# pyautogui.hotkey('ctrl', 'a')


import pyperclip

# pyperclip.copy('한국어') #save stirng in clipboard
# pyautogui.hotkey('ctrl', 'v')

# def korean_write(text):
#     pyperclip.copy(text)
#     pyautogui.hotkey('ctrl', 'v')

# korean_write('한국어')
# korean_write('안녕하세여')

# stop
# win : ctrl + alt + del
# mac : cmd + shift + option + q

# print('starts in 3 sec')
# pyautogui.countdown(3)
# print("start!")
# pyautogui.alert('failed') 
# result = pyautogui.confirm('continue?')
# print(result) # ok or cancel

# result = pyautogui.prompt("name?",'input')
# print(result)  # none or input

result = pyautogui.password("enter")
print(result)  # none or input