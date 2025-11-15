import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("400x400")
top.title("Queue of Stacks")

class Stack:
    def __init__(self):
        self.element = []

    def push(self):
        self.element.append(text_Box.get(1.0, "end-1c"))
        text_Box.delete(1.0, "end")

    def __str__(self):
        return str(self.element)

class Queue:
    def __init__(self):
        self.element = []

    def enqueueStack(self, stack_obj):
        self.element.append(stack_obj)

    def dequeueStack(self):
        if len(self.element) > 0:
            removed = self.element.pop(0)
            return removed
        else:
            return None

    def displayQueue(self):
        if len(self.element) == 0:
            label.config(text="Queue is empty")
        else:
            r = "Queue of Stacks: \n"
            for i in range(len(self.element)):
                r += "Stack " + str(i+1) + ": " + str(self.element[i].element) + "\n"
            label.config(text=r)

current_stack = Stack()         
queue_of_stacks = Queue()       


def show(x):
    global current_stack

    try:
        if x == "push":
            current_stack.push()

            label.config(text="Current Stack: " + str(current_stack.element))

        elif x == "addToQueue":
            if len(current_stack.element) == 0:
                label.config(text="Current stack is empty")
                return

            queue_of_stacks.enqueueStack(current_stack)

            current_stack = Stack()

        elif x == "dequeue":
            removed = queue_of_stacks.dequeueStack()

        elif x == "displayQueue":
            queue_of_stacks.displayQueue()

    except:
        label.config(text="There was an error")

text_Box = Text(top, height=2, width=20)
text_Box.place(x=120, y=40)

PushButton = Button(top, text="Push", width=10, height=2, command=lambda: show("push"))
PushButton.place(x=20, y=120)

AddButton = Button(top, text="Add to Queue", width=10, height=2, command=lambda: show("addToQueue"))
AddButton.place(x=120, y=120)

DequeueButton = Button(top, text="Dequeue Stack", width=10, height=2, command=lambda: show("dequeue"))
DequeueButton.place(x=220, y=120)

DisplayButton = Button(top, text="Display Queue", width=10, height=2, command=lambda: show("displayQueue"))
DisplayButton.place(x=320, y=120)

label = Label(top, text="Current Stack: ")
label.place(x=20, y=220)

top.mainloop()
