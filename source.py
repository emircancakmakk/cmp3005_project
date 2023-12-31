import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate a Karate Club graph using NetworkX
G = nx.karate_club_graph()

# Obtain the Laplacian matrix of the graph
laplacian_matrix = nx.laplacian_matrix(G).toarray()

# Calculate the eigenvalues and eigenvectors of the Laplacian matrix
eigenvalues, eigenvectors = np.linalg.eigh(laplacian_matrix)

# Choose the smallest k eigenvalues and corresponding eigenvectors
k = 4
selected_eigenvalues = eigenvalues[:k]
selected_eigenvectors = eigenvectors[:, :k]

# Perform KMeans clustering on the selected eigenvectors
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(selected_eigenvectors)

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
