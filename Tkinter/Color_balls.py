from random import *
from tkinter import *
import time
from tkinter import messagebox

# canvas and window
size = 600
root = Tk()
canvas = Canvas(root, width=size + 100, height=size + 10)
root.title('COLOR BALLS')
canvas.pack()
root.resizable(height=False, width=False)
root.wm_attributes('-alpha', 0.9)
diapason = 0
colors = ['aqua', 'blue', 'fuchsia', 'green', 'maroon', 'orange', 'pink', 'purple', 'red', 'yellow', 'violet', 'indigo',
          'chartreuse', 'lime', 'black', '#ccc', '#cce']

# func
counter = 0


def speed():
    global counter
    if counter < 0.1:
        counter += 0.01
        btn['text'] = f'speed + {int(counter * 100)}'
    else:
        messagebox.showwarning('MaxSpees', '10 it is max speed')


# btn
btn = Button(text='speed', width=20, height=5, font='Arial 10', bg='#cce', command=speed)
btn['relief'] = 'solid'
btn.place(x=230, y=450)

# create balls
while True:
    try:
        time.sleep(0.1 - counter)
    except:
        pass
    x0 = randint(0, size)
    y0 = randint(0, size - 300)
    d = randint(0, size / 5)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=choice(colors))
    root.update()
