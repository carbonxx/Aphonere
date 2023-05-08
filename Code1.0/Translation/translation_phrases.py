import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, text

G = nx.DiGraph()
G.add_edges_from([('', 'Hey'), ('', 'Bye'), ('', 'Ok'), ('', 'Thank you'),
                  ('', 'Good morning'), ('', 'Good night'), ('', 'Im'), ('Hey', 'Im'), ('Im', 'Sorry'),
                  ('Im', 'P'), ('P', 'R'), ('R', 'E'), ('E', 'K'), ('K', 'S'), ('S', 'H'), ('H','A'),
                  ('Im', 'V'), ('V', 'I'), ('I','S'), ('S', 'H'), ('H', 'N'), ('N', 'U') ])

pos = nx.spring_layout(G)

figure(figsize=(100,60))

nx.draw_networkx_nodes(G, pos, node_color='orange', node_size=100)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)

plt.show()