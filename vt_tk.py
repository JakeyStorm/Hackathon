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








class App(tk.Tk):
	def __init__(self, path,l):
		self.l =l
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
	label = tk.Label(text=name,bg="LightSkyBlue3")
	label.place(x=190,y=95)
	label['relief'] = RIDGE
	s = label.cget('text')
	
	f = open(s,'r',encoding='utf-8')

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
	overrelief = SUNKEN).place(x=30,y=80)

def search():

	b = g
	label1 = tk.Label(text="<Файл создан>",width=15,
	height=0,bg="LightSkyBlue3")
	label1['relief'] = RIDGE
	s = open(str(b[0])+'.txt','w',encoding='utf-8') 
	x = {'content':b}
	y = json.dumps(x)
	s.write(y)
	label1.place(x=190,y=205)
	s1 = re.findall(r'\w+',b)
	print(s1)
	app= App(".",s1)

	app.mainloop()

		



button2 = tk.Button(
	text="<Сгеннерировать>",
	width=15,
	height=3,
	bg="LightSkyBlue3",
	fg="black",
	command = search,
	overrelief = SUNKEN
)
def clear():
	window.configure(background='LightSkyBlue4')
	label = tk.Label(
	text = '',
	width=100,
	height=3,
	bg='LightSkyBlue4',
	fg='LightSkyBlue4'
	)
	label1 = tk.Label(text = ' ',
	width=50,
	height=50,
	bg='LightSkyBlue4',
	fg="LightSkyBlue4")

	label1.place(x=190,y=95)
	label.place(x=190,y=205)
button3 = tk.Button(text="<Очистить>",
	width=15,
	height=3,
	bg="LightSkyBlue3",
	fg="black",
	command = clear,
	overrelief = SUNKEN,

)
button3.place(x=30,y=300)
button2.place(x=30,y=190)

label_interfaks = tk.Label(
	text="InterFax",
	width = 10,
	height = 2,
	bg="LightSkyBlue4",
	font = ('Helvetica', '20'),

	)

label_interfaks.place(x=200,y=5)

window.mainloop()


# import urllib.request
# import re
# import nltk

# scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
# article = scrapped_data.read()
#
# parsed_article = bs.BeautifulSoup(article, 'html.parser')
#
# paragraphs = parsed_article.find_all('p')

# article_text = ""
# f = open('f.txt', 'r',encoding='utf-8')
# paragraphs=f.read()
# print(paragraphs)


# for p in paragraphs:
#     article_text += p
# print(article_text)
# processed_article = article_text.lower()
# processed_article = re.sub('[^а-яА-Я]', ' ', processed_article)
# processed_article = re.sub(r'\s+', ' ', processed_article)

# all_sentences = nltk.sent_tokenize(processed_article)

# all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# from nltk.corpus import stopwords
# for i in range(len(all_words)):
#     all_words[i] = [w for w in all_words[i] if w not in stopwords.words('russian')]

# from nltk.corpus import stopwords
# for i in range(len(all_words)):
#     all_words[i] = [w for w in all_words[i] if w not in stopwords.words('russian')]

# from gensim.models import Word2Vec

# word2vec = Word2Vec(all_words, min_count=2)

# vocabulary = word2vec.wv.vocab
# print(vocabulary)