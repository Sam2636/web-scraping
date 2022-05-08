""" from pynput.mouse import Button, Controller
mouse = Controller()
current_mouse_position = mouse.position
print(current_mouse_position)
 """

import pyautogui

s=pyautogui.position()

print(s)