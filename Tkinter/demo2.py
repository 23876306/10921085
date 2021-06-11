from tkinter import *
import random

def Generate():
    x = random.randint(1,100)
    lab1.config(text = x)

    
window = Tk()
window.title("CLASS EX 2")
window.geometry("600x400+100+50")   
window.config(bg="#ccddff")
x = 0

lab1 = Label(window, text=x, width=12, height=3, bg="#ccffdd")
lab1.pack()

Generate_Btn = Button(window, text="Generate", command=Generate)
Generate_Btn.pack()

exitBtn = Button(window, text="exitBtn", command=window.destroy)
exitBtn.pack()

window.mainloop()