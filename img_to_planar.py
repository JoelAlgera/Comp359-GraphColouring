from skimage import color, io, measure, graph, segmentation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# colours we only need 4 but there are some extras, colour white is for the background, so the first color is green
COLOR_PALETTE = ["white", "green", "red", "blue", "yellow", "purple", "pink", "orange", "lightblue"]


def draw_graph(adj: dict | nx.Graph, node_colors: dict | None = None) -> None:
    """Draw a graph. adj must be an adjacency list (dict of lists) or an nx.Graph.""" #this is just so I can hover for hint in VSCode
    if isinstance(adj, nx.Graph):
        G = adj
    elif isinstance(adj, dict):
        G = nx.from_dict_of_lists(adj)
    else:
        raise TypeError("adj must be an adjacency list (dict) or an nx.Graph")
        
    draw_kw = dict(with_labels=True, node_size=750, font_size=10) #this is for the labels
    if node_colors is not None:
        color_list = []
        for n in G.nodes():
            color_list.append(node_colors.get(n, 0))
        node_color = []
        for c in color_list:
            if c < len(COLOR_PALETTE):
                node_color.append(COLOR_PALETTE[c])
            else:
                node_color.append(COLOR_PALETTE[1])
        draw_kw["node_color"] = node_color

    plt.figure(figsize=(6, 6))
    try:
        nx.draw_planar(G, **draw_kw) #this throws an error if the graph is not planar

    except Exception: #we can expect an error if the graph is not planar(quite common actually)
        print("Tried to draw planar, but failed. Drawing with spring_layout.")
        pos = nx.spring_layout(G)
        nx.draw(G, pos=pos, **draw_kw)
    plt.show(block=False)

class img_planar:
    def img_load(image_path="NW_AMER.jpg"):

        img = io.imread(image_path)
        gray = color.rgb2gray(img)
        #print(np.unique(gray)) # values of the pixels in image range from 0-1 (border detection)


# setting parameter for the border and region.
        border = gray < 0.3 
        regions = gray > 0.3


#connectivity 2 is used as connectivity 1 only tracks up down left right. diagonals must be considered.
        labels = measure.label(regions, connectivity=2) 
        num_regions = labels.max()
#region detection
        print("Number of regions labeled in the image: ", num_regions - 1)

        plt.figure(figsize=(8, 8)) # new plot to show all at same time
        plt.imshow(labels > 0, cmap='gray') 
        
        # Add region numbers to help visualize the regions and debug
        for region in measure.regionprops(labels):
            y, x = region.centroid
            plt.text(x, y, str(region.label), color='red', 
                     fontsize=8, ha='center', va='center', fontweight='bold')
                    # try to center it not spending alot of time on it

        plt.axis('off')
        plt.title("Numbered Regions")
        plt.show(block=False)

        return labels, border

    def adjacency_list(labels, border):
        # skimage has some useful things to help with this process and
        # yes using an external lib is like cheating,
        #  but its much better than what we were doing before and easy

        expanded_labels = segmentation.expand_labels(labels, distance=10) 
        
       # Remember: border.astype(float) is the edge map (array of floats) we get from border = gray < 0.3
       # as the rag_boundary function requires (labels, edge_map) 
       # this is hacky and we should consider changing this later, but seems to test quite well
        rag = graph.rag_boundary(expanded_labels, border.astype(float))
        adjacency = set()
        for a, b in rag.edges():
            if a != 0 and b != 0:
                adjacency.add(tuple(sorted((int(a), int(b)))))
        print("set of edges: ", adjacency)

        return adjacency

# graph creation with networkx
    def graph_result(adjacency, node_colors=None):
        graph = nx.Graph()
        graph.add_edges_from(adjacency)
        draw_graph(graph, node_colors=node_colors)


if __name__ == "__main__":
    labels, border = img_planar.img_load("images/thinnerTest.jpg")
    adjacency = img_planar.adjacency_list(labels, border)
    img_planar.graph_result(adjacency)


  
