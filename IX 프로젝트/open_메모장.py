import pyautogui as pag
import time

if __name__=='__main__':
    pag.moveTo(100, 1100, 2)
    pag.click()
    pag.press("hangul")
    pag.typewrite("apahwkd")
    pag.press("hangul")
    pag.sleep(2)
    pag.press("enter")
    pag.moveTo(100, 800, 2)
    pag.typewrite("Hello World")
    pag.press("enter")
    pag.press("enter")
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")
    pag.press("hangul")
    pag.hotkey('ctrl', 's')
    pag.sleep(1)
    pag.typewrite("bkdlTjsdnjfem")

