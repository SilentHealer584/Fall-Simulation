from tkinter import *
from tkinter.ttk import *
import time

root = Tk()

wid = 800
high = 800

res = str(wid) + "x" + str(high)

root.geometry("500x500")
root.resizable(False, False)
root.title("Real Physics Simulator 1.0")

canvas = Canvas(root, width='480', height='500')
rectangle = canvas.create_rectangle(220, 220, 260, 260, fill = "black")
canvas.pack()




def coordsys(x, y):
    if y >= 470:
        if x <= 20:
            canvas.coords(rectangle, 0, 450, 40, 490)
            root.update()
            
        elif x >= 460:
            canvas.coords(rectangle, 440, 450, 480, 490)
            root.update()
            
        else:
            canvas.coords(rectangle, x-20, 450, x+20, 490)
            root.update()
    
    elif y <= 30:
        if x <= 20:
            canvas.coords(rectangle, 0, 10, 40, 50)
            root.update()
            
        elif x >= 460:
            canvas.coords(rectangle, 440, 10, 480, 50)
            root.update()
            
        else:
            canvas.coords(rectangle, x-20, 10, x+20, 50)
            root.update()
        
    elif x <= 20:
        canvas.coords(rectangle, 0, y-20, 40, y+20)
        root.update()
        
    elif x >= 460:
        canvas.coords(rectangle, 440, y-20, 480, y+20)
        root.update()
        
    else:
        canvas.coords(rectangle, x-20, y-20, x+20, y+20)
        root.update()



def gravity():
    global action
    action = True
    start = time.time()
    while action == True:

        xtrash, xcords, ytrash, ycords = canvas.coords(rectangle)
        if xcords >= 450:
            break
            
        else:
            canvas.move(rectangle, 0, (start-time.time())**2)
            root.update()

def launch(xforlater, yforlater, x, y):
    xmomtm = xforlater - x
    ymomtm = yforlater - y
    
    canvas.move(rectangle, xmomtm, ymomtm)



def dropstart(event):
    global action
    action = False
    x, y = event.x, event.y
    coordsys(x, y)
    
    
def dropend(event):
    global action
    action = False
    x, y = event.x, event.y
    coordsys(x, y)
    gravity()


def move(event):
    global action
    action = False
    x, y = event.x, event.y
    coordsys(x, y)
    


def vectorstart(event):
    global action, xforlater, yforlater, line
    line = canvas.create_line(-10, -10, -10, -10, fill="red", width=2)
    action = False
    x, y = event.x, event.y
    xforlater, yforlater = x, y
    coordsys(x, y)

def move1(event):
    global action
    action = False
    x, y = event.x, event.y
    canvas.coords(line, xforlater, yforlater, x, y)
    coordsys(x, y)
    
    
def vectorend(event):
    canvas.coords(line, -10, -10, -10, -10)
    global action
    action = False
    x, y = event.x, event.y
    coordsys(x, y)
    launch(xforlater, yforlater, x, y)
    
    

gravity()

root.bind('<ButtonPress-1>', dropstart)
root.bind('<B1-Motion>', move)
root.bind('<ButtonRelease-1>', dropend)

root.bind('<ButtonPress-3>', vectorstart)
root.bind('<B3-Motion>', move1)
root.bind('<ButtonRelease-3>', vectorend)

root.mainloop()








