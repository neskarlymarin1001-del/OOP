import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("400x400")
top.title("Queue")

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        self.element.append((text_Box.get(1.0, "end-1c")))
        text_Box.delete(1.0, "end")

    def dequeue(self):
        if len(self.element) > 0:
            removed = self.element.pop(0)
        else:
            label.config(text="Queue is empty")

    def displayQueue(self):
        if len(self.element) == 0:
            label.config(text="Queue is empty")
        else:
            r = "Queue: "
            for i in self.element:
                r += i + ", "
            r = r[:-2]
            label.config(text=r)

def show(x):
    try:
        if x == "CreateQ":
            q1.enqueue()
        elif x == "Dequeue":
            q1.dequeue()
        elif x == "Display":
            q1.displayQueue()
    except Exception as e:
        label.config(text="There was an error")

text_Box = Text(top, height=2, width=20)
text_Box.place(x=130, y=50)

EnqueueButton = Button(top, text="Enqueue", width=10, height=2, command=lambda: show("CreateQ"))
EnqueueButton.place(x=60, y=120)

DequeueButton = Button(top, text="Dequeue", width=10, height=2, command=lambda: show("Dequeue"))
DequeueButton.place(x=160, y=120)

DisplayButton = Button(top, text="Display", width=10, height=2, command=lambda: show("Display"))
DisplayButton.place(x=260, y=120)

label = Label(top, text="Queue: ")
label.place(x=80, y=200)

q1 = Queue()

top.mainloop()

