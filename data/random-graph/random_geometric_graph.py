# source: https://github.com/networkx/networkx/blob/master/examples/drawing/random_geometric_graph.py
import networkx as nx
import matplotlib.pyplot as plt

G=nx.random_geometric_graph(400,0.125)
# position is stored as node attribute data for random_geometric_graph
pos=nx.get_node_attributes(G,'pos')

# find node near center (0.5,0.5)
dmin=1
ncenter=0
for n in pos:
    x,y=pos[n]
    d=(x-0.5)**2+(y-0.5)**2
    if d<dmin:
        ncenter=n
        dmin=d

# color by path length from node near center
p=nx.single_source_shortest_path_length(G,ncenter)

plt.figure(figsize=(2,2), dpi=150)
nx.draw_networkx_edges(G,pos,nodelist=[ncenter],alpha=0.4)
nx.draw_networkx_nodes(G,pos,nodelist=p.keys(),
                       node_size=20,
                       node_color=p.values(),
                       cmap=plt.cm.Blues_r)

plt.xlim(-0.05,1.05)
plt.ylim(-0.05,1.05)
plt.axis('off')
plt.savefig('random-geometric-graph.png', dpi=150)
plt.show()

