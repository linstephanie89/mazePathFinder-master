from heapq import heappush, heappop
from main import state, actions, OPEN_LIST, CLOSED_LIST, clv_list


class forstate(state):
    def __lt__(self, other):
        if self.f == other.f:
            return self.g > other.g
        return self.f < other.f


def a_star(start_s, goal_s, GRID):
    # constant c to account for same f values
    n = len(GRID)
    c = (-n)*n
    heappush(OPEN_LIST, (c*start_s.f-start_s.g, start_s))
    g_values = {}
    open_dict = {start_s: c*start_s.f-start_s.g}
    min_cost = float('inf')

    while OPEN_LIST:
        curr_f, curr_s = heappop(OPEN_LIST)
        del open_dict[curr_s]
        CLOSED_LIST.add(curr_s)
        clv_list.append(curr_s)
        g_values[curr_s] = curr_s.g

        if curr_s == goal_s:
            if curr_s.g < min_cost:
                min_cost = curr_s.g
            return create_path(curr_s)

        for a in actions:
            # create state object for neighbor
            succ_s = succ(curr_s, a, GRID)
            if succ_s is None:  # neighbor is an obstacle or out of bounds
                continue
            # update the h-value if a lower g-value is found
            if succ_s in g_values and g_values[succ_s] <= curr_s.g:
                continue
            else:
                succ_s.g = curr_s.g + 1
                succ_s.h = calc_h(succ_s.position, goal_s.position)
                succ_s.f = succ_s.g + succ_s.h
                # check if the state is in the OPEN_LIST
                if succ_s in open_dict:
                    if open_dict[succ_s] <= c*succ_s.f-succ_s.g:
                        continue
                    del OPEN_LIST[OPEN_LIST.index((open_dict[succ_s], succ_s))]
                heappush(OPEN_LIST, (c*succ_s.f-succ_s.g, succ_s))
                open_dict[succ_s] = c*succ_s.f-succ_s.g
        for i in range(len(OPEN_LIST)):
            open_f, open_s = OPEN_LIST[i]
            if open_s not in g_values:
                continue
            new_h = calc_h(open_s.position, goal_s.position) + \
                g_values[open_s] - start_s.g
            if new_h < open_s.h:
                OPEN_LIST[i] = (open_s.g + new_h, open_s)
                heapify(OPEN_LIST)
    if min_cost == float('inf'):
        return None, None


def create_path(curr_s):
    path = []
    s = curr_s
    while s is not None:
        path.append(s)
        s = s.parent
    path.reverse()
    return path, curr_s.g

# function for generating successor state s based on action a


def succ(curr_s, a, GRID):
    x = curr_s.position[0]
    y = curr_s.position[1]
    if a == "up" and x > 0 and GRID[x-1][y] == 0:
        succ_s = forstate(curr_s, (x-1, y))
        return succ_s

    elif a == "down" and x < len(GRID)-1 and GRID[x+1][y] == 0:
        succ_s = forstate(curr_s, (x+1, y))
        return succ_s

    elif a == "left" and y > 0 and GRID[x][y-1] == 0:
        succ_s = forstate(curr_s, (x, y-1))
        return succ_s

    elif a == "right" and y < len(GRID)-1 and GRID[x][y+1] == 0:
        succ_s = forstate(curr_s, (x, y+1))
        return succ_s

    return None

# function for generating h based on manhattan distances


def calc_h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
