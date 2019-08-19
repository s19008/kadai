#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox as mb

def Enhancer():
    mb.showinfo("結果は...","あなたは強化系だ！")

def Emitter():
    mb.showinfo("結果は...","あなたは放出系だ！")

def Transmuter():
    mb.showinfo("結果は...","あなたは変化系だ！")

def Manipulator():
    mb.showinfo("結果は...","あなたは操作系だ！")

def Conjurer():
    mb.showinfo("結果は...","あなたは具現化系だ！")

def Specialist():
    mb.showinfo("結果は...","あなたは特質系だ！")


root = tk.Tk()
root.title('HUNTERxHUNTER性格別オーラ診断')
root.geometry("500x400")

desc_label = tk.Label(text="あなたの性格は？")
desc_label.pack()

button1 = tk.Button(
   text="単純で一途",
   width=18,
   command=Enhancer
)
button1.place(x=325, y=50)

button2 = tk.Button(
   text="短気で大雑把",
   width=18,
   command=Emitter
)
button2.place(x=325, y=180)

button3 = tk.Button(
   text="気まぐれで嘘つき",
   width=18,
   command=Transmuter
)
button3.place(x=325, y=310)

button4 = tk.Button(
   text="理屈屋・マイペース",
   width=18,
   command=Manipulator
)
button4.place(x=0, y=50)

button5 = tk.Button(
   text="神経質",
   width=18,
   command=Conjurer
)
button5.place(x=0, y=180)

button6 = tk.Button(
   text="個人主義者・カリスマ性あり",
   width=18,
   command=Specialist
)
button6.place(x=0, y=310)

root.mainloop()
