import pyautogui
from PIL import Image, ImageGrab
import time

def isCollide(data):
    #Draw the rectangle for birds
    for x in range(280, 310):   #colomn1, colomn 2
        for y in range(340, 410):   #row1, row2
            if data[x, y] < 170:
                pyautogui.keyDown('down')
                pyautogui.keyUp('down')
                return

    #Draw the rectangle for cactus
    for i in range(350, 380):   #colomn1, colomn 2
        for j in range(450, 480):   #row1, row2
            if data[i, j] < 170:
                pyautogui.press('up')
                return

if __name__ == "__main__":
    print("Hello Dino game about to start in 3 second")
    time.sleep(3)
    pyautogui.press('up')
    
while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    isCollide(data)