# 根据数据集中的数据，建立一个网络
import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
import string
import pdb


def buildgraph():
    f = open("../Wiki-Vote.txt")
    line = f.readline()
    rg = nx.Graph()
    list = []
    l = []

    # 存储所有节点的列表
    all_nodes = []
    while line:
        if line[0] != '#':
            str = line.split('\t')  # 将字符串按照制表符（\t）进行分割，并将结果存储在一个数组中
            a = str[0]  # 如果数据集是分行的，那么此处是a=str[0]，下面的也要改。做实验之前，拿一小部分数据看看本段程序运行的效果
            b = str[1]
            rg.add_edge(a, b, w=0)  # 添加边

            all_nodes.append(a)
            all_nodes.append(b)
        line = f.readline()  # 用来读取文件的一行文本数据，并将其存储在变量 line 中的操作。
    f.close()

    # 随机选择1000个节点
    selected_nodes = random.sample(all_nodes, 100)
    # 创建一个新的图，仅包含选定的节点和它们之间的边
    subgraph = rg.subgraph(selected_nodes)
    # 遍历子图的节点集合并打印节点列表
    #     for node in subgraph.nodes():
    #         print(node)
    return subgraph


def greedy():
    s = set()  # 存放收益值最大的种子
    parameters = set()
    rg = buildgraph()
    node = rg.nodes()  # 存放种子列表
    dict = {}  # 存放每个节点的增益
    lastvalue = 0  # 上一次增益的值
    n = 5  # 存放要寻找的种子个数
    k = 0  # 迭代计数器

    node = list(rg.nodes())  # 将节点视图转换为列表
    while True:
        for i in node:
            seed = set()
            seed.update(s)
            seed.add(i)
            parameters = seed
            rg1 = rg.copy()
            m = IC(parameters, rg1)  # 用m保存种子集激活的节点数
            m = m - lastvalue  # 计算增益 ，增益是将节点添加到当前种子集合后，新激活的节点数量减去上一次迭代的增益。
            dict[i] = m

        dsort = sorted(dict.items(), key=lambda d: d[1], reverse=True)  # 按照增益降序排列节点，得到的是一个二维数组。
        print(dsort)
        u = dsort[0][0]
        lastvalue = dsort[0][1]
        node.remove(u)  # 将其从节点列表中移除
        dict = {}
        s.add(u)  # 添加到种子节点集合
        k += 1
        if k >= n:
            break
    print(s)
    return s  # 返回种子集合


def IC(seed, rg1):  # 该函数用于模拟信息传播过程并计算激活的节点数量。
    PP = 100  # PP 表示每条边上触发信息传播的概率阈值，设置为100表示每条边都触发
    R = 10  # R 表示模拟信息传播的次数。
    number = 0  # 激活节点的数量
    active = set()  # 存储当前激活的节点

    # 个循环用于多次模拟信息传播过程，以获取平均传播范围。
    for i in range(0, R):  # 循环若干次，以求得平均传播范围  seed=set('1'),修改时，把下面的语句（到b=number/R）缩进
        active = seed  # 在每次模拟中，首先将初始的种子节点设置为激活节点，并计算激活节点的数量。
        numactive = len(active)

        newactive = []  # newactive 列表来存储本次循环中新激活的节点。

        for i in active:
            newactive.append(i)  # 以列表存放本次循环激活的节点。不用集合是因为把一个集合付给另一个集合时，两个集合指向同一内存

        while True:
            oldactive = set()  # 存放上一时间步t激活的节点
            oldactive.update(newactive)
            newactive = []
            dict = {}
            for v in oldactive:
                nvnew = set()
                nv = set()  # 存放邻居节点
                nv = set(rg1.neighbors(v))
                nvnew.update(nv)
                for i in nv:
                    dict = rg1.get_edge_data(v, i)
                    if dict['w'] == 1:
                        nvnew.remove(i)  # 如果本条边已经被访问过，则nv集合中减去此边
                if len(nvnew) == 0:  # 如果v没有邻居节点，则代表它不会再传播信息，应该取oldactive中的下一个节点
                    continue
                a = nvnew & active  # 去掉邻居节点中已经激活的节点
                nvnew = nvnew - a
                for w in nvnew:
                    dict = rg1.get_edge_data(v, w)  # 用字典结构表示v已经对w有激活操作，后面就不能再考虑w对v的操作

                    rg1.remove_edge(v, w)
                    rg1.add_edge(v, w, w=1)
                    p = random.randint(1, 100)  # 产生随机数，满足激活条件，则激活，把w放入newactive和active中
                    if p <= PP:
                        newactive.append(w)
                        active.add(w)
                        continue

            if len(newactive) == 0:
                break

        n = len(active)
        number += n

    b = number / R  # 包含种子集合中节点的个数
    b -= numactive
    # print(active)
    return b


if __name__ == "__main__":
    greedy()