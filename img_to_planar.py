
from skimage import color, io, measure
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

class img_planar:
    def img_load():

        img = io.imread("NW_AMER.jpg")
        gray = color.rgb2gray(img)
        print(np.unique(gray)) # values of the pixels in image range from 0-1 



#Visualization
        plt.imshow(gray, cmap="gray")
        plt.colorbar()
        plt.axis('off')
        plt.show()



# setting parameter for the border and region.
        border = gray < 0.3 
        regions = gray > 0.3

        plt.imshow(regions, cmap="gray")
        plt.axis('off')
        plt.show()



#connectivity 2 is used as connectivity 1 only tracks up down left right. diagonals must be considered.
        labels = measure.label(regions, connectivity=2) 
        num_regions = labels.max()
#region detection
        print("Number of regions labeled in the image: ", num_regions)

        io.imshow(labels)
        plt.axis('off')
        plt.show()

        return labels, border

    def adjacency_list(labels, border):
        adjacency = set()

        h, w = labels.shape #dimensions of the labeled map

        #scanning the whole labeled map
        for y in range (1, h - 1):
            for x in range(1, w - 1):
                if border[y, x]:
                    neighbors = set([
                        labels[y-1, x], # region below
                        labels[y+1, x], # region above
                        labels[y, x-1], # region left
                        labels[y, x+1] # region right
                    ])
                    neighbors.discard(0) # removing 0 label from the set, 0 is connected to every region.
                    for a in neighbors:
                        for b in neighbors:
                            if a!= b:
                                adjacency.add(tuple(sorted((int(a), int(b)))))

        return adjacency

# graph creation with networkx
    def graph_result(adjacency):
        graph = nx.Graph()
        graph.add_edges_from(adjacency)
        if 1 in graph:
            graph.remove_node(1) 

        plt.figure(figsize=(6,6))
        nx.draw(graph, with_labels=True, node_size=750, font_size=10)
        plt.show()

#calls
    labels, border = img_load()
    adjacency = adjacency_list(labels, border)
    graph_result(adjacency)
