from generate_maze import generate_maze
import numpy as np

# state object for holding position, parent, g, h, and f values of a state
# includes an equals, hash, and less than comparison function


class state():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = float('inf')
        self.h = float('inf')
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.f < other.f


# Grid Dimensions
n = 101
mazes = [generate_maze(n) for i in range(50)]
# Store the mazes in a numpy array
mazes = np.array(mazes)
# priority queue which contains only the start state initially, keeps track of all nodes to be visited --> binary heap using python libraries
# holds tuple (f-value, s)
OPEN_LIST = []
# set that keeps track of all nodes that have already been visited --> put state s into list when expanding that node
CLOSED_LIST = set()
# array of potential actions taken by state s on grid
clv_list = []
actions = ["up", "down", "left", "right"]
