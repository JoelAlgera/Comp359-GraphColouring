
from skimage import color, io, measure
import matplotlib.pyplot as plt
import networkx as nx



def draw_graph(adj: dict | nx.Graph) -> None:
    """Draw a graph. adj must be an adjacency list (dict of lists) or an nx.Graph.""" #this is just so I can hover for hint in VSCode
    if isinstance(adj, nx.Graph):
        G = adj
    elif isinstance(adj, dict):
        G = nx.from_dict_of_lists(adj)
    else:
        raise TypeError("adj must be an adjacency list (dict) or an nx.Graph")
        
    draw_kw = dict(with_labels=True, node_size=750, font_size=10) #this is for the labels

    plt.figure(figsize=(6, 6))
    try:
        nx.draw_planar(G, **draw_kw) #this throws an error if the graph is not planar

    except Exception: #we can expect an error if the graph is not planar(quite common actually)
        print("Tried to draw planar, but failed. Drawing with spring_layout.")
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, **draw_kw)
    plt.show()

class img_planar:
    def img_load(image_path="NW_AMER.jpg"):

        img = io.imread(image_path)
        gray = color.rgb2gray(img)
        #print(np.unique(gray)) # values of the pixels in image range from 0-1 


# setting parameter for the border and region.
        border = gray < 0.3 
        regions = gray > 0.3


#connectivity 2 is used as connectivity 1 only tracks up down left right. diagonals must be considered.
        labels = measure.label(regions, connectivity=2) 
        num_regions = labels.max()
#region detection
        print("Number of regions labeled in the image: ", num_regions - 1)

        #io.imshow(labels)
        #plt.axis('off')
        #plt.show()

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
                    neighbors.discard(0) # removing 0 label from the set, 0 is connected to every region.\
                    for a in neighbors:
                        for b in neighbors:
                            if a!= b:
                                adjacency.add(tuple(sorted((int(a), int(b)))))
        print("set of edges: ", adjacency)

        return adjacency

# graph creation with networkx
    def graph_result(adjacency):
        graph = nx.Graph()
        graph.add_edges_from(adjacency)
        draw_graph(graph)


if __name__ == "__main__":
    labels, border = img_planar.img_load("thinnerTest.jpg")
    adjacency = img_planar.adjacency_list(labels, border)
    img_planar.graph_result(adjacency)
  
