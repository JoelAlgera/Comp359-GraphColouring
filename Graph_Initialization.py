#This file initializes the hand drawn graphs from the README file as adjacency lists.

GRAPHS = {

    #G_ is graph name corresponding the hand drawn graph
    "G1": {
        #Defines nodes
        0: [1],
        1: [0,2],   #[] lists define what nodes are adjacent to that node
        2: [1],
    },

    "G2": {
        0: [1],
        1: [0,2,3,4],
        2: [1],
        3: [1],
        4: [1],
    },

    "G3": {
        0: [1,3,4],
        1: [0,2,3],
        2: [1,3],
        3: [0,1,2,4],
        4: [0,3],
    },

    "G4": {
        0: [1,2],
        1: [0,2],
        2: [0,1,3,4,6],
        3: [2],
        4: [2,5,7],
        5: [4],
        6: [2,7],
        7: [4,6],
    },

    "G5": {
        0: [1,4],
        1: [0,2,4],
        2: [1,5,6],
        3: [4,7],
        4: [0,1,3,5],
        5: [2,4,6,7],
        6: [2,5,7],
        7: [3,5,6],
    },

    "G6": {
        0: [1,8],
        1: [0,2,3,5],
        2: [1,4,5],
        3: [1,5,6,7],
        4: [2,5],
        5: [1,2,3,4],
        6: [3,7],
        7: [3,6,8,9],
        8: [0,7,9],
        9: [7,8],
    },
}