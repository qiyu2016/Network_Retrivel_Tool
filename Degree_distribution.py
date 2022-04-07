#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: Qiyu
@date : 2020/6/8 18:38

网络图结构中节点度分布的散点图，幂律分布（power-law distribution）
"""

import matplotlib.pyplot as plt   # 导入科学绘图包
from matplotlib.pyplot import MultipleLocator
import networkx as nx

G = nx.read_gexf('D:/PythonProject/paper5_PatentData/FunctionConceptGraph.gexf')
#G=nx.random_graphs.barabasi_albert_graph(1000,10)#生成n=1000,m=10的无标度的图
#print("某个节点的度:", G.degree(0))   #返回某个节点的度
# print("所有节点的度:",G.degree())   #返回所有节点的度
# print("所有节点的度分布序列:",nx.degree_histogram(G))#返回图中所有节点的度分布序列（从1至最大度的出现频次）
degree=nx.degree_histogram(G)   # 返回图中所有节点的度分布序列
x=range(len(degree))  # 生成X轴序列，从1到最大度
y=[z/float(sum(degree))for z in degree]   # 将频次转化为频率，利用列表内涵

# 这两行代码要写在最开始，在所有其他设置之前；否则失效
plt.rcParams['xtick.direction'] = 'in'  # in; out; inout
plt.rcParams['ytick.direction'] = 'in'   # 设置坐标刻度朝内

#plt.scatter(x,y, marker='o', s=6, color=(1,0,0))#在双对坐标轴上绘制度分布曲线
plt.scatter(x,y, marker='o', c='', s=30, edgecolors='#2e95c9')   # 空心圆标记

# 坐标轴设置
x_major_locator=MultipleLocator(500)   # 把y轴的刻度间隔设置为500，并存在变量里
y_major_locator = MultipleLocator(0.1)   # 把y轴的刻度间隔设置为0.1，并存在变量里
ax = plt.gca()   # ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator)   # 把x轴的主刻度设置为500的倍数
ax.yaxis.set_major_locator(y_major_locator)   # 把y轴的主刻度设置为0.1的倍数
plt.xlim(-100, 3000)   # 设置坐标值范围;把x轴的刻度范围设置为-50到3000，因为50不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
plt.ylim(-0.02, 0.5)
plt.tick_params(labelsize = 12)   # 设置坐标轴刻度字体大小15
plt.show()   # 显示图表
