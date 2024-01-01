import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import time

# Function to measure time for spectral clustering
def measure_spectral_clustering_time(graph):
    start_time = time.time()

    # Obtain the Laplacian matrix of the graph
    laplacian_matrix = nx.laplacian_matrix(graph).toarray()

    # Calculate the eigenvalues and eigenvectors of the Laplacian matrix
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian_matrix)

    # Choose the smallest k eigenvalues and corresponding eigenvectors
    k = 4
    selected_eigenvalues = eigenvalues[:k]
    selected_eigenvectors = eigenvectors[:, :k]

    # Perform KMeans clustering on the selected eigenvectors
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(selected_eigenvectors)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Time taken for spectral clustering on a graph of size {len(graph.nodes)}: {elapsed_time} seconds")

    # Define the layout for node positioning
    pos = nx.spring_layout(G)

    # Set node size, edge color, and colormap for visualization
    node_size = 200
    edge_color = 'gray'
    cmap = plt.cm.tab10

    # Draw the graph using NetworkX and Matplotlib
    nx.draw(graph, pos, node_color=labels, cmap=cmap, with_labels=True, node_size=node_size, edge_color=edge_color)

    # Add title to the plot
    plt.title('Spectral Clustering Results')

    # Display the plot
    plt.show()

G = nx.karate_club_graph()
measure_spectral_clustering_time(G)
