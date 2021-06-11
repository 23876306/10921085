from tkinter import *
import random

def Generate():
    data = [0] * 6
    i = 0
    while i < 6 :                               #六個空格判斷是否重複
        x = random.randint(1,43)
        flag = True
        j = 0 
        while j < i and flag:
            if data[j] == x:
                flag = False
            j +=1
        if flag: 
            data[i] = x 
            i += 1
    lab1.config(text=int(data[0]))
    lab2.config(text=int(data[1]))
    lab3.config(text=int(data[2]))
    lab4.config(text=int(data[3]))
    lab5.config(text=int(data[4]))
    lab6.config(text=int(data[5]))
window = Tk()
window.title("CLASS EX 3")
window.geometry("600x400+100+50")   
window.config(bg="#ccddff")
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0

lab1 = Label(window, text=x1, width=12, height=3, bg="#ccffdd")
lab1.pack()

lab2 = Label(window, text=x2, width=12, height=3, bg="#ccffdd")
lab2.pack()

lab3 = Label(window, text=x3, width=12, height=3, bg="#ccffdd")
lab3.pack()

lab4 = Label(window, text=x4, width=12, height=3, bg="#ccffdd")
lab4.pack()

lab5 = Label(window, text=x5, width=12, height=3, bg="#ccffdd")
lab5.pack()

lab6 = Label(window, text=x6, width=12, height=3, bg="#ccffdd")
lab6.pack()

Generate_Btn = Button(window, text="Generate", command=Generate)
Generate_Btn.pack()

exitBtn = Button(window, text="exitBtn", command=window.destroy)
exitBtn.pack()

window.mainloop()