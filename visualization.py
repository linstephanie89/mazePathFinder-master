import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import display
import time


class animated_path():

    def __init__(self, maze, closed_list, path, start_s, goal_s):

        self.start_s = start_s
        self.goal_s = goal_s

        # Layer 1: Maze (Input as a np array)
        self.maze = maze

        # Layer 2: Closed List (Input as a list of states)
        self.closed_list = closed_list
        if self.closed_list:
            self.c_max_g = max([state.g for state in self.closed_list])

        self.clv = np.zeros(maze.shape, dtype=float)
        self.clv = np.ma.masked_where(self.clv == 0, self.clv)

        # Layer 3: Path (Input as a list of states), start_s and goal_s
        if path:
            self.path = path
        else:
            self.path = []
        self.pv = np.full(maze.shape, fill_value=-1, dtype=float)
        self.pv = np.ma.masked_where(self.pv == -1, self.pv)
        self.pv[start_s.position[0]][start_s.position[1]] = 0
        self.pv[goal_s.position[0]][goal_s.position[1]] = 1

        # Animation Init

    def animate(self, i):

        if i < len(self.closed_list):

            if self.c_max_g != 0:

                self.clv[self.closed_list[i].position[0]][self.closed_list[i].position[1]] \
                    = self.closed_list[i].g / self.c_max_g

            else:

                self.clv[self.closed_list[i].position[0]
                         ][self.closed_list[i].position[1]] = 1

        elif i - len(self.closed_list) < len(self.path):

            i -= len(self.closed_list)

            self.pv[self.path[i].position[0]
                    ][self.path[i].position[1]] = i / len(self.path)

        else:
            print('.', end='')
            return

        # Show
        self.ax.clear()
        self.ax.axis('off')
        plt.imshow(self.maze, alpha=1, cmap='Greys')
        plt.imshow(self.clv, alpha=.5, cmap='Wistia')
        plt.imshow(self.pv, alpha=1, cmap='cool')

    def start_single_animation(self):
        self.fig, self.axs = plt.subplots()
        plt.tick_params(left=False, right=False, labelleft=False,
                        labelbottom=False, bottom=False)
        self.interval = 1 / self.maze.shape[0]
        self.anim = animation.FuncAnimation(self.fig, self.animate, frames=len(
            self.closed_list) + len(self.path), interval=self.interval)
        plt.show()


class repeated_animated_path():

    def __init__(self, animated_path_dict):

        self.animated_path_dict = animated_path_dict
        self.animated_path_list = list(animated_path_dict.values())
        self.algorithm_names = list(animated_path_dict.keys())
        self.x = 0
        self.fig, self.ax = plt.subplots()
        plt.tick_params(left=False, right=False, labelleft=False,
                        labelbottom=False, bottom=False)

    def repeated_animate(self, i):

        # Termination Sequence
        if i == self.final_threshold:
            print('.', end='')
            return

        # Have we reached the end of this a*?
        if i == sum([(len(y.path) + len(y.closed_list))
                    for y in self.animated_path_list[:1 + self.x]]):

            self.x += 1

        # Subtracting previous a* lengths from i
        i -= sum([(len(y.path) + len(y.closed_list))
                  for y in self.animated_path_list[:self.x]])

        anim = self.animated_path_list[self.x]

        if i < len(anim.closed_list):

            if anim.c_max_g != 0:

                anim.clv[anim.closed_list[i].position[0]][anim.closed_list[i].position[1]] = \
                    anim.closed_list[i].g / anim.c_max_g

            else:

                anim.clv[anim.closed_list[i].position[0]
                         ][anim.closed_list[i].position[1]] = 1

        elif i - len(anim.closed_list) < len(anim.path):

            i -= len(anim.closed_list)

            anim.pv[anim.path[i].position[0]
                    ][anim.path[i].position[1]] = i / len(anim.path)

        # Show
        self.ax.clear()
        self.ax.axis('off')
        plt.imshow(anim.maze, alpha=1, cmap='Greys')
        plt.imshow(anim.clv, alpha=.5, cmap='Wistia')
        plt.imshow(anim.pv, alpha=1, cmap='cool')
        plt.title(self.algorithm_names[self.x])

    def start_repeated_animate(self):
        self.final_threshold = sum(
            [(len(y.path) + len(y.closed_list)) for y in self.animated_path_list])
        self.anim = animation.FuncAnimation(
            self.fig, self.repeated_animate, interval=50)
        plt.show()
        self.x = 0
