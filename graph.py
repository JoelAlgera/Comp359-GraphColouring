#https://mrgallo.github.io/fundamentals/pygame/pygame-template.html


# pygame template
from collections import deque,defaultdict
import pygame


pygame.init()

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 12)



#These are the node colours
Colour_White = (255,255,255) #colour 1
Colour_Black = (0,0,0) #colour 2
Colour_Red = (255,160,120) #colour 3
Colour_Yellow = (255,255,0) #colour 4

Node_size = 18



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
#G4 = {
#    0: [1,2],
#    1: [0,2],
#    2: [0,1,3,4,6],
#    3: [2],
#    4: [2,5,7],
#    5: [4],
#    6: [2,7],
#    7: [4,6],
#    }



def calculate_pos(graph, root, width, spacer): #this lays out the nodes in the pattern of a BFS tree, it need some work because of it has crossing of the edges

    visited= set([root])
    levels= defaultdict(list)

    queue= deque([(root,0)])
    while queue:
        node, depth = queue.popleft()
        levels[depth].append(node)

        for x in graph[node]:
            if x not in visited:
                visited.add(x)
                queue.append((x,depth +1)) #append as a pair

    pos = {}

    for depth, nodes in levels.items():
        #I need to return 2 pos where the nodes are and track that to draw the lines to connect them so I also need a way to track it

        #the y depends on the depth
        y= 100 + depth * spacer
        align = width // (len(nodes)+1)

        #now for x depends on align and number of nodes

        for i, node in enumerate(nodes):
            x= spacer + align * (i+1)
            pos[node] = (x,y)
    
    return pos

pos= calculate_pos(G5, root=0, width=WIDTH, spacer=100)


running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #Exit

    screen.fill(Colour_White)  # THIS DRAWS THE BACKGROUND(NEEDED)
    

    #logic for drawing the edges
    drawn=set()
    for pos_x, node_neighbors in G5.items():
        for pos_y in node_neighbors:
            if pos_x < pos_y:
                pygame.draw.line (
                    screen,
                    "black",
                    pos[pos_x],
                    pos[pos_y],
                    5 
                )
            drawn.add((pos_x,pos_y))
            



    #logic for drawing the nodes
    for node, (x,y) in pos.items():
        pygame.draw.circle(
            screen, "red", (x,y), Node_size
        )
        name= font.render(str(node),1,"black")
        screen.blit(name, name.get_rect(center=(x,y)))


    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()