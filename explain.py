import pyautogui

def copy():
    pyautogui.hotkey('ctrl', 'shift', 'up')
    pyautogui.hotkey('ctrl', 'shift', 'c')

def copilot():
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', 'alt', 'i')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('ctrl', 'shift', 'enter')
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', '`')

if __name__ == "__main__":
    copy()
    copilot()
