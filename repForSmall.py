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
    c = n*n
    heappush(OPEN_LIST, (c*start_s.f-start_s.g, start_s))
    open_dict = {start_s: c*start_s.f-start_s.g}

    while OPEN_LIST:
        # identify s with smallest f-value
        curr_f, curr_s = heappop(OPEN_LIST)
        del open_dict[curr_s]
        # add state into closed list to expand
        CLOSED_LIST.add(curr_s)
        clv_list.append(curr_s)
        # found path from start to destination
        if curr_s == goal_s:
            return create_path(curr_s)
        # for each neighbor of current node
        for a in actions:
            succ_s = succ(curr_s, a, GRID)
            if succ_s is None:  # neighbor is an obstacle or out of bounds
                continue
            else:
                new_g = curr_s.g + 1
                for closed_s in CLOSED_LIST:
                    if closed_s == succ_s:
                        break
                else:
                    succ_s.g = new_g
                    succ_s.h = calc_h(succ_s.position, goal_s.position)
                    succ_s.f = succ_s.g + succ_s.h
                    # check if the state is in the OPEN_LIST
                    if succ_s in open_dict:
                        if open_dict[succ_s] <= c*succ_s.f-succ_s.g:
                            continue
                        del OPEN_LIST[OPEN_LIST.index(
                            (open_dict[succ_s], succ_s))]
                    heappush(OPEN_LIST, (c*succ_s.f-succ_s.g, succ_s))
                    open_dict[succ_s] = c*succ_s.f-succ_s.g
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
