import community
import networkx as nx
#import matplotlib.pyplot as plt
import time


# Replace this with your networkx graph loading depending on your format !
#G = nx.erdos_renyi_graph(30, 0.05)
'''G= nx.Graph()
G.add_path([0,1,2])
print(G.nodes())'''
G = nx.read_edgelist('prueba.csv', delimiter=';', nodetype=str, encoding="utf-8")
print("llego")
#print(G.nodes())

#time.sleep(200)
#first compute the best partition
print("-----------------------------------------------")
partition = community.best_partition(G)
print("-----------------------------------------------")

i=0
for j in partition.values():
  if(j>=i):
    i=j
    
print(i)
print("-----------------------------------------------")
time.sleep(20)
#print(partition)
time.sleep(200)

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]

print (partition)