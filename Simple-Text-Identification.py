try:
    import Image
except ImportError:
    from PIL import Image
import os
import keyboard
import pytesseract
import pyscreenshot
import pyautogui

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

x = 0
y = 0
x1 = 0
y1 = 0


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


def imageGrab():
    global x, y, x1, y1
    im = pyscreenshot.grab(bbox=(x, y, x1, y1))
    return im


def imageShow():
    global x, y, x1, y1
    im = pyscreenshot.grab(bbox=(x, y, x1, y1))
    im.show()
    # pyscreenshot.grab_to_file('im.png')  # to file


def setCursorPosTL():  # Top Left
    global x, y
    x, y = pyautogui.position()
    print(pyautogui.position())


def setCursorPosBR():  # Bottom Right
    global x1, y1
    x1, y1 = pyautogui.position()
    print(pyautogui.position())


def writeText():
    # picT = pytesseract.image_to_string(Image.open('Unbenannt2.PNG'))
    picT = pytesseract.image_to_string(imageGrab())
    keyboard.press_and_release('backspace')
    if picT == "":
        print("Kein Text erkannt.")
    else:
        keyboard.write(picT)
        print(picT)
        # keyboard.press_and_release('Enter')


def clipText():
    picT = pytesseract.image_to_string(imageGrab())
    print(picT)
    addToClipBoard(picT)


print("set topleft: a | set bottomright: s | write text: d | clipboard: f | showImage: g")
keyboard.add_hotkey('a', setCursorPosTL)
keyboard.add_hotkey('s', setCursorPosBR)
keyboard.add_hotkey('d', writeText)
keyboard.add_hotkey('f', clipText)
keyboard.add_hotkey('g', imageShow)
while True:
    pass
