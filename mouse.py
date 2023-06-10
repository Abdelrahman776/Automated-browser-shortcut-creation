import pyautogui 

pyautogui.click(1890,70,duration=0.01) # moving to the drop down menu on top right of brave browser then clicking
# pyautogui.click()
pyautogui.moveRel(0,677,duration=0.01)# moving to more tools option then click
pyautogui.click() 

pyautogui.moveRel(-520,30)  # from more tools choose "create shortcut" option
pyautogui.click()

pyautogui.moveTo(1110,295,duration=.2) # click on create button on the popup window
pyautogui.click()

