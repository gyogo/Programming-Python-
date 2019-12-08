import pyautogui as pag
import time #sleep때사용

if __name__=='__main__':
    pag.moveTo(200,400,2)
    pag.click()
    pag.typewrite("happy birthday to seungyeon!",interval=0.2)
    pag.press("enter") #키 입력
    pag.typewrite("happy birthday to namkyoung")
    pag.press("enter")
    pag.press("hangul")
    pag.typewrite("ryfuddk tkfkdgo")
    pag.press("hangul")