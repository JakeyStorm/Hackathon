import tkinter as tk
import tkinter as tk
from tkinter import filedialog as fd 
import re
import json
window = tk.Tk()
window.title("Интерфакс")

window.geometry('450x450')
window.configure(background='blue')


label = tk.Label()
g = ''
def callback():
	global g
	name = fd.askopenfilename() 
	label = tk.Label(text=name)
	label.place(x=150,y=200)
	s = label.cget('text')
	
	f = open(s,'r',encoding='utf-8')

	text = json.load(f)[0]['news'][0]['body']
	g = text
	print(g)


button = tk.Button(
	text='выбрать файл',
	width=10,
	height=3,
	bg="white",
	fg="black",
	command=callback).place(x=180,y=100)

def search():
	b = g
	label1 = tk.Label(text=b[0:10]) 
	label1.place(x=200,y=350)


button2 = tk.Button(
	text="Сгенить",
	width=10,
	height=3,
	bg="white",
	fg="black",
	command = search
)

button2.place(x=180,y=250)

window.mainloop()





