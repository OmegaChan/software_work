import jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities


stop_words = 'E:/软件工程/test/NLPIR_stopwords.txt'
stopwords = codecs.open(stop_words,'r',encoding='utf-8').readlines()
stopwords = [ w.strip() for w in stopwords ]
stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']

def token_cwj(filename):
    result = []
    with open(filename, 'r',encoding='utf-8') as f:
        text = f.read()
        words = pseg.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result

filenames = [
            'E:/软件工程/test/orig_0.8_add.txt',
    'E:/软件工程/test/orig_0.8_del.txt',
    'E:/软件工程/test/orig_0.8_dis_1.txt',
    'E:/软件工程/test/orig_0.8_dis_10.txt',
    'E:/软件工程/test/orig_0.8_dis_15.txt',

            ]


corpus_Cwj = []
for each in filenames:
    corpus_Cwj.append(token_cwj(each))

dictionary = corpora.Dictionary(corpus_Cwj)
doc_vectors = [dictionary.doc2bow(text) for text in corpus_Cwj]


tfidf = models.TfidfModel(doc_vectors)
tfidf_vectors = tfidf[doc_vectors]



lsi = models.LsiModel(tfidf_vectors, id2word=dictionary, num_topics=2)
lsi.print_topics(2)
lsi_vector = lsi[tfidf_vectors]
query = token_cwj('E:/软件工程/test/orig.txt')
query_bow = dictionary.doc2bow(query)
query_lsi = lsi[query_bow]
index = similarities.MatrixSimilarity(lsi_vector)
sims = index[query_lsi]
# print(list(enumerate(sims)))
a1 = open('requirements.txt', 'w', encoding='utf-8')
a1.write("orig.txt与orig_0.8_add.txt相似度为：" + '%.2f%%' % (list(enumerate(sims))[0][1] * 100)+"\n")
a1.write("orig.txt与orig_0.8_del.txt相似度为：" + '%.2f%%' % (list(enumerate(sims))[1][1] * 100)+"\n")
a1.write("orig.txt与orig_0.8_dis_1.txt相似度为：" + '%.2f%%' % (list(enumerate(sims))[2][1] * 100)+"\n")
a1.write("orig.txt与orig_0.8_dis_10.txt相似度为：" + '%.2f%%' % (list(enumerate(sims))[3][1] * 100)+"\n")
a1.write("orig.txt与orig_0.8_dis_15.txt相似度为：" + '%.2f%%' % (list(enumerate(sims))[4][1] * 100)+"\n")
