from tkinter import *

def addBtn():
    global x
    x += 1
    lab1.config(text = x)           #lab1.config() : config() 函數來更改標籤元件的文字內容 (text 屬性)

def subBtn():
    global x
    x -= 1
    lab1.config(text = x)


window = Tk()
window.title("CLASS EX 1")
window.geometry("600x400+100+50")   #第一個+號:X軸位移量 第二個+號:Y軸位移量
window.config(bg="#ccddff")
x = 0

lab1 = Label(window, text=x, width=12, height=3, bg="#ccffdd")
lab1.pack()

addBtn = Button(window, text="addBtn", command=addBtn)
addBtn.pack()

subBtn = Button(window, text="subBtn", command=subBtn)
subBtn.pack()

exitBtn = Button(window, text="exitBtn", command=window.destroy, bg="red" )
exitBtn.pack()

window.mainloop() 