import tkinter
import pyautogui as autop
import cv2
from tkinter import *
from tkinter import ttk
import time
import os

#ウィンドウ幅と高さの設定(変更可)
width = 600
height = 400

wh = str(width) + 'x' + str(height)

item = tkinter.Tk()
item.title(u"簡易モザイクフィルター")
item.geometry(wh + "+0+0")
item.resizable(width = False, height = False)
item.config(bg="#ffffff")
item.attributes("-transparentcolor", "#ffffff")
item.state('zoomed')

menubar = tkinter.Menu(item)
item.config(menu=menubar)

#現在座標取得(win32guiが動かなかったため断念-今後改善予定)

i = 0
while True:
    #スクリーンショット(範囲指定)
    i += 1
    picturename = "screenshot" + str(i) + ".png"
    screenshot = autop.screenshot()
    screenshot.save(r"./picture/" + picturename)

    #モザイク処理
    address = cv2.imread("./picture/" + picturename)
    def filter(address):
        small = cv2.resize(address, None, fx = 0.2, fy = 0.2, interpolation=cv2.INTER_NEAREST)
        return cv2.resize(small, address.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    filterimg = filter(address)
    cv2.imwrite(r"./picture/"  + picturename,filterimg)

    #画像表示(処理後)
    imgadress = PhotoImage(file="./picture/" + picturename)
    canvas = Canvas(bg="black", width = 1920, height = 1080)
    canvas.place(x = 0, y = 0)
    canvas.create_image(1, 1, image=imgadress, anchor=NW)
    time.sleep(0.5)

    #画像削除
    try:
        os.remove(r"./picture/screenshot" + str(i - 3) + ".png")
        if (i >= 5):
            break
    except:
        pass
item.mainloop()