import repForward
import repBack
import repForLarge
import repForSmall
import adaptiveA
from main import state, OPEN_LIST, CLOSED_LIST, clv_list, mazes, n
import time

# variables for calculating averages
ITERATIONS = 50
runtimes = []


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
    if path:
        print([s.position for s in path])
    end = time.time()
    total_time = end - start
    runtime_sum = 0
    runtimes.append(total_time)
    for i in runtimes:
        runtime_sum += i

    average_runtime = runtime_sum / ITERATIONS
    print("average runtime: " + str(average_runtime))


for maze in mazes:
    # call_a_star(repForward.a_star, maze)
    call_a_star(repBack.a_star, maze)
    # call_a_star(repForLarge.a_star, maze)
    # call_a_star(repForSmall.a_star, maze)
    # call_a_star(adaptiveA.a_star, maze)
