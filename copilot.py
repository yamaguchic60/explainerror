import pyautogui

def copilot():
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', 'alt', 'i') 
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'shift', 'enter')
    pyautogui.hotkey('ctrl', '1')

if __name__ == "__main__":
    copilot()
