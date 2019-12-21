#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests 
import matplotlib.pyplot as plt
import networkx as nx

URL = "https://raw.githubusercontent.com/DealPete/forceDirected/master/countries.json"
myData = requests.get(url = URL)
data = myData.json()

nodes = data["nodes"]
links = data["links"]

G = nx.Graph()

for link in links:
    G.add_edge(nodes[link["source"]]["code"], nodes[link["target"]]["code"], weight=1)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=800, node_color='pink')
nx.draw_networkx_edges(G, pos, G.edges, width=3, alpha=0.5, edge_color='teal')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
plt.rcParams['figure.figsize'] = [55, 45]
plt.show()


# In[ ]:




