# Write a program to draw colored shapes (line, rectangle, oval) on canvas.

from tkinter import *
root=Tk()
root.geometry("400x400")    
root.title("Shapes")
canvas=Canvas(root,width=400,height=300)
canvas.pack(side=TOP)

Frame1=Frame(root,width=400,height=100)
Frame1.pack(side=BOTTOM)

def line():
    canvas.create_line(10,10,200,200,fill="red",width=5)
    canvas.pack()
def rectangle():
    canvas.create_rectangle(10,10,200,200,fill="blue",width=5)
    canvas.pack()
def oval():
    canvas.create_oval(10,10,200,200,fill="green",width=5)
    canvas.pack()

button1=Button(Frame1,text="Line",command=line)
button1.pack(side=LEFT)
button2=Button(Frame1,text="Rectangle",command=rectangle)
button2.pack(side=LEFT)
button3=Button(Frame1,text="Oval",command=oval)
button3.pack(side=LEFT)
root.mainloop()
