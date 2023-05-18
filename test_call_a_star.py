import repForward
import repBack
import repForLarge
import repForSmall
import adaptiveA
from main import state, OPEN_LIST, CLOSED_LIST, clv_list
from test_main import maze, n
import visualization
import time


def call_a_star(a_star, GRID):
    start = time.time()
    start_s = state(None, (0, 0))
    goal_s = state(None, (n-1, n-1))
    if a_star == adaptiveA.a_star:
        start_s.h = abs(start_s.position[0] - goal_s.position[0]) + \
            abs(start_s.position[1] - goal_s.position[1])
    else:
        start_s.h = 0
    start_s.g = 0
    # initialize OPEN and CLOSED list
    OPEN_LIST.clear()
    CLOSED_LIST.clear()
    clv_list.clear()
    path, min_cost = a_star(start_s, goal_s, GRID)
    end = time.time()
    total_time = end - start
    if a_star == repBack.a_star:
        clv_list.reverse()
    copy_clv_list = clv_list.copy()
    return visualization.animated_path(GRID, copy_clv_list, path, start_s, goal_s)


animated_path_dict = \
    {"Repeated Forward": call_a_star(repForward.a_star, maze),
     "Repeated Backward": call_a_star(repBack.a_star, maze),
     "Repeated For Large": call_a_star(repForLarge.a_star, maze),
     "Repeated For Small": call_a_star(repForSmall.a_star, maze),
     "Adaptive": call_a_star(adaptiveA.a_star, maze)}\

x = visualization.repeated_animated_path(animated_path_dict)
x.start_repeated_animate()
