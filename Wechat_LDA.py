# coding=utf-8
import codecs
from multiprocessing import cpu_count
import numpy as np
import jieba
import sys
from gensim import corpora
from gensim.models.word2vec import LineSentence
from gensim.models import TfidfModel, LdaMulticore
import logging

from unicodecsv.py2 import UnicodeWriter

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)


stopwords = [stopwords[:-1] for stopwords in codecs.open('stop_words.txt', encoding='utf8', mode='r')]


def train_lda():
	"""
	Usage: python Wechat_LDA.py wechat.csv
	"""
	with open(sys.argv[1], 'r') as wx:
		for f in wx:
			seg = jieba.cut(f)
			seg = [word for word in seg if word not in stopwords]
			with codecs.open('wechat_seg.txt', encoding='utf-8', mode='ab') as wx_seg:
				wx_seg.write(' '.join(seg))

	documents = open('wechat_seg.txt', 'r')
	dictionary = corpora.Dictionary(LineSentence(documents))
	corpus = [dictionary.doc2bow(text) for text in LineSentence(documents)]
	tfidf_model = TfidfModel(corpus, id2word=dictionary, normalize=True)
	tfidf_model.save('wechat_seg.txt.tfidf_model')
	# corpora.MmCorpus.serialize('wechat_seg.txt.tfidf_model.mm', tfidf_model[corpus])
	lda_model = LdaMulticore(corpus, id2word=dictionary, num_topics=100, workers=cpu_count()-1)
	lda_model.save('wechat_lda_model.pkl')

	topics = []
	for doc in corpus:
		topics.append(lda_model[doc])

	counts = np.zeros(100)
	for top_doc in topics:
		for ti, _ in top_doc:
			counts[ti] += 1

	words = lda_model.show_topic(counts.argmax(), 64)
	with open('top_words.txt', 'w') as tw:
		writer = UnicodeWriter(tw)
		for w in words:
			writer.writerow((w[0], int(float(w[1])*1000)))


if __name__ == '__main__':
	train_lda()