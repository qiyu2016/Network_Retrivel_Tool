#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/5/22 9:32

利用 CSV文件中的 边的表达，构建network, 并保存；（保存后，之后可以直接调用图文件）
然后，基于设计师输入的关键词node 和 路径长度path_length，利用Random Walk连接出更多的概念和功能词汇
"""

import networkx as nx
import pandas as pd
#import numpy as np
import random
#from tqdm import tqdm
#from sklearn.decomposition import PCA
#import matplotlib.pyplot as plt
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

nx.write_gexf(G, './FunctionConceptGraph.gexf')

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