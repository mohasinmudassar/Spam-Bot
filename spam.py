import pyautogui, time
import webbrowser as wb
c_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'  #give your searching application path

wb.get (c_path).open('web.whatsapp.com')
time.sleep(5)
f = open("script.txt" , 'r')
#wb.open ("web.whatsapp.com")
time.sleep(30)
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")