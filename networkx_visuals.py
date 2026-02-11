# To run use python3 .\networkx_visuals.py
# This is a much better lib then before, I would recommend you all look at it
# TODO 
#  Read from Graph_Intialization and make it work with matlibplot to quickyly flip through this
#  We have to color the nodes, would be cool if can be done in real time, there is a animation for this lib
# https://networkx.org/documentation/stable/auto_examples/3d_drawing/plot_3d_animation_basic.html


# add node labels?
# add some test cases (dont know what they use for python tho)


import networkx as nx
import matplotlib.pyplot as plt

#This is the adj of graph G5****
G5 = {
        0: [1,4],
        1: [0,2,4],
        2: [1,5,6],
        3: [4,7],
        4: [0,1,3,5],
        5: [2,4,6,7],
        6: [2,5,7],
        7: [3,5,6],
    }
K5= {
    0: [1,2,3,4],
    1: [0,2,3,4],
    2: [0,1,3,4],
    3: [0,1,2,4],
    4: [0,1,3,2],
}


def draw_graph(adj):

    G = nx.from_dict_of_lists(adj) #We have the adj of the graph, this returns a graph from the list described in Graph_initialization
    try:
        if nx.is_planar:
            print("gdwdwadawdadws")
            nx.draw_planar(G)
    except:
            print("graph cannot be drawn planar, drawing non-planar version")
            nx.draw(G)

    plt.show()

#                   COLOURS FOR LATER
#G.add_nodes_from([(4, {"color": "red"}), (5, {"color": "green"})])
#pull the color from the nodes to draw them
#node_colors = [G.nodes[color]["color"] for color in G.nodes()]

#draw_graph(G5)
draw_graph(K5)


#https://networkx.org/documentation/stable/tutorial.html
#https://networkx.org/documentation/stable/reference/drawing.html
#https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.planar_drawing.combinatorial_embedding_to_pos.html#networkx.algorithms.planar_drawing.combinatorial_embedding_to_pos



#To cite NetworkX please use the following publication:
#Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008