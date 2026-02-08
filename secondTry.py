import random

class State:
    cycle = 0
    def __init__(self, nodes, arcs):
        self.nodes = nodes
        self.arcs = arcs

    def step(self):
        try:
            node = self.nodes.index(0)
        except ValueError:
            print("All nodes are coloured. Solution found!")
            self.print_state()
            return True
        
        for colour in range(1, 5):
            if self.is_valid_colour(node, colour):
                self.nodes[node] = colour
                State.cycle += 1
                print("Cycle", State.cycle, ": Assigned colour", colour, "to node", node)
                if self.step():

                    return True
                
                self.nodes[node] = 0
        return False
    

        """ for i in range(len(self.nodes)):
            if self.nodes[i] == 0:
                for x in range(3):
                    colour = x+1
                    if self.is_valid_colour(i, colour) and i not in self.checked:
                        heirloom = self.nodes.copy()
                        heirloom[i] = colour
                        child = State(parent=self, children=[], nodes=heirloom, arcs=self.arcs)
                        self.children.append(child)
                        child.print_state()
                        return child
                print("No valid colour found for node", i)
                self.parent.step()
                return None
                """

                    
    def is_valid_colour(self, node_index, colour):
        for a,b in self.arcs:
            if node_index == a and self.nodes[b] == colour:
                return False
            if node_index == b and self.nodes[a] == colour:
                return False
        return True

    def print_state(self):
        print("Nodes and their colours:")
        for i, c in enumerate(self.nodes):
            print(f"Node {i}: Colour {c}")

"""
def create_initial_state(num_nodes, arcs):
    nodes = [0] * num_nodes
    return State(None, [], nodes, arcs)


def recursive_steps(state):
    if state is None:
        return
    child_state = state.step()
    recursive_steps(child_state)
"""




def canada():
    arcs = [(0,1),(0,2),(0,3),(1,2),(2,3),(2,4),(2,5),(3,4),(4,6),(5,6),(6,7),(7,8),(8,9),(8,10),(9,12),(12,11),(11,10)]
    nodes = [0] * 13
    state = State(nodes, arcs)
    state.step()

def tough1():
    arcs = [(0,1),(0,2),(0,3),(0,5),(1,5),(2,3),(2,5),(3,5),(3,4),(3,6),(3,7),(3,8),(4, 6),(5,6),(5,7),(5,8), (6,8), (7,8),(4,9),(6,9),(8,9)]
    nodes = [0] * 10
    state = State(nodes, arcs)
    state.step()

tough1()
