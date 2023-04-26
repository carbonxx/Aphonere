import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, text

G = nx.DiGraph()
G.add_edges_from([('', 'A'), ('', 'B'), ('', 'C'), ('', 'D'), ('', 'E'), ('', 'F'), ('', 'G'), ('', 'H'), ('', 'I'),
                  ('', 'J'), ('', 'K'), ('', 'L'), ('', 'M'),('', 'N'), ('', 'O'), ('', 'P'), ('', 'Q'), ('', 'R'),
                  ('', 'S'), ('', 'T'), ('', 'U'), ('', 'V'), ('', 'W'), ('', 'X'), ('', 'Y'), ('', 'Z'),

                  ('A', 'A'), ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'),
                  ('H', 'I'),('I', 'J'), ('J', 'K'), ('K', 'L'), ('L', 'M'),('M', 'N'), ('N', 'O'), ('O', 'P'),
                  ('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'T'), ('T', 'U'), ('U', 'V'),('V', 'W'), ('W', 'X'),
                  ('X', 'Y'), ('Y', 'Z'),

                  ('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'),
                  ('A', 'I'),('A', 'J'), ('A', 'K'), ('A', 'L'), ('A', 'M'),('A', 'N'), ('A', 'O'), ('A', 'P'),
                  ('A', 'Q'), ('A', 'R'), ('A', 'S'), ('A', 'T'), ('A', 'U'), ('A', 'V'),('A', 'W'), ('A', 'X'),
                  ('A', 'Y'), ('A', 'Z')
                  ])

pos = nx.spring_layout(G, scale=10)

figure(figsize=(500,100))

nx.draw_networkx_nodes(G, pos, node_color='orange', node_size=100)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)

plt.show()

