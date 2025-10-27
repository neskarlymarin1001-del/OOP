import tkinter

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height=500, width=800)

shape1 = myCanvas.create_oval(100, 100, 300, 300, fill="blue")
shape2 = myCanvas.create_rectangle(10, 10, 100, 100, fill="pink")



myCanvas.pack()
root.mainloop()