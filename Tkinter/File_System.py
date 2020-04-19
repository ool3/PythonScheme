import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('400x400')
window.title('File Assistant')
window.resizable(width=False, height=False)
window['bg'] = 'white'
window.wm_attributes('-alpha', 0.95)
# list all
all_list = {}


# def
def add():
    direct = entry.get()
    text_ = entry_text.get()
    if not direct:
        messagebox.showwarning('Error 120', 'Вы не ввели директорию')
    else:
        all_list[direct] = text_


def see_text():
    if all_list:
        list_print = []
        for key, word in all_list.items():
            list_print.append(f'{key} : {word}')
        messagebox.showinfo('Окно просмотра', '\n'.join(list_print))
    else:
        messagebox.showerror('Error 404', 'Нет директорий')


def see_dir():
    if all_list:
        sort_list = sorted(all_list.keys(), key=lambda x: x.split('/')[0])

        messagebox.showinfo('Все директории', sort_list)
    else:
        messagebox.showerror('Error 101', 'Введите хотя-бы 1 директорию')


dark = False


def do_dark():
    global dark
    global text_btn
    if not dark:
        dark = True
        window['bg'] = '#2C3337'
        review['border'] = '0'
        btn_dir['border'] = '0'
    else:
        dark = False
        window['bg'] = 'white'
        review['border'] = '2'
        btn_dir['border'] = '2'


def new_window():
    global all_list
    root = tk.Tk()
    root.geometry('300x200')
    root.resizable(width=False, height=False)
    label = tk.Label(root, text='Какую директорию хотите изменить:')
    entry_root = tk.Entry(root, justify='center')

    # func
    def change():

        if entry_root.get() not in all_list:
            messagebox.showerror('Error 101', 'Такой директории нет')
        else:
            def change_file():
                all_list[entry_root.get()] = change_entry.get()

            label_2 = tk.Label(root, text='Текст:')
            change_entry = tk.Entry(root, justify='center', bg='black', fg='white')
            change_btn = tk.Button(root, text='Изменить', command=change_file)
            label_2.pack()
            change_entry.pack()
            change_btn.pack()

    btn_en = tk.Button(root, text='Check', command=change)
    label.pack()
    entry_root.pack()
    btn_en.pack()
    root.mainloop()


# create Label and entry for dir
label = tk.Label(text='Введите директорию:', font='Arial 15')
entry = tk.Entry(window, font='Consolas 15', justify='center', relief='solid')
# create Entry and label for text
entry_text = tk.Entry(window, font='Consolas 15', justify='center', relief='solid')
text = tk.Label(text='Текст:', font='Arial 15')
# btn
btn = tk.Button(text='Добавить', width=20, height=2, relief='solid', command=add)
# review all
review = tk.Button(text='Посмотреть директории',
                   width=20, height=3, bg='#ADD8E6', font='Arial 9', relief='groove', command=see_dir)
# see text with directory
btn_dir = tk.Button(text='Текст директорий', font='Arial 9', width=20,
                    height=3, relief='groove', command=see_text, bg='#ADD8E6')
# dark theme
btn_dark = tk.Button(font='Arial 8', width=6, height=3, bg='#ccc', command=do_dark)
btn_dark['text'] = 'Change\nTheme'
# btn change file
btn_file = tk.Button(font='Arial 8', width=30, height=3, bg='#4682B4',
                     command=new_window, relief='groove', fg='white')
btn_file['text'] = 'Изменить файл'
# pack
label.pack()
entry.pack()
text.pack()
entry_text.pack()
btn.place(x=125, y=130)
review.place(x=30, y=200)
btn_dir.place(y=200, x=220)
btn_dark.place(x=0, y=0)
btn_file.place(x=100, y=300)
window.mainloop()
