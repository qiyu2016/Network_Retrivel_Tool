#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/4/28 14:02
"""

import networkx as nx
import pandas as pd
import numpy as np
import random
from tqdm import tqdm
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import time
start = time.clock()

#filepath = './csvData.csv'
filepath = 'D:/5_PatentData/Data/Network_represent/edgerepresent.csv'
df = pd.read_csv(filepath, sep = ",")   # 读取csv文件
print(df.head())   # 查看数据对象的前n行，默认5
print(df.shape)   # 参看行数和列数

# construct an undirected graph
G = nx.from_pandas_edgelist(df, "source", "target", edge_attr=True, create_using=nx.Graph())
print(len(G))   # number of nodes


# function to generate random walk sequences of nodes
def get_randomwalk(node, path_length):
    random_walk = [node]

    for i in range(path_length - 1):
        temp = list(G.neighbors(node))
        temp = list(set(temp) - set(random_walk))
        if len(temp) == 0:
            break

        random_node = random.choice(temp)
        random_walk.append(random_node)
        node = random_node

    return random_walk

print(get_randomwalk('UAVs', 10))   # 查看随机游走10步，起点是UAVs

all_nodes = list(G.nodes())   # 所有节点的列表
#all_nodes2 = list(G.nodes())   # 所有节点的列表
#print(all_nodes)

#all_nodes = all_nodes2[0:30]   # 只设置30个节点

random_walks = []
for n in tqdm(all_nodes):
    for i in range(5):
        random_walks.append(get_randomwalk(n, 10))

# count of sequences
print(len(random_walks))



import warnings
#warnings.filterwarnings('ignore')
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
#import gensim
from gensim.models import Word2Vec



# train word2vec model
# 参数可见 (https://radimrehurek.com/gensim/models/word2vec.html)
model = Word2Vec(window = 4, min_count=1, sg = 1, hs = 0,
                 negative = 10, # for negative sampling
                 alpha=0.03, min_alpha=0.0007,
                 seed = 14)
#model = Word2Vec(random_walks, window=5, min_count=1)

model.build_vocab(random_walks, progress_per=2)
model.train(random_walks, total_examples=model.corpus_count, epochs=20, report_delay=1)

print(model)

# find top n similar nodes
#model.similar_by_word('UAVs')

model.save('./Network_DeepWalk.model')



# 获取程序运行时间
end = time.clock()
seconds = end-start
#seconds = 323278.464909
#seconds = 0.6
print('Running time: %s Seconds' %seconds)
# 将运行时间秒转换为时分秒
if seconds >=1:
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    print('Running time(hours:mins:seconds): %02d:%02d:%02d' %(h, m, s))
