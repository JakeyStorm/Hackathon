import re
import nltk
import os
import gensim.downloader as api
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec



dataset_info = api.info("text8")
dataset = api.load("text8")
word2vec_model = api.load('word2vec-google-news-300')


data =[]
for word in dataset:
    data.append(word)

data_1 = data[:1200]
data_2 = data[1200:]
w2v_model = Word2Vec(data_1, min_count=0, workers=cpu_count())


w2v_model.save('Word2VecModel')
model = Word2Vec.load('Word2VecModel')

article_text = ""
f = open('f.txt', 'r',encoding='utf-8')
paragraphs=f.read()
f_city = open('bdcity.txt', 'r')

df = f

strcity = f_city.read().split()
paragraphsSplit = paragraphs.split()
city_in_text=""
for i in range(len(strcity)):
    if strcity[i] in paragraphs:
        city_in_text = strcity[i]

f_name = open('russian_surnames.txt', 'r', encoding='utf-8')
strName = f_name.read().split()

for j in range(len(strName)):
    if strName[j] in paragraphsSplit:
        paragraphs = paragraphs.replace(strName[j]," ", 1)


import pymorphy2
from nltk.corpus import stopwords
morph = pymorphy2.MorphAnalyzer()
ru_stopwords = stopwords.words('russian')
digits = [str(i) for i in range(10)]
def preprocess(tokens):
    return [morph.normal_forms(word)[0]
            for word in tokens
                if (word[0] not in digits and
                    word not in ru_stopwords)]

for p in paragraphs:
    article_text += p
print(article_text)
processed_article = article_text.lower()
processed_article = re.sub('[^а-яА-Я]', ' ', processed_article)
processed_article = re.sub(r'\s+', ' ', processed_article)
all_sentences = nltk.sent_tokenize(processed_article)
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
from nltk.corpus import stopwords
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('russian')]
from nltk.corpus import stopwords
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('russian')]
from gensim.models import Word2Vec

word2vec = Word2Vec(all_words,min_count=1)
word2vec1 = Word2Vec(all_words,min_count=3)

vocabulary = word2vec.wv.vocab
vocabulary1 = word2vec1.wv.vocab

for i in vocabulary1.keys():
    check=i
    break

print(word2vec.wv.most_similar(check))
print(vocabulary1)

