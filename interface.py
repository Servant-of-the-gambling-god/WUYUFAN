import tkinter as tk
import os, sys
import subprocess
from subprocess import Popen,PIPE
from xml.dom.minidom import Comment
from PIL import Image, ImageTk

route = r"C:\Users\evan\Desktop\Program\prog2-2\prog_des\ex9.exe"

def move_to_bottom():
    # 将图像移动到最下层
    canvas.tag_lower(img2)

def Return_To_Home():
    quit()

def start_game():
    ##subprocess.call('C:\\Users\\evan\\Desktop\\Program\\prog2-2\\prog_des\\test.exe')
    ##os.system(route)
    ##os.system("cd C:\Users\evan\Desktop\Program\prog2-2\prog_des")
    ##os.system("ping 8.8.8.8")
    ##os.system("gcc -o C:\Users\evan\Desktop\Program\prog2-2\prog_des\newhappyhappyhappytest.exe C:\Users\evan\Desktop\Program\prog2-2\prog_des\test.c -m32")
    subprocess.Popen("C:\\Users\\USER\\Desktop\\test\\fp\\1.exe")

def How_to_play():
    ##manual_window = tk.Tk()
    ##manual_window.geometry("950x650+25+25")
    manual_label=tk.Label(window, text = 'manual')
    window.mainloop()

# 建立主視窗 Frame
window = tk.Tk()

# 設定視窗標題
window.title('interface')


# 設定視窗大小為 1000x700，視窗（左上角）在螢幕上的座標位置為 (500, 500)
window.geometry("1230x900-0+0")

img = Image.open("C:\Users\evan\Downloads\download_image_1716740824453.png")
img2 = ImageTk.PhotoImage(img)
canvas = tk.Canvas(window, width=1230, height=900)
#canvas.pack()
canvas.create_image(0,0, anchor=tk.NW, image=img2, command=move_to_bottom)

header_label = tk.Label(window, text='\nTetris\n\n' ,width=100, height=10, font=('Times New Roman', 25, 'bold'))
header_label.pack()

# 開按鈕
button_1 = tk.Button(window, text = 'GAME START', command=start_game, width=100, height=10)
button_1.pack()

##button_2 = tk.Button(window, text = 'SETTING')
##button_2.pack()

##button_3 = tk.Button(window, text = 'MANUAL', command=How_to_play)
##button_3.pack()

button_4 = tk.Button(window, text = 'EXIT', command=Return_To_Home)
button_4.pack()

# 執行主程式
window.mainloop()
