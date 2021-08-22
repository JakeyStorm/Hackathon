import tkinter as tk
import tkinter as tk
from tkinter import filedialog as fd
import re
import json
import tkinter.ttk as ttk
import csv
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

import re
import nltk
import os
import gensim.downloader as api
from multiprocessing import cpu_count

import pymorphy2
from gensim.models.word2vec import Word2Vec
from corus import load_lenta

from gensim.utils import simple_preprocess
from gensim.models import Word2Vec
from nltk.corpus import stopwords



class App(tk.Tk):
    def __init__(self, path, l):
        self.l = l
        super().__init__()
        self.title("Заголовки")

        columns = ("#1")
        self.tree = ttk.Treeview(self, show="headings", columns=columns)
        self.tree.heading("#1", text="Заголовок")

        ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=ysb.set)

        for contact in self.l:
            self.tree.insert("", tk.END, values=contact)
        self.tree.bind("<<TreeviewSelect>>", self.print_selection)

        self.tree.grid()
        ysb.grid()
        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=2)

    def print_selection(self, event):
        for selection in self.tree.selection():
            item = self.tree.item(selection)
            last_name = item
            print(text.format(last_name))


window = tk.Tk()
window.title("Интерфакс")

window.geometry('550x450')
window.configure(background='LightSkyBlue4')

label = tk.Label()
g = ''


def callback():
    global g
    name = fd.askopenfilename()
    label = tk.Label(text=name, bg="LightSkyBlue3")
    label.place(x=190, y=95)
    label['relief'] = RIDGE
    s = label.cget('text')

    f = open(s, 'r', encoding='utf-8')

    text = json.load(f)[0]['news'][0]['body']
    g = text
    print(g)


button = tk.Button(
    text="<Выбрать файл>",
    width=15,
    height=3,
    bg="LightSkyBlue3",
    fg="black",
    command=callback,
    overrelief=SUNKEN).place(x=30, y=80)


def search():
    b = g
    label1 = tk.Label(text="<Файл создан>", width=15,
                      height=0, bg="LightSkyBlue3")
    label1['relief'] = RIDGE
    s = open(str(b[0]) + '.txt', 'w', encoding='utf-8')
    x = {'content': b}
    y = json.dumps(x)
    s.write(y)
    label1.place(x=190, y=205)
    s1 = re.findall(r'\w+', b)
    print(s1)
    app = App(".", s1)

    app.mainloop()


button2 = tk.Button(
    text="<Сгеннерировать>",
    width=15,
    height=3,
    bg="LightSkyBlue3",
    fg="black",
    command=search,
    overrelief=SUNKEN
)


def clear():
    window.configure(background='LightSkyBlue4')
    label = tk.Label(
        text='',
        width=100,
        height=3,
        bg='LightSkyBlue4',
        fg='LightSkyBlue4'
    )
    label1 = tk.Label(text=' ',
                      width=50,
                      height=50,
                      bg='LightSkyBlue4',
                      fg="LightSkyBlue4")

    label1.place(x=190, y=95)
    label.place(x=190, y=205)


button3 = tk.Button(text="<Очистить>",
                    width=15,
                    height=3,
                    bg="LightSkyBlue3",
                    fg="black",
                    command=clear,
                    overrelief=SUNKEN,

                    )
button3.place(x=30, y=300)
button2.place(x=30, y=190)

label_interfaks = tk.Label(
    text="InterFax",
    width=10,
    height=2,
    bg="LightSkyBlue4",
    font=('Helvetica', '20'),

)

label_interfaks.place(x=200, y=5)

window.mainloop()
