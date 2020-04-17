import tkinter


def key_pressed(event):
    if event.keysym == 'space':
        canvas.coords(oval, (300, 300, 310, 310))
        canvas.itemconfig(oval, fill='green')
    if event.keysym == 'Up':
        canvas.move(oval, 0, -10)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 10)
    elif event.keysym == 'Left':
        canvas.move(oval, -10, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 10, 0)
    if canvas.coords(oval)[1] < 200 or canvas.coords(oval)[1] > 400 or canvas.coords(oval)[0] < 200 or \
            canvas.coords(oval)[0] > 400:
        canvas.itemconfig(oval, fill='red')
    if int(canvas.coords(oval)[1]) == 600 or int(canvas.coords(oval)[0]) == 600 or \
            int(canvas.coords(oval)[1]) == 0 or int(canvas.coords(oval)[0]) == 0:
        move_wrap(canvas, oval, canvas.coords(oval))


def move_wrap(canvas, obj, move):
    if int(move[0]) == 0:
        canvas.move(obj, 590, 0)
    elif int(move[1]) == 0:
        canvas.move(obj, 0, 590)
    elif int(move[0]) == 600:
        canvas.move(obj, -590, 0)
    else:
        canvas.move(obj, 0, -590)


master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='blue', height=600, width=600)
oval = canvas.create_oval((300, 300), (310, 310), fill='green')
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
