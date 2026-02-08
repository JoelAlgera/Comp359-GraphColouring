import random

class State:
    
    def __init__(self, map, parent):
        self.map = map
        self.parent = parent
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)
    
    def step(self):
        for i in range(len(self.map)):
            gunPoint = self.map[i]
            if gunPoint.colour == 0:
                print("IM USELESS")
                neighborcolours = []
                for j in range(len(gunPoint.neighbors)):
                    neighborcolours.append(gunPoint.neighbors[j].colour)
                colour = random.randint(1, 3)
                if colour not in neighborcolours:
                    childmap = self.map
                    childmap[i].colour = colour
                    child = State(map = childmap, parent = self)
                    self.addChild(child)
                return child
    def tellMeAboutYour(self):
        print("My parent is", self.parent, "My children are", self.children)
        information = []
        for i in range(len(self.map)):
            gubba = (self.map[i].name, self.map[i].colour)
            information.append(gubba)
        print(information)

class Node:

    
    def __init__(self, name, colour):
        self.name = name
        self.neighbors = []
        self.colour = colour
    
    def iAm(self):
        print("My Name is", self.name, "My friends are", self.neighbors, "I am", self.colour, "years old")
    
    def addFriend(self, node):
        self.neighbors.append(node)

node1 = Node("John Arbuckle", 0)
node2 = Node("Garfield Hamburter", 0)
node3 = Node("Odie bodie", 0)
node1.addFriend(node2)
node2.addFriend(node1)
node2.addFriend(node3)
node3.addFriend(node2)

state1 = State(map = [node1,node2,node3], parent = "NULL")
state2 = state1.step()
state1.tellMeAboutYour()
state2.tellMeAboutYour()