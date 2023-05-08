import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Define the directed graph
G = nx.DiGraph()
G.add_edges_from([('', 'Good'), ('', 'Hello'), ('', 'How are you'), ('', 'Im'), ('', 'Okay'), ('Hello', 'Im'),
                  ('Im', 'Good'), ('Im', 'Okay'), ('Hello', 'How are you'), ('Im', 'Okay'), ('Okay', 'Im'),

                  ('Good', 'Morning'), ('Good', 'Afternoon'), ('Good', 'Night'), ('Good', 'Day'),

                  ('', 'Thank you'), ('Thank you', 'P'), ('', 'Sorry'), ('Sorry', 'P'), ('Im', 'Sorry'), ('', 'Please'),
                  ('Please', 'P'), ('Im', 'P'), ('P', 'R'), ('R', 'E'), ('E', 'K'), ('K', 'S'), ('S', 'H'), ('H', 'A'),

                  ('Nice to meet', 'you'), ('you', 'Bye'), ('you', 'V'), ('', 'Excuse me'), ('Excuse me', 'V'),
                  ('', 'Bye'), ('Good', 'Bye'), ('Bye', 'V'), ('V', 'I'), ('I', 'S'), ('S', 'H'), ('H', 'N'), ('N', 'U'),

                  ('Mon', 'Day'), ('Tue', 'Day'), ('Wednes', 'Day'), ('Thurs', 'Day'), ('Fri', 'Day'), ('Sat', 'Day'),
                  ('Sun', 'Day')
                  ])
# Take input path from the user
with open('input.txt', 'r') as f:
    path = f.readline().strip().split()

# Check if the path exists in the graph
if all((path[i], path[i + 1]) in G.edges for i in range(len(path) - 1)):
    # Create a list of colors for the edges based on whether it is part of the path or not
    edge_colors = ['red' if (u, v) in zip(path, path[1:]) else G[u][v].get('color', 'black') for u, v in G.edges]

    # Draw the graph with colored edges
    pos = nx.spring_layout(G)

    figure(figsize=(100, 60))

# ---> nx.draw_networkx_nodes(G, pos, node_color='orange', node_size=100)
# nx.draw_networkx_labels(G, pos)

    nx.draw(G, pos, with_labels=True, edge_color=edge_colors)
    plt.show()

else:
    print("Invalid path!")
