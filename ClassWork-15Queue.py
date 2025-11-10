import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x500")

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        x = valueTxt.get(1.0, "end-1c")
        self.element.append(x)

    def dequeue(self):
        self.element.remove(0)

    def displayQueue(self):
        print("Elements in Queue: ")
        for i in self.element:
            print(i)

def show(x):
    try:
        if x == "CreateQ":
            q1.enqueue()
        elif x == "Dequeue":
            q1.dequeue()
        elif x == "Display":
            q1.displayQueue()

    except:
        print("hello")

# Main Code

B1 = Button(top, text="CreateQ", width=10, height=5, command=lambda: show("CreateQ"))
B1.place(x=100, y=150)
B2 = Button(top, text="Dequeue", width=10, height=5, command=lambda: show("Dequeue"))
B2.place(x=200, y=150)
B3 = Button(top, text="Display", width=10, height=5, command=lambda: show("Display"))
B2.place(x=200, y=150)

q1 = Queue()

top.mainloop()