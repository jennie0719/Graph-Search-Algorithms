import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add nodes with their positions
positions = {
    "West Seattle": (7, 5), 
    "Sodo": (16.5, 5), 
    "Beacon Hill": (19.5, 0.5), 
    "Columbia City": (24, 2),
    "Pioneer Square": (17, 9.5),
    "International District": (21.5, 10.5),
    "Downtown": (17.5, 13.5),
    "Belltown": (12.5, 17),
    "South Lake Union": (15.5, 17.5),
    "Capitol Hill": (21, 18),
    "Queen Anne": (11, 20.5),
    "Magnolia": (5.5, 24),
    "Fremont": (11.5, 27),
    "Wallingford": (16, 27),
    "University District": (22, 27),
    "Ballard": (7, 30),
    "Phinney Ridge": (12.5, 32),
    "Green Lake": (18, 32.5),
    "Ravenna": (23, 31.5),
}

# Add nodes to the graph
G.add_nodes_from(positions.keys())

# Add edges with lengths
edges = [('West Seattle', 'Sodo', 8), 
         ('Sodo', 'Beacon Hill', 4), 
         ('Sodo', 'Columbia City', 5),
         ('Beacon Hill', 'Columbia City', 4),
         ('Sodo', 'International District', 7), 
         ('Sodo', 'Pioneer Square', 3),
         ('Pioneer Square', 'International District', 4), 
         ('Pioneer Square', 'Downtown', 4), 
         ('Downtown', 'International District', 6), 
         ('Downtown', 'Belltown', 6), 
         ('Downtown', 'South Lake Union', 5), 
         ('Downtown', 'Capitol Hill', 7), 
         ('South Lake Union', 'Belltown', 2), 
         ('Queen Anne', 'Belltown', 3), 
         ('South Lake Union', 'Capitol Hill', 5), 
         ('South Lake Union', 'Queen Anne', 4), 
         ('University District', 'Capitol Hill', 8), 
         ('Wallingford', 'Capitol Hill', 9), 
         ('Queen Anne', 'Wallingford', 9), 
         ('Queen Anne', 'Fremont', 7), 
         ('Queen Anne', 'Ballard', 9), 
         ('Queen Anne', 'Magnolia', 5), 
         ('Ballard', 'Magnolia', 7), 
         ('Ballard', 'Phinney Ridge', 6), 
         ('Ballard', 'Fremont', 4), 
         ('Phinney Ridge', 'Fremont', 3), 
         ('Phinney Ridge', 'Green Lake', 3), 
         ('Wallingford', 'Fremont', 3), 
         ('Wallingford', 'Green Lake', 3), 
         ('University District', 'Green Lake', 5), 
         ('Ravenna', 'Green Lake', 4), 
         ('Wallingford', 'University District', 4), 
         ('Ravenna', 'University District', 5), 
         ]
G.add_weighted_edges_from(edges)

# # Draw the graph with specified positions
# nx.draw(G, pos=positions, with_labels=True, node_size=1000, node_color='lightblue', font_size=6)

# # Add edge labels
# edge_labels = {(u, v): f'{d["weight"]}' for u, v, d in G.edges(data=True)}
# nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels)

# plt.xlim(0, 30)
# plt.ylim(0, 35)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Seattle')
# plt.grid(True)
# plt.show()