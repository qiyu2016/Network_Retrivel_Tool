#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/6/8 11:27

1\随机选择几个图中的节点
2\测试每一个节点与其他节点的最短路径为1,2,3……的节点个数
"""

import networkx as nx
import random
import csv

G = nx.read_gexf('./FunctionConceptGraph.gexf')
#node = 'drone'
#print(nx.shortest_path_length(G, node, node))   # 节点与自身之间的最短路径为 0
all_nodes = list(G.nodes())   # 所有节点的列表

def count_num(node, steps):
    count = 0
    for i in all_nodes:
        if nx.has_path(G, node, i) is True:
#            print(i)
            if nx.shortest_path_length(G, node, i) == steps:
                count = count + 1
        else:
            continue
    return count


nodelist = random.sample(all_nodes, 10)
nodenumList = []
for item in nodelist:
    node = item
    nodenum = [node]
    for j in range(1, 10):
        number = count_num(node, j)
        nodenum.append(number)
    print(nodenum)
    nodenumList.append(nodenum)


'''    
node = 'deliver'
nodenum = [node]
for j in range(1,7):
    number = count_num(node, j)
    nodenum.append(number)
print(nodenum)
'''

# 写入CSV文件
pathsort = "D:/5_PatentData/Data/CalculateResult/nodespathlenthsum02.csv"
CSVFunc = open(pathsort, 'w', newline='')
writer = csv.writer(CSVFunc)
writer.writerow(['Node', '1step', '2step', '3step', '4step', '5step', '6step', '7step', '8step', '9step'])
for iFS in nodenumList:
    writer.writerow(iFS)
CSVFunc.close()




