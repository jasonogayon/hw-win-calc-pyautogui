import pyautogui, time

pauseSeconds = 0.3

# Open Windows Calculator via CLI
pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('calc', pause=pauseSeconds)
pyautogui.press('enter', pause=pauseSeconds)

# Wait for the Calculator: 2 Seconds
time.sleep(2)

# Addition
pyautogui.press('escape', pause=pauseSeconds)
pyautogui.press('7', pause=pauseSeconds)
pyautogui.press('+', pause=pauseSeconds)
pyautogui.press('3', pause=pauseSeconds)
pyautogui.press('enter', pause=pauseSeconds)

# Subtraction
pyautogui.press('escape', pause=pauseSeconds)
pyautogui.press('7', pause=pauseSeconds)
pyautogui.press('-', pause=pauseSeconds)
pyautogui.press('3', pause=pauseSeconds)
pyautogui.press('enter', pause=pauseSeconds)

# Multiplication
pyautogui.press('escape', pause=pauseSeconds)
pyautogui.press('7', pause=pauseSeconds)
pyautogui.press('*', pause=pauseSeconds)
pyautogui.press('3', pause=pauseSeconds)
pyautogui.press('enter', pause=pauseSeconds)

# Division
pyautogui.press('escape', pause=pauseSeconds)
pyautogui.press('7', pause=pauseSeconds)
pyautogui.press('/', pause=pauseSeconds)
pyautogui.press('3', pause=pauseSeconds)
pyautogui.press('enter', pause=pauseSeconds)

# Close Calculator
pyautogui.press('escape', pause=pauseSeconds)
pyautogui.hotkey('alt', 'f4')
