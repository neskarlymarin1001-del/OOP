import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("400x400")
top.title("Stack GUI")

class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append((text_Box.get(1.0, "end-1c")))
        text_Box.delete(1.0, "end")

    def pop(self):
        if len(self.element) > 0:
            self.element.pop()
        else:
            output_label.config(text="Stack is empty")

    def displayStack(self):
        if len(self.element) == 0:
            output_label.config(text="Stack is empty")
        else:
            result = "Elements in Stack: "
            for i in self.element:
                 result = result + i + ", "
            result = result[:-2]
            output_label.config(text=result)

def show(x):
    try:
        if x == "push":
            s1.push()
        elif x == "pop":
            s1.pop()
        elif x == "display":
            s1.displayStack()
    except Exception as e:
        output_label.config(text=f"Error: {e}")

text_Box = Text(top, height=2, width=20)
text_Box.place(x=130, y=50)

B1 = Button(top, text="Push", width=10, height=2, command=lambda: show("push"))
B1.place(x=60, y=120)

B2 = Button(top, text="Pop", width=10, height=2, command=lambda: show("pop"))
B2.place(x=160, y=120)

B3 = Button(top, text="Display", width=10, height=2, command=lambda: show("display"))
B3.place(x=260, y=120)

output_label = Label(top, text="")
output_label.place(x=70, y=200)

s1 = Stack()

top.mainloop()