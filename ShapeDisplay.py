from Tkinter import *
import os
import random

master = Tk()

aButton = PhotoImage(file = "./ButA.gif")
bButton = PhotoImage(file = "./ButB.gif")
up = PhotoImage(file = "./JoystickUp.gif")
right = PhotoImage(file = "./JoystickRight.gif")
down = PhotoImage(file = "./JoystickDown.gif")
left = PhotoImage(file = "./JoystickLeft.gif")


w = Canvas(master, width=1400, height=600)
w.pack()

# def _create_circle(self, x, y, r, **kwargs):
#     return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)

# tk.Canvas.create_circle = _create_circlecanvas.create_circle(100, 120, 50, fill="blue", outline="#DDD", width=4)
# canvas.create_circle(150, 40, 20, fill="#BBB", outline="")
# # root.wm_title("Circles and Arcs")
# canvas_id = canvas.create_text(10, 10, anchor="nw")

# canvas.itemconfig(canvas_id, text="this is the text")
# canvas.insert(canvas_id, 12, "new ")

def create_circle(x, y, r, **kwargs):
    return w.create_oval(x-r, y-r, x+r, y+r, **kwargs)


previousArrangement = "";
i1 = 0;
i2 = 0;
i3 = 0;
i4 = 0;
i5 = 0;
i6 = 0;
i7 = 0;

def drawScene():
    global previousArrangement
    global i1
    global i2
    global i3
    global i4
    global i5
    global i6
    global i7

    w.delete("all")
    allTickets = open("currentNumbers.txt")
    ticketText = allTickets.read()
    if (len(filter(lambda x : x.isdigit(), ticketText.split("\n")[3].split(" "))) == 8 and previousArrangement != ticketText):
        indices = random.sample(range(0, 8), 7)
        i1 = indices[0]
        i2 = indices[1]
        i3 = indices[2]
        i4 = indices[3]
        i5 = indices[4]
        i6 = indices[5]
        i7 = indices[6]
        previousArrangement = ticketText
    allTickets.seek(0)

    for ticketIdx, ticket in enumerate(allTickets) :
        if(ticketIdx == 3):
            continue
        for numberIdx, number in enumerate(ticket.split(" ")):
            number = number.rstrip()
            if(ticketIdx == 0 and numberIdx == 5):
                color = "#ff0000"
            elif(ticketIdx == 1 and numberIdx == 5):
                color = "#ffff00"
            elif(ticketIdx == 2):
                color = "#ffa500"
            elif(ticketIdx == 3 and (numberIdx == i1 or numberIdx == i5)):
                color = "#ff69b4"
            elif(ticketIdx == 3 and (numberIdx == i2 or numberIdx == i6)):
                color = "#00ff00"
            elif(ticketIdx == 3 and (numberIdx == i3 or numberIdx == i7)):
                color = "#add8e6"
            elif(ticketIdx == 3 and numberIdx == i4):
                color = "#ffb6c1"
            else:
                color = "#BBB"

            x = 150 * (numberIdx+1)
            y = 75 + 150 * ticketIdx

            if(number.isdigit()):
                create_circle(x, y, 50, fill=color, outline="")
                w.create_text(x,y, text=number, font=("Purisa", 30), width=100)
            else:
                if(number == "a"):
                    w.create_image(x,y, image=aButton)
                if(number == "b"):
                    w.create_image(x,y, image=bButton)
                if(number == "up"):
                    w.create_image(x,y, image=up)
                if(number == "right"):
                    w.create_image(x,y, image=right)
                if(number == "down"):
                    w.create_image(x,y, image=down)
                if(number == "left"):
                    w.create_image(x,y, image=left)
    allTickets.close()
    master.after(200,lambda:drawScene())

# eins = tk.StringVar()
# data1 = tk.Label(root, textvariable=eins)
# data1.config(font=('times', 37))z54
# data1.pack()
# get_text(root,eins,"test.txt")
# print eins


drawScene()
mainloop()