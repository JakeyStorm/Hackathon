import tkinter as tk
import tkinter as tk
from tkinter import filedialog as fd 
import re
import json
import tkinter.ttk as ttk
import csv
import tkinter as tk
import tkinter.ttk as ttk

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

window.geometry('450x450')
window.configure(background='black')


label = tk.Label()
g = ''
def callback():
	global g
	name = fd.askopenfilename() 
	label = tk.Label(text=name)
	label.place(x=150,y=90)
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
	command=callback).place(x=70,y=80)

def search():

	b = g
	label1 = tk.Label(text="файл создан",width=10,
	height=3,)
	s = open(str(b[0])+'.txt','w',encoding='utf-8') 
	x = {'content':b}
	y = json.dumps(x)
	s.write(y)
	label1.place(x=200,y=190)
	s1 = re.findall(r'\w+',b)
	print(s1)
	app= App(".",s1)

	app.mainloop()

		




button2 = tk.Button(
	text="Сгенить",
	width=10,
	height=3,
	bg="white",
	fg="black",
	command = search
)
def clear():
	window.configure(background='blue')
	label = tk.Label(
	text = '',
	width=100,
	height=3,
	bg='blue',
	fg='blue'
	)
	label1 = tk.Label(text = ' ',
	width=10,
	height=3,
	bg='blue',
	fg="blue")

	label1.place(x=200,y=190)
	label.place(x=150,y=90)
button3 = tk.Button(text="очистить",
	width=10,
	height=3,
	bg="white",
	fg="black",
	command = clear
)
button3.place(x=70,y=300)
button2.place(x=70,y=190)

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