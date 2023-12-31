# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering

# Generate a Karate Club graph using NetworkX
G = nx.karate_club_graph()

# Obtain the adjacency matrix of the graph
adjacency_matrix = nx.adjacency_matrix(G)

# Set the number of clusters for spectral clustering
n_clusters = 4

# Create a SpectralClustering object with specified parameters
spectral = SpectralClustering(n_clusters=n_clusters, affinity='precomputed', random_state=42)

# Fit the spectral clustering model and obtain cluster labels
labels = spectral.fit_predict(adjacency_matrix)

# Define the layout for node positioning
pos = nx.spring_layout(G)

# Set node size, edge color, and colormap for visualization
node_size = 200
edge_color = 'gray'
cmap = plt.cm.tab10

# Draw the graph using NetworkX and Matplotlib
nx.draw(G, pos, node_color=labels, cmap=cmap, with_labels=True, node_size=node_size, edge_color=edge_color)

# Add title to the plot
plt.title('Spectral Clustering Results')

# Display the plot
plt.show()
