import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
g.add_node(2)
g.add_node(5)
g.add_node(3)

g.add_edge(5, 2) # 5 -> 2
g.add_edge(2, 7)


# g.add_node(7)

nx.draw(g, with_labels=True)

plt.show()