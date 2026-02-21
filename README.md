# Comp359-GraphColouring

A Group project with Joel Algera, Brayden Schneider, Alexander Calderon, and Jacob Thompson for our course in COMP 359 ON1 on Design and Analysis of Algorithms

Our initial task was creating a Naive (non-minimal colour) graph colouring algorithm for planar graphs, where no neighbouring nodes can share the same colour.

In this project, we hope to learn more about the proposed graph search methods, explore the variations in algorithm complexity following each strategy's application, and experiment with the validity of the 4-colour theorem along with potential optimizations to our colouring algorithm if possible.

To begin we created 6 hand drawn graphs of increasing complexity shown below and initialized them in the Graph_Initialization.py file as adjacency lists.
<img width="996" height="514" alt="COMP359AS2_GraphsV1" src="https://github.com/user-attachments/assets/de524377-1eba-4311-88d9-753c9584ce58" />

With these graphs we were able to create our initial colouring algorithm and test it throuhgout these graphs for accuracy as they were simple enough to see if the algorithm worked.

Once this task was completed our goal was to push further, expand our scope, and do more than the baseline level our prompt required us to do.

Our plans to further our project and exploration:<br>
-Optimize the algorithm to use as few colours as possible (max should always be 4 for a planar graph as per the four colour theorem). We want to apply techniques such as arc consistency, cut-sets, and variable elimination inorder to minimize the colours needed.<br>
-Output our coloured planar graphs as 2d maps to better display the work done by the colouring algorithm.<br>
-If we can output the graphs as 2d maps we would like to explore ways of taking in an uncoloured 2d map, converting it to a planar graph, colouring it, and outputting the coloured version of that graph where there are no adjacent colours.<br>
-Finally if all other goals are completed create a user-friendly GUI to present the algorithm at runtime.<br>

## References

- Used chatgpt to create the sample graphs to test the algorithms efficacy - <https://chatgpt.com/share/698bc9df-1180-8004-a495-fbc1b0f8ccdc>
- Networkx(nx) paper : Hagberg, A. A., Schult, D. A., & Swart, P. J. (2008). Exploring network structure, dynamics, and function using NetworkX
- The algorithm used by networkx, to draw the graphs: M. Chrobak and T.H. Payne: A Linear-time Algorithm for Drawing a Planar Graph on a Grid 1989 http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.51.6677
- SkiImage(ski) paper/ rag algorithm: van der Walt S. et al. (2014). scikit-image: Image processing in Python. PeerJ, 2:e453. <https://doi.org/10.1016/0020-0190(95)00020-D>



## Python Libraries

This project used the following python libraries:

- skimage - <https://scikit-image.org/docs/stable/api/api.html>
- networkx - <https://networkx.org/en/>
- Numbpy - <https://numpy.org/>
- MatlibPlot- <https://matplotlib.org/>

## Resources (functions from the libaries)
- Region Adjacency Graphs with ski : https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_rag.html
- Doing colored nodes with nx: https://networkx.org/documentation/latest/reference/algorithms/coloring.html#module-networkx.algorithms.coloring
- Doing colored nodes with nx: https://networkx.org/documentation/latest/auto_examples/drawing/plot_house_with_colors.html
- Converting a nxgraph: https://networkx.org/documentation/latest/reference/convert.html
## Debug Videos

- Joel: <https://youtu.be/N339ilLS49M>
- Brayden <https://youtu.be/otu7jLRBgzM>
