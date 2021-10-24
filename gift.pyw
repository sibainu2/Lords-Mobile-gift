import cv2
import math
import numpy as np
import pyautogui
from time import sleep 
import tkinter as tk
import tkinter.simpledialog as simpledialog
import glob
import os


root = tk.Tk()
root.withdraw() #小さなウィンドウを表示させない
gifuto = simpledialog.askstring("Input Box", "ギフトの数を入力してください",)


sleep(3)


screenshot1 = pyautogui.screenshot()
l=os.environ['USERNAME']
#l=glob.glob()
print(l)
screenshot1.save(r"C:\\Users\\"+l+"\\Desktop\\gift\\Photo\\gift.png")#保存先

img_rgb = cv2.imread(r"C:\\Users\\"+l+"\\Desktop\\gift\\Photo\\gift.png")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#l=glob.glob()
template = cv2.imread(r"C:\\Users\\"+l+"\\Desktop\\gift\\img\\gift.png",0)
w, h = template.shape[::-1]
threshold = 0.9
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
y,x = np.where( res >= threshold)
x = list(x)
y = list(y)
print(x,y)
try:
    gy = y[0]-130

    gift=math.ceil(int(gifuto)/4)
    print(gift)
    for r in range(gift): 
        for i in range(len(x)):
            pyautogui.click(x[i],y[i])
            sleep(0.2)
        pyautogui.click(x[0],gy)
        sleep(0.3)
except:
    print("ギフトがありません")


